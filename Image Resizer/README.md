
# Image Resizer

This is a simple Python script that uses the Pillow library to resize a batch of images to a specified resolution.

## Requirements

- Python 3.x
- Pillow library

You can install the Pillow library using pip:

```bash
pip install pillow
```

## Usage

To use this script, you need to specify the directory of the images you want to resize, the directory where you want to save the resized images, and the dimensions (width and height) you want to resize your images to.

Here's an example:

```python
resize_images('/path/to/your/images', '/path/to/save/resized/images', 800, 600)
```

In this example:
- '/path/to/your/images' is the directory where your images are located.
- '/path/to/save/resized/images' is the directory where you want to save the resized images.
- 800 and 600 are the width and height you want to resize your images to.

Please replace '/path/to/your/images', '/path/to/save/resized/images', 800, and 600 with your actual values.

