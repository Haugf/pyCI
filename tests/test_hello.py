import pytest
import sys
sys.path.append("/Users/brettbissey/pyCI/")
from one import func

#should fail
def test_answer():
    assert func() == False

#should pass
def test_2():
    assert func() == True
