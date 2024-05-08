def decrypt(word):
  if word == '':
    return '<no-input>'

  first_letterd = chr(ord(word[0]) - 2)
  last_letterd = chr(ord(word[-1]) - 2)
  middled = word[-2:0:-1]  # this takes the middle out of the word and reverses it
  return f'{first_letterd}{middled}{last_letterd}'

def encrypt(word):
  if word == '':
    return '<no-input>'

  first_letter = chr(ord(word[0]) + 2)
  last_letter = chr(ord(word[-1]) + 2)
  middle = word[-2:0:-1]  # this takes the middle out of the word and reverses it
  return f'{first_letter}{middle}{last_letter}'

def main():
    end = "no"
    while end != "yes":
        choice = input("What would you like to do? (encrypt/decrypt): ").lower()
        if choice == "decrypt":
            message = input("What is your message: ")
            decrypted = decrypt(message)
            print(decrypted)
        elif choice == "encrypt":
            message = input("What is your message: ")
            encrypted = encrypt(message)
            print(encrypted)
        else:
            print("Invalid action!")
        end = input("Do you wish to end? ").lower()
main()
