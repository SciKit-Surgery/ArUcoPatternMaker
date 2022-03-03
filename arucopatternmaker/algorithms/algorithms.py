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


def drawMarker(ctx,id10,sw,sh,x,y):
    """
    draws an ArUco marker on the canvas

    :param ctx: the canvas context to draw on
    :param id10: the marker id to draw in base 10
    :param sw: The marker width
    :param sh: The marker height
    :param x: The marker centre (horizontal)
    :param y: The marker centre (vertical)

    :returns: a string defining the marker for a reference file
    """
    id = int2base(id10,4).zfill(5) # 0 padded 5 digits
    rows = [int(q) for q in id] # as integers
    marker_string = str(id10,"\t",x,"\t",y,"\t0\t",
             x - sw / 2,"\t",y-sh/2, "\t0\t",
             x + sw / 2,"\t",y-sh/2, "\t0\t",
             x + sw / 2,"\t",y+sh/2, "\t0\t",
             x - sw / 2,"\t",y+sh/2, "\t0\t")
    sw = sw/7.0
    sh = sh/7.0
    #val = padDigits(Number(id).toString(4),5);
    #rows = /(\d)(\d)(\d)(\d)(\d)/.exec(val).slice(1,6);
    #ctx = canvas.getContext('2d');
    #pad = canvas.pad;// || 15;
    #sw=(canvas.width - (pad*2))/7;
    #sh=(canvas.height - (pad*2))/7;
    #background white
    for h in range(0,7):
        for w in range(0,7):
            #print (h, w)
            if (w==0 or h==0 or h==6 or w==6):
                black = True
            elif markers_opts[rows[h - 1]][w - 1]:
                black = True
            else:
                black = False
            # draw rectangle at ... w*sw+pad h*sh+pad sized sw,sh
            # filled and stroken in white or black ... 
            if black:
                if ( True ):
                        #ctx.set_source_rgb(0,0.384,0.490)
                    ctx.set_source_rgb(0.0,0.0,0.0)
                else:
                    ctx.set_source_rgb(0.2,0.584,0.690)
            else:
                #continue
                ctx.set_source_rgb(1,1,1)
            #this stroke command draws a rectangle of some thickness, which
            #causes an overlap on the lines.
            #ctx.rectangle(w*sw + x,h*sh + y,sw,sh);
            #ctx.stroke();
            ctx.rectangle(w*sw + x,h*sh + y,sw,sh);
            ctx.fill();

    return marker_string


