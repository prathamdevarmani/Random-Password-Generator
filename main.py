import random as r
import string as str

def Password(lenght, use_text=True, use_number=True, use_special_character=True):
    character =""
    if use_text:
        character +=str.ascii_letters
    if use_number:
        character +=str.digits
    if use_special_character:
        character +=str.punctuation
    
    if not character:
        print("error:Please select atleast one character type.")
        return
    
    pwd =''.join(r.choice(character) for _ in range(lenght))
    return pwd
    
def main():
    print("\n\n\t\t\t\t\tPassword Generator")
    
    try:
        lenght = int(input("Enter your password lenght: "))
        use_text = input("Do you want to include letter in your password? (Y/N): ").lower() == 'y'
        use_number =input("Do you want to include number in your password? (Y/N): ").lower() =='y'
        use_special_character =input("Do you want to include Special character in your password? (Y/N): ").lower() =='y'

        pwd = Password(lenght, use_text, use_number, use_special_character)

        if pwd:
            print("\n\nYour Generated Password:", pwd)
        else:
            print("Password generation failed.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for password length.")
if __name__ == "__main__":
    main()       
