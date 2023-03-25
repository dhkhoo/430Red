import random
import string

allLetters = string.ascii_letters + string.digits
size = 8

for i in range(50):
    ranUsername = ''.join(random.choices(allLetters, k=size))
    print(ranUsername)