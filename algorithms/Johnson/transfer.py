from network import ImageTransformNet
from utils import *
import time

image_transformer = ImageTransformNet()
now_model = None


def transfer(content_path, style_path, output_path):
    content = get_image_tensor_from_path(content_path)
    # style = get_image_tensor_from_path(style_path)
    target = image_transformer(content)
    # transfer_result_show(content, style, target, 'Transfer', save_file='_show'.join(os.path.splitext(output_path)))
    save_tensor_image(target, output_path)


def reload_model(model_path):
    global now_model
    if now_model != model_path:
        now_model = model_path
        if not torch.cuda.is_available():
            image_transformer.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage))
        else:
            image_transformer.load_state_dict(torch.load(model_path))
        image_transformer.to(device)


def transfer_all():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    for style in os.listdir(STYLE_DIR):
        if not style.endswith('DS_Store'):
            model = get_model_name_from_style_path(style)
            if os.path.exists(model):
                reload_model(model)
                for content in os.listdir(CONTENT_DIR):
                    if not content.endswith('DS_Store'):
                        output = os.path.splitext(content)[0] + 'x' + os.path.splitext(style)[0] + '_Johnson.png'
                        if os.path.exists(get_output_absolute_path(output)):
                            continue
                        now_time = time.time()
                        try:
                            transfer(get_content_absolute_path(content), get_style_absolute_path(style),
                                     get_output_absolute_path(output))
                            print(f'generate content{content} and style{style} cost {time.time() - now_time} s')
                        except Exception as e:
                            print(f'generate content{content} and style{style} failed because of {e}')


if __name__ == '__main__':
    transfer_all()
