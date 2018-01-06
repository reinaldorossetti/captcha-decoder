from PIL import Image, ImageEnhance, ImageFilter


def iterate(im, iteration):
    if iteration == 0:
        return im

    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    if iteration != 1:
        # applying contrast
        im = enhancer.enhance(2)
        im.show()
    # convert to mode 1.
    im = im.convert('1')
    im.show()

    return iterate(im, iteration - 1)
