#!/usr/bin/env python

import Image

black = (0, 0, 0)
white = (255, 255, 255)

def view(ims, names = None):
    import pygame
    pygame.init()

    sw, sh = pygame.display.list_modes()[0]

    im = ims[0]
    width,height = im.size

    # Target size is 90% of sw
    zf = min(0.9 * sw / im.size[0], 0.6 * sh / im.size[1])

    ww = int(width * zf)
    size = width * zf,height * zf
    y0 = int(height * zf)
    y1 = int(height * zf + 40)

    screen = pygame.display.set_mode((ww, y1 + ww))

    fo = pygame.font.SysFont("freemono", 20)

    pygame.key.set_repeat(300, 50)

    screen.fill(black)
    def mainpic(im):
        b = pygame.image.fromstring(im.convert("RGB").tostring(), im.size, "RGB")
        return pygame.transform.scale(b, (int(zf * width), int(zf * height)))
    mp = mainpic(im)

    def announce(ss):
        for i,s in enumerate(ss):
            msg = fo.render(s, False, (255,255,255,128), (0,0,0,128))
            screen.blit(msg, (0, y0 + 20 * i))
            del msg

    (x, y) = (0, 0)
    (px, py) = (None, None)
    z = 7
    redraw = True
    while True:
        if redraw:
            screen.blit(mp, (0,0))
            if x < im.size[0] and y < im.size[1]:
                pixel = im.getpixel((x, y))
                if len(pixel) == 3:
                    (r, g, b) = pixel
                    a = 255
                elif len(pixel) == 4:
                    (r, g, b, a) = pixel
                if names is None:
                    fn = str(ims.index(im))
                else:
                    fn = names[ims.index(im)]
                pixval = " ".join(["%s=%02x" % (c, v) for (c, v) in zip(im.mode, pixel)])
                announce(["xy=%4d,%4d  (%d %d) %-16s" % (x, y, im.size[0], im.size[1], fn),
                          pixval + "  "])
                sub = im.crop((x - z/2, y - z/2, x + 1 + z/2, y + 1 + z/2))
                imsub = pygame.transform.scale(pygame.image.fromstring(sub.convert("RGB").tostring(), sub.size, "RGB"), (ww, ww))
                screen.blit(imsub, (0, y1))
                for i in range(1, z):
                    pygame.draw.line(screen, black, (0, y1 + ww * i / z), (ww, y1 + ww * i / z))
                    pygame.draw.line(screen, black, (ww * i / z, y1), (ww * i / z, y1 + ww))
                x0 = ww * (z / 2) / z
                x1 = ww * (z / 2 + 1) / z
                corners = [
                    (x0, y1 + x0),
                    (x1, y1 + x0),
                    (x1, y1 + x1),
                    (x0, y1 + x1)]
                pygame.draw.lines(screen, white, True, corners, 2)
                (px, py) = (x, y)
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == 27 or event.key == ord('q'):
                    pygame.display.quit()
                    return
                if event.key == ord(' '):
                    i = ims.index(im)
                    i = (i + 1) % len(ims)
                    im = ims[i]
                    mp = mainpic(im)
                    redraw = True
                if event.key == ord('-'):
                    z += 2
                    redraw = True
                if event.key == ord('='):
                    z -= 2
                    redraw = True
            if event.type == pygame.MOUSEMOTION:
                (x, y) = [int(c / zf) for c in event.pos]
                if (x, y) != (px, py):
                    redraw = True

if __name__ == '__main__':
    import sys
    ims = [Image.open(a) for a in sys.argv[1:]]
    view(ims, sys.argv[1:])
