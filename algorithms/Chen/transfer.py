from model import *
from utils import *

encoder = VGGEncoder().to(device)
decoder = VGGDecoder()
if not torch.cuda.is_available():
    decoder.load_state_dict(torch.load('model.pt', map_location=lambda storage, loc: storage))
else:
    decoder.load_state_dict(torch.load('model.pt'))
decoder.to(device)


def transfer(content_path, style_path, output_path, reload=False):
    if reload:
        global decoder
        decoder = VGGDecoder()
        if not torch.cuda.is_available():
            decoder.load_state_dict(torch.load('model.pt', map_location=lambda storage, loc: storage))
        else:
            decoder.load_state_dict(torch.load('model.pt'))
        decoder.to(device)
    content = get_image_tensor_from_path(content_path)
    style = get_image_tensor_from_path(style_path)
    content_feature = encoder(content)
    style_feature = encoder(style)
    target_feature = style_swap(content_feature, style_feature, patch_size=3)
    target_reconstruct = decoder(target_feature)
    transfer_result_show(content, style, target_reconstruct, 'Transfer',
                         save_file='_show'.join(os.path.splitext(output_path)))
    save_tensor_image(target_reconstruct, output_path)


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
