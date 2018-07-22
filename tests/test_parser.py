import pytest
from escroll.util import parsed_args



def test_init():
    args = parsed_args(['-i', 'the_test'])
    assert args.init == 'the_test'

   
