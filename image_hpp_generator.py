import sys, os, itertools, re
import PIL.GifImagePlugin
import PIL.Image

folder_name = sys.argv[1]
picture_names = os.listdir(folder_name)
picture_names.sort(key=lambda f: int(re.sub('\D', '', f)))

output = open("Image.hpp", mode="w")

for i in range(len(picture_names)):
    image = PIL.Image.open(f"{folder_name}/{picture_names[i]}")
    image = image.convert("RGB")
    pixels = list(image.getdata())

    output.write(f"const unsigned char data_{i}[] = {'{'}")

    def to_rgb565(pixel):
        (r, g, b) = pixel
        return ((r & 0b11111000) << 8) | ((g & 0b11111100) << 3) | (b >> 3)
    
    def to_bytes(pixel): return (
        hex(pixel & 0xFF),
        hex(pixel >> 8)
    )

    pixels = map(to_rgb565, pixels)
    pixels = map(to_bytes, pixels)
    pixels = itertools.chain.from_iterable(pixels)
    pixels = ",".join(pixels)

    output.write(pixels)

    output.write("};\n\n")

output.write("\n")

output.write(f"const unsigned char* datas[] = {'{'}")

datas = map(
    lambda i: f"data_{i}", 
    [i for i in range(len(picture_names))]
)
datas = ",".join(datas)
output.write(datas)

output.write("};")