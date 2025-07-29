import random
import string
import sys

ch= " " + string.punctuation + string.digits + string.ascii_letters
ch=list(ch)
lst=ch.copy()
random.shuffle(lst)

while True:
    print("1.Encryption\n2.Decryption\n3.Exit")
    n=int(input("Enter your choice: "))
    ct=""
    if n==1:
        pt=input("Enter a message: ")
        print("Original text:",pt)
        for x in pt:
            i=ch.index(x)
            ct+=lst[i]
        print("Encrypted text:",ct)
    elif n==2:
        pt=input("Enter text to Decrypt: ")
        print("Encrypted text:",pt)
        for x in pt:
            i=lst.index(x)
            ct+=ch[i]
        print("Decrypted text:",ct)
    elif n==3:
        sys.exit("Thankyou!!! Have a nice day!!!")
    else:
        print("Invalid choice")
