import random
import string

class PasswordGenerator:

    def generate_password():
        pass

    def analyze_password():
        pass

    def main():

        choose = input("If you would like to generate a password, please type G.\n If you would like to analyze the strength of a password, please type S.")
        
        if choose.lower() == "g": # Generate
            # Request length of password
            length = input("Please enter the desired length of your password.")

            try:
                length = int(length)
            except ValueError:
                print("Non-Integer value detected. Please restart the program.") 

            character_set = string.ascii_lowercase # default character set to choose from

            # request uppercase, special characters, numbers and add to character list
            uppercase_bool = (input("Include uppercase characters? Y/N")).lower()

            if uppercase_bool == "y":
                character_set += string.ascii_uppercase
            
            number_bool = (input("Include numbers? Y/N")).lower()

            if number_bool == "y":
                character_set += string.digits

            symbols_bool = (input("Include special characters? Y/N")).lower()

            if symbols_bool == "y":
                character_set += string.punctuation
                
            character_pool = ''
            
            for _ in range(length):
                character_pool = character_pool.join(random.choice(character_set))

        elif choose.lower() == "s": # Evaluate Strength
            password_enterred = input("Please enter your password to be evaluated.")
        else: # Invalid Answer
            print("Invalid choice. Please restart the program.")    

    if __name__ == "__main__": 
        main()