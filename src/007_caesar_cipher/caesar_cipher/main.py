def main():
    
    print(" Do you want to encrypt or decrypt your text ? ")

    try:
        select = int(input("Enter 1 for encrypt and 2 for decrypt : "))

        if select == 1:
            text=input("Enter your text: ")
            key =int(input("Enter your key(only number) :"))
            print("Your encrypted text : " , encrypt (text , key))

        elif select == 2:
            text=input("Enter your text: ")
            key =int(input("Enter your key(only number) :"))
            print("Your decrypted text : " , decrypt(text , key) )

        else:
            print("Plz enter a valid option")

    except ValueError:
        print("PLZ enter numbers only for the option and the key!!!")

if __name__ == '__main__':
    print(main())