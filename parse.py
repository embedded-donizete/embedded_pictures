from typing import Tuple

def rgb_tuple_to_rgb565_int(
    pixel: Tuple[int, int, int]
) -> int:
    (r, g, b) = pixel
    r = (r & 0b11111000) << 8
    g = (g & 0b11111100) << 3
    b = b >> 3
    return r | g | b

def int_to_bytes(
    number: int, 
    size: int = 2, 
    is_big_endian: bool = False
) -> list[int]:
    MASK = 0xFF
    bytes = []
    for i in range(size): bytes.append((number >> (i * 8)) & MASK)
    if is_big_endian: bytes.reverse()
    return bytes