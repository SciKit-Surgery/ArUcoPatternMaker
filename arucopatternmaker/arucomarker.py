#! /usr/bin/python3.7

import cairo,argparse,random

from algorithms.algorithms import draw_marker

#TEST: https://jcmellado.github.io/js-aruco/getusermedia/getusermedia.html
#http://terpconnect.umd.edu/~jwelsh12/enes100/markergen.html
#http://terpconnect.umd.edu/~jwelsh12/enes100/markers.js

if __name__ == '__main__':
    import argparse

    pages = dict(A4=(210,297),A3=(297,420))

    parser = argparse.ArgumentParser(description='Aruco Page Maker to PDF, Emanuele Ruffaldi 2015')
    parser.add_argument('--page', default="A4", help='page size: A4 or A3')
    parser.add_argument('--pages',default=1,type=int,help="number of pages")
    parser.add_argument('--landscape', dest='landscape', action='store_const',const=True,default=False,help="set landscape")
    parser.add_argument('--portrait', dest='landscape', action='store_const',const=False,default=False,help="set landscape")
    parser.add_argument('--markersize', type=float,default=20,help="marker size (mm)")
    parser.add_argument('--bordersize', type=float, default=1,help="border around marker (mm)")
    parser.add_argument('--spacing', type=float,default=2,help="marker spacing in vertical and horizontal (mm)")
    parser.add_argument('--pagemargin', type=float,default=15,help="spacing default around (mm)")
    parser.add_argument('--fill', action="store_true",help="fills the page")
    parser.add_argument('--rows', type=int,default=5,help="fill rows")
    parser.add_argument('--cols', type=int,default=3,help="fill cols")
    parser.add_argument('--first', type=int,default=360,help="first id")
    parser.add_argument('--last', type=int,default=410,help="last id")
    parser.add_argument('--repeat', type=bool,default=False,help="repeat mode (ends at last)")
    parser.add_argument('--count', type=int,default=0,help="count (alternative to last)")
    parser.add_argument('--border', action='store_true',help="draws black border around")
    parser.add_argument('--pageborder', action='store_true',help="draws black border around")
    parser.add_argument('--axis', action='store_true',help="highlights axis")
    parser.add_argument('--random', action='store_true',help="randomize markers for board (and produces the randomization)")
    parser.add_argument('--output',default="output.pdf",help="outputfilename")


    args = parser.parse_args()

    page = pages[args.page]
    if args.landscape:
        page = (page[1],page[0])
    if args.count != 0:
        args.last = args.first + args.count - 1
    else:
        args.count = args.last - args.first + 1

    mm2pts = 2.83464567
    lw = 0.5 # mm
    lwdef = 0.5
    bordercolor = (0.0,0.0,0.0)
    if args.fill:
        args.cols = (page[0]-args.pagemargin*2)/(args.markersize+args.bordersize*2+args.spacing)
        args.rows = (page[1]-args.pagemargin*2)/(args.markersize+args.bordersize*2+args.spacing)
        print ("fill results in rows x cols",args.rows,args.cols)

    bid = 0

    width_pts, height_pts = page[0]*mm2pts,page[1]*mm2pts
    print ( page[0] , page [1] )
    surface = cairo.PDFSurface (args.output, width_pts, height_pts)
    ctx = cairo.Context (surface)
    #ctx.set_antialias(True)
    #ctx.set_line_width(50)
    #ctx.set_line_join(True)
    ctx.scale(mm2pts,mm2pts)
    done = False

    n = args.pages*args.rows*args.cols
    if args.count < n:
        n = args.count    
    n=100
    markers = [args.first+i for i in range(0,n)]
    if args.random:
        random.shuffle(markers)
        open(args.output+".txt","w").write(" ".join([str(x) for x in markers]))

    for p in range(0,args.pages):
        if done:
            break
        if args.pageborder:
            ctx.set_source_rgb(*bordercolor)
            ctx.set_line_width(lw)
            ctx.rectangle(args.pagemargin,args.pagemargin,page[0]-args.pagemargin*2,page[1]-args.pagemargin*2)
            ctx.set_line_width(lwdef) # default
            ctx.stroke()
        y = args.pagemargin
        x = args.pagemargin 
        #lets hack this bit to do a bunch around the edges
        x = 3
        for y in range (6, 286 , 26):
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,x + args.bordersize,y + args.bordersize))
            bid = bid + 1
            id = markers[bid % len(markers)]
            bid = bid + 1

        ctx.show_page()
        surface.finish()
        exit()
        for y in range (292, 190 , -32):
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,
                    x + args.bordersize,y - args.bordersize - args.markersize))
            bid = bid + 1
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,
                    210 - x + args.bordersize - args.markersize,y - args.bordersize - args.markersize))
            bid = bid + 1
        
        x = 5 + args.markersize + args.bordersize 
        for y in range (6, 20 , 32):
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,x + args.bordersize,y + args.bordersize))
            bid = bid + 1
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,210 - x + args.bordersize - args.markersize,y + args.bordersize))
            bid = bid + 1

        for y in range (292, 270 , -32):
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,
                    x + args.bordersize,y - args.bordersize - args.markersize))
            bid = bid + 1
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,
                    210 - x + args.bordersize - args.markersize,y - args.bordersize - args.markersize))
            bid = bid + 1
        
        x = 5 + 2 * (args.markersize + args.bordersize )
        for y in range (6, 20 , 32):
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,x + args.bordersize,y + args.bordersize))
            bid = bid + 1
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,210 - x + args.bordersize - args.markersize,y + args.bordersize))
            bid = bid + 1

        for y in range (292, 270 , -32):
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,
                    x + args.bordersize,y - args.bordersize - args.markersize))
            bid = bid + 1
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,
                    210 - x + args.bordersize - args.markersize,y - args.bordersize - args.markersize))
            bid = bid + 1
    
        """ x = 5 + 3 * (args.markersize + args.bordersize )
        for y in range (6, 20 , 22):
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,x + args.bordersize,y + args.bordersize))
            bid = bid + 1
            id = markers[bid % len(markers)]
            print(draw_marker(ctx,id,args.markersize,args.markersize,210 - x + args.bordersize - args.markersize,y + args.bordersize))
            bid = bid + 1
        """
        for y in range (292, 270 , -22):
            id = markers[bid % len(markers)]
            draw_marker(ctx,id,args.markersize,args.markersize,
                    x + args.bordersize,y - args.bordersize - args.markersize)
            bid = bid + 1
            id = markers[bid % len(markers)]
            draw_marker(ctx,id,args.markersize,args.markersize,
                    210 - x + args.bordersize - args.markersize,y - args.bordersize - args.markersize)
            bid = bid + 1





