#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Get an image. Display it and save it using PIL."""

import qi
import argparse
import sys
import time
from naoqi import ALProxy
from PIL import Image


def main():
    """
    First get an image, then show it on the screen with PIL.
    """
    # Get the service ALVideoDevice.
    IP = "192.168.1.9"
    PORT=9559
    try:
        global video
        video = ALProxy("ALVideoDevice",IP,9559)
    except Exception, e:
        print "Error: ",e

    resolution = 2    # VGA
    colorSpace = 11   # RGB

    videoClient = video.subscribe("python_client", resolution, colorSpace, 5)

    t0 = time.time()

    # Get a camera image.
    # image[6] contains the image data passed as an array of ASCII chars.
    naoImage = video.getImageRemote(videoClient)

    t1 = time.time()

    # Time the image transfer.
    print "acquisition delay ", t1 - t0

    video.unsubscribe(videoClient)


    # Now we work with the image returned and save it as a PNG  using ImageDraw
    # package.

    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]
    image_string = str(bytearray(array))

    # Create a PIL Image from our pixel array.
    im = Image.frombytes("RGB", (imageWidth, imageHeight), image_string)

    # Save the image.

    im.save("emocion.png", "PNG")

    im.show()
