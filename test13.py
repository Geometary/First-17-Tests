from sys import argv

script, first, second, third = argv

age = raw_input ("How old are you?")
height = raw_input ("How tall are you?")
weight = raw_input ("How heavy are you?")

print "Then you are %r old, %r tall and %r heavy." % (
	age, height, weight)