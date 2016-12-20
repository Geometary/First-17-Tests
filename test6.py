#! = Put a character string into another character string
#Define parameter x !
x = "There is %d types of people." % 10
#Define parameter binary
binary = "binary"
#Define parameter do_not
do_not = "don't"
#Define parameter y and use parameters binary and do_not as a part of y ! !
y = "Those who know %s and those who %s." % (binary, do_not)
#This is the first part of parameter list.

#Display parameter x
print x
#Display parameter y
print y

#Display parameter x as a part of a sentence, which means you must use format mark. !
print "I said %r." % x
#Display parameter y as a part of a sentence, which means you must use format mark.  !
print "I also said %s." % y

#Define parameter hilarious
hilarious = True
#Define parameter joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

#Display parameters joke_evaluation and hilarious !
print joke_evaluation % hilarious

#Define parameter w
w = "This is the left side of..."
#Define parameter e
e = "a goetz with an English book."

#Display the combination of parameters w and e
print w + e