import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
loader = transforms.Compose([transforms.ToTensor()])
unloader = transforms.ToPILImage()


def get_image_tensor_from_path(image_path, scale=True, output_size=(256, 256)):
    image = Image.open(image_path).convert('RGB')
    if scale:
        # 为了简化，一旦缩放这里均认为输出是正方形图片
        width, height = image.size
        # 窄的图片取上方，宽的图片取中间
        if width < height:
            image = image.crop((0, 0, width, width))
        else:
            image = image.crop((width / 2 - height / 2, 0, width / 2 + height / 2, height))
        image = image.resize(output_size)
    plt.imshow(image)
    plt.pause(0.01)
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)


def get_image_from_tensor(tensor):
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = unloader(image)
    return image


def tensor_image_show(tensor, title=None):
    image = get_image_from_tensor(tensor)
    plt.imshow(image)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)


def save_tensor_image(tensor, image_path):
    image = get_image_from_tensor(tensor)
    image.save(image_path)


if __name__ == '__main__':
    get_image_tensor_from_path('../image/content/1.png')
