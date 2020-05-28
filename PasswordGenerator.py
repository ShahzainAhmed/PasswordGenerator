# Importing String module.
import string

from random import *

# Initializing a variable. 
characters = string.ascii_letters + string.punctuation + string.digits

# Initializing a second variable. 
password = "".join(choice(characters) for x in range(randint(8, 16)))

print(password)
