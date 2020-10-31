''' Note that it is assumed that the input will be a file with .txt extension''' 
from spellcheckpy import SpellCheck

#if the file is in a separate directory input should be like this
#check = SpellCheck(r'C:\Users\ANWOY\Desktop\test.txt')
#Note: the 'r' before path is a must
check = SpellCheck('demo.txt')
#the other two parameters are optional, but can be specified explicitly, like
#check = SpellCheck('demo.txt', max_edit_dist=3, length_of_prefix=6)
check.replace()

