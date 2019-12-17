
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# import ../db.py
import one

#should fail
def test_answer():
    assert one.func() == False

#should pass
def test_2():
    assert one.func() == True
