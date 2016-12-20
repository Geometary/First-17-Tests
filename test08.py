# -*- coding: utf-8 -*-
formatter = "%r %r %r %s"
# %s is used to display that Chinese character and so does the code in line 1. 

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "哟")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I love English.",
	"Because English is good for me.",
	"So let's start learning English together.",
	"Because English is good for you."
)