from PIL import Image
from random import randint, choice, sample

doras = [Image.open('doras/%d.png' % i, 'r') for i in xrange(1,11)]
swiper = Image.open('swiper.png', 'r').convert('LA')
monkey = Image.open('monkey.png', 'r').convert('LA')

size = 144,144

bag = Image.open('bag.png', 'r').convert('LA')
bag.thumbnail(size, Image.ANTIALIAS)

isa = Image.open('isa.png', 'r').convert('LA')
isa.thumbnail(size, Image.ANTIALIAS)

bull = Image.open('bull.png', 'r').convert('LA')
bull.thumbnail(size, Image.ANTIALIAS)

def random_offset_in_quad(pos):
    if pos == 1:
        offset = randint(720, 1440-288), randint(0, 720-288)
    if pos == 2:
        offset = randint(0, 720-288), randint(0, 720-288)
    if pos == 3:
        offset = randint(0, 720-288), randint(720, 1440-288)
    if pos == 4:
        offset = randint(720, 1440-288), randint(720, 1440-288)
    return offset

def overlap(dora_offset, dora_size, offset, size):
    if offset[0] <= dora_offset[0]+dora_size[0] and offset[0] >= dora_offset[0] and offset[1] <= dora_offset[1]+dora_size[1] and offset[1] >= dora_offset[1]:
        return True
    if offset[0]+size[0] <= dora_offset[0]+dora_size[0] and offset[0]+size[0] >= dora_offset[0] and offset[1]+size[1] <= dora_offset[1]+dora_size[1] and offset[1]+size[1] >= dora_offset[1]:
        return True
    if offset[0]+size[0] <= dora_offset[0]+dora_size[0] and offset[0]+size[0] >= dora_offset[0] and offset[1] <= dora_offset[1]+dora_size[1] and offset[1] >= dora_offset[1]:
        return True
    if offset[0] <= dora_offset[0]+dora_size[0] and offset[0] >= dora_offset[0] and offset[1]+size[1] <= dora_offset[1]+dora_size[1] and offset[1]+size[1] >= dora_offset[1]:
        return True
    return False

def overlaps(arr, offset, size):
    for idx,obj in enumerate(arr):
        if overlap(obj[0], obj[1], offset, size):
            # print arr, offset, size, idx
            return True
    return False

def randomize_palette(img):
    r = randint(1,4)
    if r == 1:
        return img.convert("LA")
    elif r == 2:
        return img.convert("P", palette=Image.ADAPTIVE, colors=4)
    elif r == 3:
        return img.convert("P", palette=Image.ADAPTIVE, colors=8)
    elif r == 4:
        return img.convert("P", palette=Image.ADAPTIVE, colors=16)

for _ in xrange(800):
    objects = []
    dora_idx = randint(0,9)
    dora = randomize_palette(doras[dora_idx])
    dora_size = randint(144,288),randint(144,288)
    dora.thumbnail(dora_size, Image.ANTIALIAS)
    swiper_size = randint(144,288),randint(144,288)
    swiper.thumbnail(swiper_size, Image.ANTIALIAS)
    monkey_size = randint(144,288),randint(144,288)
    monkey.thumbnail(monkey_size, Image.ANTIALIAS)

    background = Image.new('RGBA', (1440, 1440), (randint(0,255), randint(0,255), randint(0,255),255))
    foreground = Image.new('RGBA', (1440, 1440), (0,0,0,0))
    bg_w, bg_h = background.size

    pos = sample(range(1,5),3)

    dora_offset = random_offset_in_quad(pos[0])
    foreground.paste(dora, dora_offset)
    objects.append((dora_offset, dora_size))

    offset = random_offset_in_quad(pos[1])
    while overlaps(objects, offset, swiper_size):
        offset = random_offset_in_quad(pos[1])
    foreground.paste(swiper, offset)
    objects.append((offset, swiper_size))

    offset = random_offset_in_quad(pos[2])
    while overlaps(objects, offset, monkey_size):
        offset = random_offset_in_quad(pos[2])
    foreground.paste(monkey, offset)
    objects.append((offset, monkey_size))

    offset = randint(0,1440-144),randint(0,1440-144)
    while overlaps(objects, offset, (144,144)):
        offset = randint(0,1440-144),randint(0,1440-144)
    foreground.paste(isa, offset)
    objects.append((offset, (144,144)))

    offset = randint(0,1440-144),randint(0,1440-144)
    while overlaps(objects, offset, (144,144)):
        offset = randint(0,1440-144),randint(0,1440-144)
    foreground.paste(bag, offset)
    objects.append((offset, (144,144)))

    offset = randint(0,1440-144),randint(0,1440-144)
    while overlaps(objects, offset, (144,144)):
        offset = randint(0,1440-144),randint(0,1440-144)
    foreground.paste(bull, offset)
    # foreground.paste(isa, (randint(0,1440-144),randint(0,1440-144)))
    # foreground.paste(bag, (randint(0,1440-144),randint(0,1440-144)))
    # foreground.paste(bull, (randint(0,1440-144),randint(0,1440-144)))
    background.paste(foreground, (0,0),foreground)
    background = background.resize((720,720), Image.ANTIALIAS)
    background.save('out/%d/%d.png' % (pos[0],_), optimize=True, quality=10)
    print _
