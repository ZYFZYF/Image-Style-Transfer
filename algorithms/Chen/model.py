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
            nn.InstanceNorm2d(out_channels))

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


if __name__ == '__main__':
    encoder = VGGEncoder()
