# coding=utf-8

"""ArUco Pattern Maker"""
import random
import cairo

from arucopatternmaker.algorithms.algorithms import draw_marker

def run_demo(page_size, landscape, fill_page, page_margin,
        marker_size, border_size, spacing, columns, rows, output, first,
        last, count, randomise, page_border, verbose):
    """ Run the application """
    pages = dict(A4=(210,297),A3=(297,420))
    page = pages[page_size]
    if landscape:
        page = (page[1],page[0])

    if count != 0:
        last = first + count - 1
    else:
        count = last - first + 1
    
    mm2pts = 2.83464567
    line_width = 0.5 # mm
    default_linewidth = 0.5
    border_colour = (0.0,0.0,0.0)

    if fill_page:
        columns = (page[0] - page_margin*2)/(marker_size + border_size*2
                + spacing)
        rows = (page[1] - page_margin*2)/(marker_size + border_size *2
                + spacing)

    bid = 0

    width_pts, height_pts = page[0] * mm2pts, page[1] * mm2pts
    surface = cairo.PDFSurface (output, width_pts, height_pts)

    ctx = cairo.Context (surface)

    ctx.scale(mm2pts,mm2pts)
    done = False

    number_of_tags = rows * columns
    if count < number_of_tags:
        number_of_tags = count
    number_of_tags = 100
    markers = [first + i for i in range(0, number_of_tags)]
    if randomise:
        random.shuffle(markers)


    with open(output+".txt","w") as reference_out:
        if page_border:
            ctx.set_source_rgb(*border_colour)
            ctx.set_line_width(line_width)
            ctx.rectangle(page_margin, page_margin,page[0]
                    -page_margin*2, page[1] - page_margin*2)
            ctx.set_line_width(default_linewidth) # default
            ctx.stroke()
        y = page_margin
        x = page_margin
        #lets hack this bit to do a bunch around the edges
        x = 3
        for y in range (6, 286 , 26):
            marker_id = markers[bid % len(markers)]
            reference_out.write(draw_marker(ctx, marker_id, 
                marker_size, marker_size,
                x + border_size,y + border_size))
            reference_out.write("\n")
            bid = bid + 1
            marker_id = markers[bid % len(markers)]
            bid = bid + 1

    ctx.show_page()
    surface.finish()
