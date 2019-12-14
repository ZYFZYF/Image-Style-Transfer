from Gatys.transfer import VggFeatureExtractor
from utils import *
from tqdm import tqdm
from config import Johnson
import numpy as np
from network import ImageTransformNet
import torch.nn as nn
import time
from Johnson.transfer import transfer


def train(style_path):
    # 模型载入
    vgg = VggFeatureExtractor().to(device).eval()
    image_transformer = ImageTransformNet().to(device)
    optimizer = torch.optim.Adam(image_transformer.parameters(), lr=Johnson.learning_rate)
    loss_fn = nn.MSELoss()
    # 先把style的信息拿出来
    style = get_image_tensor_from_path(style_path)
    _, style_layers = vgg(style)
    style_gram = []
    for style_layer in style_layers:
        style_layer = style_layer.reshape(style_layer.shape[1], -1)
        style_gram.append(torch.mm(style_layer, style_layer.t()))

    train_contents = [TRAIN_CONTENT_DIR + content for content in os.listdir(TRAIN_CONTENT_DIR)]
    loss_list = []

    for i in tqdm(range(Johnson.training_steps)):
        content_list = []
        for j in range(Johnson.batch_size):
            while True:
                rand_content = train_contents[np.random.randint(len(train_contents))]
                try:
                    content = get_image_tensor_from_path(rand_content)
                    break
                except Exception as e:
                    print(f'get content {rand_content} failed')
            content_list.append(content)
        content = torch.cat(content_list, dim=0)
        target = image_transformer(content)
        target_content_layer, target_style_layers = vgg(target)
        content_layer, _ = vgg(content)
        content_loss = loss_fn(target_content_layer, content_layer)
        style_loss = 0
        for j in range(len(target_style_layers)):
            for k in range(Johnson.batch_size):
                target_layer = target_style_layers[j][k].reshape(target_style_layers[j][k].shape[0], -1)
                target_gram = torch.mm(target_layer, target_layer.t())
                style_loss += loss_fn(target_gram, style_gram[j])
        style_loss /= Johnson.batch_size

        normalize_loss = smooth_loss(target)
        total_loss = Johnson.alpha * content_loss + Johnson.beta * style_loss + Johnson.gamma * normalize_loss
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

        loss_list.append(total_loss.item())
        if (i + 1) % Johnson.show_step == 0:
            now_time = time.time()
            torch.save(image_transformer.state_dict(), get_model_name_from_style_path(style_path))
            print(f'save cost {time.time() - now_time}')
            now_time = time.time()
            transfer(get_content_absolute_path('12.jpg'), get_style_absolute_path('8.jpg'),
                     get_output_absolute_path(f'12x8_John_{i + 1}_of_{Johnson.training_steps}.jpg'), reload=True)
            print(f'transfer cost {time.time() - now_time}')

            now_time = time.time()
            plt.plot(range(len(loss_list)), loss_list)
            plt.ylim((0, 20))
            plt.xlabel('iteration')
            plt.ylabel('loss')

            plt.title('train loss')
            plt.savefig(f'train_loss.png')
            print(f'draw loss cost {time.time() - now_time}')
        print(
            'now {}/{} content loss is {}, style loss iss {}, smooth loss is {} and total loss is {}'.format(i + 1,
                                                                                                             Johnson.training_steps,
                                                                                                             content_loss,
                                                                                                             style_loss,
                                                                                                             normalize_loss,
                                                                                                             total_loss.item()))
        # transfer_result_show(content, style, target, 'Target {}/{}'.format(i + 1, Gatys.training_steps))


if __name__ == '__main__':
    train(get_style_absolute_path('4.png'))
