def sub_x_y(x, y):
	return x - y

def testsub_x_y():
	assert sub_x_y(9, 3) == 6
	assert sub_x_y(9, 7)  == 2




def add_x_y(x, y):
	return x + y

def testadd_x_y():
	assert add_x_y(0, 3) == 3
	assert add_x_y(1, 7) == 8
	assert add_x_y(55, 60) == 115
	assert add_x_y(12, 12) == 24
