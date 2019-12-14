from network import ImageTransformNet
from utils import *
import time

image_transformer = ImageTransformNet()
is_first = True


def transfer(content_path, style_path, output_path, reload=False):
    global is_first, decoder
    model = get_model_name_from_style_path(style_path)
    if is_first or reload:
        is_first = False
        if not torch.cuda.is_available():
            image_transformer.load_state_dict(torch.load(model, map_location=lambda storage, loc: storage))
        else:
            image_transformer.load_state_dict(torch.load(model))
        image_transformer.to(device)
    content = get_image_tensor_from_path(content_path, scale=False)
    style = get_image_tensor_from_path(style_path, scale=False)
    target = image_transformer(content)
    transfer_result_show(content, style, target, 'Transfer', save_file='_show'.join(os.path.splitext(output_path)))
    save_tensor_image(target, output_path)


def transfer_all():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    for style in os.listdir(STYLE_DIR):
        if not style.endswith('DS_Store'):
            for content in os.listdir(CONTENT_DIR):
                if not content.endswith('DS_Store'):
                    output = os.path.splitext(content)[0] + 'x' + os.path.splitext(style)[0] + '_Johnson.png'
                    # if os.path.exists(get_output_absolute_path(output)):
                    #     continue
                    now_time = time.time()
                    try:
                        transfer(get_content_absolute_path(content), get_style_absolute_path(style),
                                 get_output_absolute_path(output), reload=True)
                        print(f'generate content{content} and style{style} cost {time.time() - now_time} s')
                    except Exception as e:
                        print(f'generate content{content} and style{style} failed because of {e}')


if __name__ == '__main__':
    transfer_all()