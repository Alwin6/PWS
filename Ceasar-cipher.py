def encrypt(string, shift):
 
  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher

def decrypt(string, shift):
 
  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
  
  return cipher

while True:
    print("1 for encrypting, 2 for decrypting\n")
    choice = int(input("> "))
    if choice == 1:
        text = input("\nenter string: ")
        s = int(input("enter shift number: "))
        print("\noriginal string: ", text)
        print("after encryption: ", encrypt(text, s))
    elif choice == 2:
        text = input("\nenter string: ")
        s = int(input("enter shift number: "))
        print("\nencrypted string: ", text)
        print("after decryption: ", decrypt(text, s))
    else:
        print("Invalid choice!")