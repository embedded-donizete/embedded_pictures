import sys, os, pathlib, shutil
import PIL
import PIL.GifImagePlugin
import PIL.Image

gif_name = sys.argv[1]
gif_image_file: PIL.GifImagePlugin.GifImageFile = PIL.Image.open(gif_name)

folder_name = pathlib.Path(gif_name).stem
if pathlib.Path(folder_name).is_dir():
    shutil.rmtree(folder_name)
os.mkdir(folder_name)

for frame in range(gif_image_file.n_frames):
    gif_image_file.seek(frame)
    image = gif_image_file.resize((64, 64))
    image.save(f"{folder_name}/{folder_name}_{frame}.png")