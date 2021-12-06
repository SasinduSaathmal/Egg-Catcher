from pygame import transform


def small_img(img, factor):
    size = round(img.get_width() // factor), round(img.get_height() // factor)
    return transform.scale(img, size)


def large_img(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return transform.scale(img, size)


def scale_desk(img, width, height):
    size = round(img.get_width() * width), round(img.get_height() // height)
    return transform.scale(img, size)


def blit_text_center(win, font, text: str , color: tuple, height: int = 0, width: int = 0):
    render = font.render(text, 1, color)
    win.blit(render, (win.get_width() / 2 - render.get_width() /
             2, (win.get_height() + height) / 2 - render.get_height() / 2))

