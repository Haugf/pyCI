
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(file))))
# import ../db.py
import one

#should fail
def test_answer():
    assert func() == False

#should pass
def test_2():
    assert func() == True
