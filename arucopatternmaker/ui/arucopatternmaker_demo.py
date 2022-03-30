# coding=utf-8

"""ArUco Pattern Maker"""
import random
import cairo

from arucopatternmaker.algorithms.algorithms import draw_marker

def run_demo(page_size, landscape, #pylint: disable=too-many-arguments
        fill_page, page_margin, marker_size, border_size, spacing,
        columns, rows, output, first, last, count, randomise):
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

    number_of_tags = rows * columns
    if count < number_of_tags:
        number_of_tags = count
    number_of_tags = 100
    markers = [first + i for i in range(0, number_of_tags)]
    if randomise:
        random.shuffle(markers)

    with open(output+".txt","w", encoding='utf8') as reference_out:
        y_coord = page_margin
        x_coord = page_margin
        #lets hack this bit to do a bunch around the edges
        x_coord = 3
        for y_coord in range (6, 286 , 26):
            marker_id = markers[bid % len(markers)]
            reference_out.write(draw_marker(ctx, marker_id,
                marker_size, marker_size,
                x_coord + border_size,y_coord + border_size))
            reference_out.write("\n")
            bid = bid + 1
            marker_id = markers[bid % len(markers)]
            bid = bid + 1

    ctx.show_page()
    surface.finish()
