import pytest
import os
from escroll.util import init

def test_scroll_exists():
    #if it does
    test_scroll = open('thetest.scroll', 'w+')
    lines = ["~{}~\n", "&{}&\n", "?{}?\n"]
    test_scroll.writelines(lines)
    test_scroll.close()

    assert init('realscroll') == False
    os.remove('thetest.scroll')

def test_scroll_dne():

    assert init('realscroll') == True
    os.remove('realscroll.scroll')
