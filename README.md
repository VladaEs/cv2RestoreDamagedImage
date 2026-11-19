# Image Inpainting

This project restores images with black lines using OpenCV's TELEA and Navier-Stokes inpainting methods. It generates and widens a mask around the damaged areas, then displays the original image, mask, and both results.

## Run

Install the dependencies:

```bash
pip install opencv-python matplotlib
```

Run the script from the project directory:

```bash
python main.py
```

The input images are in the `images` folder. Large images may take longer to process.