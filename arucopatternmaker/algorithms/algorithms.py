"""Algorithms for the ArUco pattern maker application"""

import string

def int2base(int_x, base):
    """
    Convert an integer value (base 10) to another base

    :param int_x: a base 10 integer
    :param base: the base to convert to

    :returns: the number in a different base
    """
    character_set = string.digits + string.ascii_lowercase + \
          string.ascii_uppercase

    if int_x < 0:
        sign = -1
    elif int_x == 0:
        return character_set[0]
    else:
        sign = 1
    int_x *= sign
    digits = []
    while int_x:
        digits.append(character_set[int_x % base])
        int_x //= base
    if sign < 0:
        digits.append('-')

    digits.reverse()
    return ''.join(digits)


def draw_marker(ctx, id10, tag_width, tag_height, pos_x, pos_y,
        marker_colour = None, page_offset = None):
    """
    draws an ArUco marker on the canvas

    :param ctx: the canvas context to draw on
    :param id10: the marker id to draw in base 10
    :param tag_width: The marker width
    :param tag_height: The marker height
    :param pos_x: The marker centre (horizontal)
    :param pos_y: The marker centre (vertical)
    :param marker_colour: The marker colour to use, default black

    :returns: a string defining the marker for a reference file
    """
    if marker_colour is None:
        marker_colour = [0.0,0.0,0.0]

    if page_offset is None:
        page_offset = [-100, -135]

    tag_id = int2base(id10,4).zfill(5) # 0 padded 5 digits
    rows = [int(q) for q in tag_id] # as integers

    bit_width = tag_width/7.0
    bit_height = tag_height/7.0

    markers_opts = [[False,True,True,True,True],[False,True,False,False,False]
                   ,[True,False,True,True,False],[True,False,False,False,True]]


    for h_bit in range(0,7):
        for w_bit in range(0,7):
            if (w_bit==0 or h_bit==0 or h_bit==6 or w_bit==6):
                fill_bit = True
            elif markers_opts[rows[h_bit - 1]][w_bit - 1]:
                fill_bit = True
            else:
                fill_bit = False
            # draw rectangle at ... w*bit_width+pad h*bit_height+pad
            #sized bit_width,bit_height
            # filled and stroken in white or fill_colour ...
            if fill_bit:
                ctx.set_source_rgb(marker_colour[0], marker_colour[1],
                            marker_colour[2])
                ctx.rectangle(w_bit*bit_width + pos_x,h_bit*bit_height + pos_y,
                        bit_width, bit_height)
                ctx.fill()

    pos_x = pos_x + page_offset[0]
    pos_y = pos_y + page_offset[1]
    return (f"{id10}\t{pos_x}\t{pos_y}\t{0}"+
            f"\t{pos_x-tag_width/2}\t{pos_y-tag_height/2}\t{0}" +
            f"\t{pos_x+tag_width/2}\t{pos_y-tag_height/2}\t{0}" +
            f"\t{pos_x+tag_width/2}\t{pos_y+tag_height/2}\t{0}" +
            f"\t{pos_x-tag_width/2}\t{pos_y+tag_height/2}\t{0}")
