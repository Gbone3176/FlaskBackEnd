from PIL import Image

def resize_image(input_image_path, output_image_path, size=(32, 32)):
    with Image.open(input_image_path) as image:
        # 使用LANCZOS滤镜进行高质量的下采样
        resized_image = image.resize(size, Image.Resampling.LANCZOS)
        resized_image.save(output_image_path)

# 使用示例
input_path = '../../../Downloads/figs/Gbone.jpg'  # 替换为你的图片路径
output_path = '../static/Gbone32.jpg'  # 输出图片的路径
resize_image(input_path, output_path)
