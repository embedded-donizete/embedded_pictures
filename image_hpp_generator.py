import argparse, os, itertools

import PIL.GifImagePlugin
import PIL.Image

from parse import rgb_tuple_to_rgb565_int, int_to_bytes

def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder")
    parser.add_argument("--template", default="frame_%d.png")
    parser.add_argument("--data_type", default="uint16_t", choices=["uint8_t", "uint16_t"])

    return parser.parse_args()

args = parse_args()

input_folder = args.input_folder
template = args.template
data_type = args.data_type

output = open("Image.hpp", mode="w")
image_counting = len(os.listdir(input_folder))

for i in range(image_counting):
    image = PIL.Image.open(os.path.join(input_folder, template % i))
    image = image.convert("RGB")
    pixels = list(image.getdata())

    output.write("#include <stdint.h>\n\n")

    output.write(f"const {data_type} data_{i}[] = {'{'}")

    pixels = map(rgb_tuple_to_rgb565_int, pixels)
    if data_type == "uint8_t":
        pixels = map(int_to_bytes, pixels)
        pixels = itertools.chain.from_iterable(pixels)
    pixels = map(hex, pixels)
    pixels = ",".join(pixels)

    output.write(pixels)

    output.write("};\n\n")

output.write("\n")

output.write(f"const {data_type}* datas[] = {'{'}")

datas = map(
    lambda i: f"data_{i}", 
    [i for i in range(image_counting)]
)
datas = ",".join(datas)
output.write(datas)

output.write("};")