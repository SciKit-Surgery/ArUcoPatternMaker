"""Algorithms for the ArUco pattern maker application"""

import string

def int2base(x, base):
  """
  Convert an integer value (base 10) to another base
  
  :param x: a base 10 integer
  :param base: the base to convert to

  :returns: the number in a different base
  """
  character_set = string.digits + string.ascii_lowercase + \
          string.ascii_uppercase

  if x < 0: 
      sign = -1
  elif x == 0: 
      return character_set[0]
  else: 
      sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(character_set[x % base])
    x //= base
  if sign < 0:
    digits.append('-')
  
  digits.reverse()
  return ''.join(digits)


def drawMarker(ctx,id10,tag_width,tag_height,x,y,marker_colour = [0.0,0.0,0.0]):
    """
    draws an ArUco marker on the canvas

    :param ctx: the canvas context to draw on
    :param id10: the marker id to draw in base 10
    :param tag_width: The marker width
    :param tag_height: The marker height
    :param x: The marker centre (horizontal)
    :param y: The marker centre (vertical)
    :param marker_colour: The marker colour to use, default black

    :returns: a string defining the marker for a reference file
    """
    id = int2base(id10,4).zfill(5) # 0 padded 5 digits
    rows = [int(q) for q in id] # as integers
    
    bit_width = tag_width/7.0
    bit_height = tag_height/7.0

    markers_opts = [[False,True,True,True,True],[False,True,False,False,False]
                   ,[True,False,True,True,False],[True,False,False,False,True]];
    background_colour = [1.0, 1.0, 1.0]


    for h in range(0,7):
        for w in range(0,7):
            if (w==0 or h==0 or h==6 or w==6):
                fill_bit = True
            elif markers_opts[rows[h - 1]][w - 1]:
                fill_bit = True 
            else:
                fill_bit = False
            # draw rectangle at ... w*bit_width+pad h*bit_height+pad sized bit_width,bit_height
            # filled and stroken in white or fill_colour ... 
            if fill_bit:
                ctx.set_source_rgb(marker_colour[0], marker_colour[1], 
                            marker_colour[2])
                ctx.rectangle(w*bit_width + x,h*bit_height + y, bit_width, bit_height);
                ctx.fill();

    return (f"{id10}\t{x}\t{y}\t{0}"+
            f"\t{x-tag_width/2}\t{y-tag_height/2}\t{0}" +
            f"\t{x+tag_width/2}\t{y-tag_height/2}\t{0}" +
            f"\t{x+tag_width/2}\t{y+tag_height/2}\t{0}" +
            f"\t{x-tag_width/2}\t{y+tag_height/2}\t{0}")

