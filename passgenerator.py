import string
from random import *
import sys

min_char = 8
max_char = int(sys.argv[1])

allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

print ("Your password is marked in red " + '\x1b[1;37;41m' + password + '\x1b[0m' + " and was generated with"  + '\x1b[1;32;40m', len(password), '\x1b[0m'+"characters of length.")
