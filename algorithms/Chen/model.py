import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision


class VGGEncoder(nn.Module):
    def __init__(self):
        super(VGGEncoder, self).__init__()
        self.net = torchvision.models.vgg19(pretrained=True).features[:12]
        # 冻结vgg网络的参数
        for p in self.parameters():
            p.requires_grad = False

    def forward(self, image):
        return self.net(image)


class CIR(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, padding_size=1):
        super(CIR, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size,
                      stride=stride, padding=padding_size),
            # nn.InstanceNorm2d(out_channels),
            nn.ReLU())

    def forward(self, x):
        return self.model(x)


class VGGDecoder(nn.Module):
    def __init__(self):
        super(VGGDecoder, self).__init__()
        self.model = nn.Sequential(
            CIR(in_channels=256, out_channels=128),
            nn.UpsamplingNearest2d(scale_factor=2),
            CIR(in_channels=128, out_channels=128),
            CIR(in_channels=128, out_channels=64),
            nn.UpsamplingNearest2d(scale_factor=2),
            CIR(in_channels=64, out_channels=64),
            nn.Conv2d(in_channels=64, out_channels=3, kernel_size=3, stride=1, padding=1)
        )

    def forward(self, x):
        return self.model(x)


def style_swap(content_feature, style_feature, patch_size):
    # 这里顺序不能颠倒(滑动窗口）
    patches = style_feature.unfold(2, patch_size, 1).unfold(3, patch_size, 1)
    # print(patches[0, 0, 0, 0])
    # print(patches.shape)
    # 把通道维移到后面
    patches = patches.permute(0, 2, 3, 1, 4, 5)
    patches = patches.reshape(-1, patches.shape[3], patches.shape[4], patches.shape[5])
    # 将patches归一化
    norm = torch.norm(patches.reshape(patches.shape[0], -1), dim=1).reshape(-1, 1, 1, 1)
    normalize_patches = patches / norm
    # 卷积
    conv = F.conv2d(content_feature, normalize_patches)
    # 找到每个位置相似度最大的位置
    one_hots = torch.zeros_like(conv)
    one_hots.scatter_(1, conv.argmax(dim=1, keepdim=True), 1)
    # 转置卷积
    deconv = F.conv_transpose2d(one_hots, patches)
    # 因为重叠的原因每个点会被更新多次，因此算一下重叠的次数再平均一下
    overlap = F.conv_transpose2d(one_hots, torch.ones_like(patches))
    return deconv / overlap


if __name__ == '__main__':
    x = torch.rand(1, 3, 8, 8)
    y = torch.rand(1, 3, 8, 8)
    y[0, 0, 0, 0] = 0
    y[0, 0, 0, 1] = 1
    y[0, 0, 0, 2] = 2
    y[0, 0, 1, 0] = 3
    y[0, 0, 1, 1] = 4
    y[0, 0, 1, 2] = 5
    y[0, 0, 2, 0] = 6
    y[0, 0, 2, 1] = 7
    y[0, 0, 2, 2] = 8
    print(y[0, 0])
    style_swap(x, y, 3)
