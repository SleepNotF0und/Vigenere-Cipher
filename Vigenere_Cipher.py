while True:
    ch =int(input("Press 1 for Encrypt || Press 2 for Decrypt\n>>>"))
    if ch == 1:
        text = input("Text:").lower() #.replace(' ','_')
        print("!!! THE KEY MUST BE CHARACTERS !!!\n")
        key = input("Key:")

        if len(text) > len(key):
            key =key*100

        Vigenere=[]
        for tx,k in zip(text,key):
            if ord(tx) + ord(k) > ord('z') and tx != ' ':
                Vigenere.append(chr(ord(tx) + ord(k) - ord('z')))
            else:
                Vigenere.append(chr(ord(tx) + ord(k)))

        print("\n=======================================")
        print("           !!! Encrypted !!!             ")
        print("".join(Vigenere))
        print("\n=======================================\n")

    elif ch == 2:
        text = input("Text:")
        key = input("Key:")

        if len(text) > len(key):
            key = key*100

        Vigenere=[]
        for tx,k in zip(text,key):
            if ord(tx) - ord(k) < ord('z') and tx != ' ':
                Vigenere.append(chr(ord(tx) - ord(k) + ord('z')))
            else:
                Vigenere.append(chr(ord(tx) - ord(k)))

        print("\n=======================================")
        print("           !!! Decrypted !!!             ")
        print("".join(Vigenere))
        print("\n=======================================\n")
