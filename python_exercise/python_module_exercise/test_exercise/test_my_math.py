import my_math

def test_add():
	assert  my_math.add(1,2) == 3
	assert my_math.add(5,9) == 14

def test_minus():
	assert  my_math.minus(1,2) == -1
	assert my_math.minus(5,9) == -4