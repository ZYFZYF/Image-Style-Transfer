import torch
from torch import nn
from torchvision import models
from algorithms.utils import *
from algorithms.config import Gatys
from tqdm import tqdm
import os


class VggFeatureExtractor(nn.Module):
    def __init__(self):
        super(VggFeatureExtractor, self).__init__()
        self.content_layer = '21'  # conv4_2
        self.style_layers = ['0', '5', '10', '19', '28']  # conv1_1, conv2_1, conv3_1, conv4_1, conv5_1
        self.vgg_model = models.vgg19(pretrained=True).features

    def forward(self, x):
        content = None
        style = []
        for k, v in self.vgg_model._modules.items():
            x = v(x)
            if k in self.style_layers:
                style.append(x)
            if k == self.content_layer:
                content = x
        return content, style


def transfer(content_path, style_path, output_path):
    content = get_image_tensor_from_path(content_path, encoder=vgg_encoder, scale=True)
    style = get_image_tensor_from_path(style_path, encoder=vgg_encoder, scale=True)
    net = VggFeatureExtractor().to(device).eval()
    target = content.clone().requires_grad_(True)
    optimizer = torch.optim.Adam([target], lr=Gatys.learning_rate)
    for i in tqdm(range(Gatys.training_steps)):
        content_layer, _ = net(content)
        target_content_layer, target_style_layers = net(target)
        _, style_layers = net(style)
        content_loss = torch.mean(torch.pow(target_content_layer - content_layer, 2))
        style_loss = 0
        for target_layer, style_layer in zip(target_style_layers, style_layers):
            target_layer = target_layer.squeeze(0).reshape(target_layer.shape[1], -1)
            style_layer = style_layer.squeeze(0).reshape(style_layer.shape[1], -1)
            target_gram = torch.mm(target_layer, target_layer.t())
            style_gram = torch.mm(style_layer, style_layer.t())
            style_loss += torch.mean(torch.pow(target_gram - style_gram, 2)) / len(target_style_layers) / \
                          target_layer.shape[
                              0] / target_layer.shape[1]
        normalize_loss = smooth_loss(target)
        total_loss = Gatys.alpha * content_loss + Gatys.beta * style_loss + Gatys.gamma * normalize_loss
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
        if (i + 1) % Gatys.show_step == 0:
            print('now {}/{} content loss is {}, style loss iss {} and total loss is {}'.format(i + 1,
                                                                                                Gatys.training_steps,
                                                                                                content_loss,
                                                                                                style_loss,
                                                                                                total_loss.item()))
            # transfer_result_show(content, style, target, 'Target {}/{}'.format(i + 1, Gatys.training_steps))
    transfer_result_show(content, style, target, 'Transfer', save_file='_show'.join(os.path.splitext(output_path)))
    save_tensor_image(target, output_path)


def transfer_all():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    for content in os.listdir(CONTENT_DIR):
        if not content.endswith('DS_Store'):
            for style in os.listdir(STYLE_DIR):
                if not style.endswith('DS_Store'):
                    output = os.path.splitext(content)[0] + 'x' + os.path.splitext(style)[0] + '_Gatys.png'
                    if os.path.exists(get_output_absolute_path(output)):
                        continue
                    transfer(get_content_absolute_path(content), get_style_absolute_path(style),
                             get_output_absolute_path(output))


if __name__ == '__main__':
    transfer_all()
    # transfer(get_content_absolute_path('2.png'), get_style_absolute_path('1.png'), get_output_absolute_path('2x1.png'))l
    # print(models.vgg19(pretrained=True).features)
