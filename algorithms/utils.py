import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import os

CONTENT_DIR = os.path.dirname(os.path.dirname(__file__)) + '/image/content/'
STYLE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/image/style/'
OUTPUT_DIR = os.path.dirname(os.path.dirname(__file__)) + '/image/output/'

TRAIN_CONTENT_DIR = os.path.dirname(os.path.dirname(__file__)) + '/dataset/content/'
TRAIN_STYLE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/dataset/style/'


def get_content_absolute_path(filename):
    return CONTENT_DIR + filename


def get_style_absolute_path(filename):
    return STYLE_DIR + filename


def get_output_absolute_path(filename):
    return OUTPUT_DIR + filename


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
default_encoder = transforms.Compose([transforms.ToTensor()])
default_decoder = transforms.ToPILImage()
vgg_encoder = transforms.Compose([transforms.ToTensor(),
                                  transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
vgg_decoder = transforms.Compose([transforms.Normalize(mean=[-2.118, -2.036, -1.804], std=[4.366, 4.464, 4.444]),
                                  transforms.Lambda(lambda img: torch.clamp(img, 0, 1)),
                                  transforms.ToPILImage()])


def get_image_tensor_from_path(image_path, encoder=default_encoder, scale=True, output_size=(256, 256)):
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
    image = encoder(image).unsqueeze(0)
    return image.to(device, torch.float)


def get_image_from_tensor(tensor, decoder=vgg_decoder):
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = decoder(image)
    return image


def tensor_image_show(tensor, title=None):
    image = get_image_from_tensor(tensor)
    plt.imshow(image)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)


plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300


def transfer_result_show(content_tensor, style_tensor, target_tensor, target_show_name, save_file=None):
    content = get_image_from_tensor(content_tensor)
    fig = plt.figure()
    plt.sca(fig.add_subplot(1, 3, 1))
    plt.imshow(content)
    plt.title('Content')
    plt.xticks([])
    plt.yticks([])
    style = get_image_from_tensor(style_tensor)
    plt.sca(fig.add_subplot(1, 3, 2))
    plt.imshow(style)
    plt.title('Style')
    plt.xticks([])
    plt.yticks([])
    target = get_image_from_tensor(target_tensor)
    plt.sca(fig.add_subplot(1, 3, 3))
    plt.imshow(target)
    plt.title(target_show_name)
    plt.xticks([])
    plt.yticks([])
    # plt.show(block=False)
    # plt.pause(0.01)
    if save_file:
        plt.savefig(save_file)
    plt.close(fig)


def save_tensor_image(tensor, image_path):
    image = get_image_from_tensor(tensor)
    image.save(image_path)


# 光滑正则项，为了让图片显得更加自然、光滑以及减少突变
def smooth_loss(img):
    h_loss = torch.sum(torch.pow(img[:, :, :, :-1] - img[:, :, :, 1:], 2))
    w_loss = torch.sum(torch.pow(img[:, :, :-1, :] - img[:, :, 1:, :], 2))
    # 之所以除以2是因为本质上是算了两个差的和
    return (h_loss + w_loss) / (img.shape[1] * img.shape[2] * img.shape[3] * 2)


if __name__ == '__main__':
    get_image_tensor_from_path('../image/content/1.png')
