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
        
        elif choose.lower() == "s": # Evaluate Strength
            
            password_enterred = input("Please enter your password to be evaluated.")
        
        else: # Invalid Answer

            print("Invalid choice. Please restart the program.")    

    if __name__ == "__main__": 
        main()