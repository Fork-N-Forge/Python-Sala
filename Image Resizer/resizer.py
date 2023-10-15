from PIL import Image
import os

def resize_images(image_directory, output_directory, width, height):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(image_directory):
        if filename.endswith(".jpg"):  # specify your file type
            img = Image.open(os.path.join(image_directory, filename))
            img = img.resize((width, height))
            img.save(os.path.join(output_directory, filename))

# usage
resize_images('/path/to/your/images', '/path/to/save/resized/images', 800, 600)
