import pytest
import sys
sys.path.append("../pyCL")
import one

#should fail
def test_answer():
    assert one.func() == False

#should pass
def test_2():
    assert one.func() == True
