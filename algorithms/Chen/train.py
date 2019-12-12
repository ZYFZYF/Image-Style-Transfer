from utils import *
from config import Chen
from Chen.model import *
from Chen.transfer import transfer
from tqdm import tqdm
import random
import numpy as np


def get_parameter_number(net):
    total_num = sum(p.numel() for p in net.parameters())
    trainable_num = sum(p.numel() for p in net.parameters() if p.requires_grad)
    return {'Total': total_num, 'Trainable': trainable_num}


def train():
    train_contents = [TRAIN_CONTENT_DIR + content for content in os.listdir(TRAIN_CONTENT_DIR)]
    train_styles = [TRAIN_STYLE_DIR + style for style in os.listdir(TRAIN_STYLE_DIR)]
    print(f'Totally we have {len(train_contents)} contents and {len(train_styles)} styles')

    loss_fn = nn.MSELoss(reduction='mean')
    encoder = VGGEncoder().to(device)
    decoder = VGGDecoder().to(device)
    optimizer = torch.optim.Adam(decoder.parameters(), lr=Chen.learning_rate)
    print(f'we have {get_parameter_number(decoder)} parameters in VGGDecoder to learn')
    loss_list = []

    for i in tqdm(range(Chen.training_steps)):
        # 一次训练batch_size个
        content_list = []
        style_list = []
        for j in range(Chen.batch_size):
            while True:
                rand_content = train_contents[np.random.randint(len(train_contents))]
                rand_style = train_styles[np.random.randint(len(train_styles))]
                try:
                    content = get_image_tensor_from_path(rand_content)
                    style = get_image_tensor_from_path(rand_style)
                    break
                except Exception as e:
                    print(f'get content {rand_content} and style {rand_style} failed')
            content_list.append(content)
            style_list.append(style)
        content = torch.cat(content_list, dim=0)
        style = torch.cat(style_list, dim=0)

        content_feature = encoder(content)
        style_feature = encoder(style)
        # style swap这步操作必须每一维单独做
        target_features = []
        for j in range(Chen.batch_size):
            target_features.append(
                style_swap(content_feature[j].unsqueeze(0), style_feature[j].unsqueeze(0), patch_size=3))
        target_feature = torch.cat(target_features, dim=0)

        content_reconstruct = decoder(content_feature)
        style_reconstruct = decoder(style_feature)
        target_reconstruct = decoder(target_feature)

        content_reconstruct_feature = encoder(content_reconstruct)
        style_reconstruct_feature = encoder(style_reconstruct)
        target_reconstruct_feature = encoder(target_reconstruct)

        # 三类loss
        image_reconstruction_loss = loss_fn(content, content_reconstruct) + loss_fn(style, style_reconstruct)
        # TODO 这里加上目标图表的风格重建分是否合适
        feature_reconstruction_loss = loss_fn(content_feature, content_reconstruct_feature) + loss_fn(style_feature,
                                                                                                      style_reconstruct_feature) + loss_fn(
            target_feature, target_reconstruct_feature)
        normalize_loss = smooth_loss(content_reconstruct) + smooth_loss(style_reconstruct) + smooth_loss(
            target_reconstruct)
        total_loss = image_reconstruction_loss + feature_reconstruction_loss + normalize_loss

        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

        loss_list.append(total_loss.item())

        if (i + 1) % Chen.show_step == 0:
            torch.save(decoder.state_dict(), 'model.pt')
            transfer(get_content_absolute_path('12.jpg'), get_style_absolute_path('8.jpg'),
                     get_output_absolute_path(f'12x8_Chen_{i + 1}_of_{Chen.training_steps}.jpg'), reload=True)
            plt.plot(range(len(loss_list)), loss_list)
            plt.ylim((0, 10))
            plt.xlabel('iteration')
            plt.ylabel('loss')
            plt.title('train loss')
            plt.savefig(f'train_loss.png')
            print(
                f'now image loss is {image_reconstruction_loss.item()}, feature loss is {feature_reconstruction_loss.item()}, smooth loss is {normalize_loss.item()} and total loss is {total_loss.item()}')


if __name__ == '__main__':
    train()
