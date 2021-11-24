from PIL import Image
import os


def convert_images_png():
    images = os.listdir("./images_to_be_converted")
    count = 0
    for image in images:

        img = Image.open(f"./images_to_be_converted/{image}")
        converted = img.convert("RGB")
        image_name = image.rsplit(".", 1)
        converted.save(f"converted_images/{image_name[0]}.png", "png")
        count += 1
        print(f"Image:{image} converted ({count}/{len(images)})")
        os.remove(f"./images_to_be_converted/{image}")


convert_images_png()
