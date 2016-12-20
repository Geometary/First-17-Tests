#Ask user to input argument variable and import it from system
from sys import argv

#Name argument variable
script, filename = argv

#Define parameter txt
txt = open(filename)

#Display the sentence and use the 'filename' variable as a part.
print "Here's your file %r:" % filename
#Use the parameter txt and open the file.
print txt.read()
print txt.close()



#Display this demand.
print "Type the filename again:"
#Define parameter file_again.
file_again = raw_input("> ")

#Define parameter txt_again.
txt_again = open(file_again)

#Open the file again.
print txt_again.read()
print txt_again.close()