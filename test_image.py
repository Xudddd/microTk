from microbit import *
from random import randint

display.show('TEST', 50, monospace=True)
display.scroll('img', 100)
while 1:
    img = Image('01234:56789:98765:43210:13579')
    stamp = Image(3, 3)
    while 1:
        display.show(img)
        for i in range(5):
            for x in range(5):
                for y in range(5):
                    img.set_pixel(x, y, max(0, img.get_pixel(x, y) - 1))
            display.show(img)
            sleep(100)
        if randint(1, 2) == 1:
            stamp.fill(randint(3, 9))
            img.blit(stamp, 0, 0, 3, 3, randint(0, 2), randint(0, 2))
        else:
            img += Image.HEART * randint(3, 9)