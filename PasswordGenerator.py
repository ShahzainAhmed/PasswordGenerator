# Importing modules.
import string

from random import *

# Initializing a variable. 
characters = string.ascii_letters + string.punctuation + string.digits

# Initializing a second variable. 
password = "".join(choice(characters) for x in range(randint(8, 16)))

# Using print statement to generate the random password
print(password)

# Congratulations! This will generate a random number now. 
