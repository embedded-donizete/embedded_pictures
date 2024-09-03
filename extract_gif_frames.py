import argparse, os

import PIL.GifImagePlugin
import PIL.Image

def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser()
    parser.add_argument("gif_image")
    parser.add_argument("output_folder")
    parser.add_argument("--width", required=False)
    parser.add_argument("--height", required=False)

    return parser.parse_args()

args = parse_args()

gif_name = args.gif_image
output_folder = args.output_folder
width = args.width
height = args.height

gif_image_file: PIL.GifImagePlugin.GifImageFile = PIL.Image.open(gif_name)

width = int(width) if width else gif_image_file.width
height = int(height) if height else gif_image_file.height

for frame in range(gif_image_file.n_frames):
    gif_image_file.seek(frame)
    image = gif_image_file.resize((width, height))
    image.save(os.path.join(output_folder, f"frame_{frame}.png"))