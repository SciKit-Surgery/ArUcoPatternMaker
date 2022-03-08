# coding=utf-8

"""ArUcoPatternMaker tests"""

import cairo
import arucopatternmaker.algorithms.algorithms as alg

# Pytest style

def test_int_to_base():
    """Test that in2base works for a few cases """
    assert alg.int2base(78, 4) == '1032'
    assert alg.int2base(149, 10) == '149'
    assert alg.int2base(-44, 16) == '-2c'

def test_draw_marker():
    """Tests for drawMarker"""

    surface = cairo.PDFSurface (None, 10, 10)
    context = cairo.Context(surface)
    _marker_string = alg.draw_marker(context, 0, 0.0, 0.0,
            0.0, 0.0 ,marker_colour = [0.0,0.0,0.0])
