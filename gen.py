import random
import string

wykorzystane_znaki = string.ascii_letters + string.digits + string.punctuation

Twoje_Haslo = "".join(random.sample(wykorzystane_znaki, 8))

print(Twoje_Haslo)