#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
@author: noogel
@file: gen.py
@date: 2019-09-24
"""

__author__ = "noogel"

import argparse

from PIL import Image

CANVAS_SIZE = (1080, 1080)


def constrain(size, height):
    aspect_ratio = size[0] / float(size[1])
    return int(aspect_ratio * height), height


def gen(image_path):
    bg_canvas = Image.new('RGBA', CANVAS_SIZE, (255, 255, 255, 0))
    bg_canvas.paste(Image.open("asset/bg.png"))

    cover_canvas = Image.new('RGBA', CANVAS_SIZE, (255, 255, 255, 0))
    cover_img = Image.open(image_path)
    cover_img = cover_img.resize(constrain(cover_img.size, CANVAS_SIZE[1]))
    cover_canvas.paste(cover_img, mask=Image.open("asset/mask.png"))

    return Image.alpha_composite(cover_canvas, bg_canvas)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file path")
    args = parser.parse_args()
    gen(args.input).save("{}_out.png".format(args.input.rsplit(".", 1)[0]))
