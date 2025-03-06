import random
import string

class PasswordGenerator:

    def generate_password(length, uppercase = True, numbers = True, symbols = True):
        
            character_set = string.ascii_lowercase # default character set to choose from

            if uppercase:
                character_set += string.ascii_uppercase

            if numbers:
                character_set += string.digits

            if symbols:
                character_set += string.punctuation
                
            password = ''
            
            for i in range(length): # append specified number of characters to password
                password += random.choice(character_set)

            return password

    def analyze_password():
        pass