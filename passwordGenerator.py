# Random Password Generator 

import random 
from string import punctuation 

# create list with special characters 
special_chars = list(punctuation)

# there are 32 elements in the list 
print(len(special_chars))

# with special characters
password = ""
for i in range(5):
    # produces random uppercase character/letter 
    a = chr(random.randint(65, 90))
    # produce random lowercase character/letter 
    b = chr(random.randint(65, 90)).lower()
    # produce special character 
    c = special_chars[random.randint(0, 31)]
    
    password = password + a + b + c 

print(password)
    
# shuffle password, won't follow upper case 
# lower case, special character structure 
print(''.join(random.sample(password, len(password))))

    
    
