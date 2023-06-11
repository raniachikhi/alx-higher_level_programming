#!/usr/bin/python3
def print_list_integer(my_list=[]):
	"""takes a list of int & prints them on separate line."""
	for i in range(len(my_list)):
		print("{:d}".format(my_list[i]))
