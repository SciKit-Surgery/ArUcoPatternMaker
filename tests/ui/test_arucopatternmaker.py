# coding=utf-8

"""Command line processing"""

from arucopatternmaker.ui.arucopatternmaker_demo import run_demo


def test_arucopatternmaker():
    """Test that main function runs"""

    run_demo('A4', False, False, 15,
            20, 1, 2, 3,
            5, 'test_output.pdf', 360, 410, 0,
            False, False, False)
