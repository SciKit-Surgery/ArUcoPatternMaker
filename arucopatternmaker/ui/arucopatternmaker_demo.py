# coding=utf-8

"""ArUco Pattern Maker"""
import cairo,argparse,random

from arucopatternmaker.algorithms.algorithms import draw_marker

def run_demo(page_size, page_count, landscape, fill_page, page_margin,
        marker_size, border_size, spacing, columns, rows, output, first,
        last, count, randomise, page_border, verbose):
    """ Run the application """
    pages = dict(A4=(210,297),A3=(297,420))
    page = pages[page_size]
    if landscape:
        page = (page[1],page[0])

    mm2pts = 2.83464567
    lw = 0.5 # mm
    lwdef = 0.5
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

    n = page_count * rows * columns
    if count < n:
        n = count
    n=100
    markers = [first + i for i in range(0,n)]
    if randomise:
        random.shuffle(markers)
        open(args.output+".txt","w").write(" ".join([str(x) for x in markers]))

    for p in range(0, page_count):
        if done:
            break
        if page_border:
            ctx.set_source_rgb(*border_colour)
            ctx.set_line_width(lw)
            ctx.rectangle(page_margin, page_margin,page[0]
                    -page_margin*2, page[1] - page_margin*2)
            ctx.set_line_width(lwdef) # default
            ctx.stroke()
        y = page_margin
        x = page_margin
        #lets hack this bit to do a bunch around the edges
        x = 3
        for y in range (6, 286 , 26):
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,marker_size, marker_size,
                x + border_size,y + border_size))
            bid = bid + 1
            id = markers[bid % len(markers)]
            bid = bid + 1

    ctx.show_page()
    surface.finish()


