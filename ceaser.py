#This is a ceaser cipher with a twist. I made it such that it also shifts the numbers and puntuations which is not present in the original Ceaser Cipher logic.

import string

abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digit=list(string.digits)
punc=" "+string.punctuation
punc=list(punc)

pt=input("Enter a message: ")

while True:
  try:
    k=int(input("Enter a key: "))
    break
  except Exception:
    print("Enter an integer value")

ct=""
for i,c in enumerate(pt):
  if c in digit:
    j=digit.index(c)
    ind=(j+k)%10
    ct+=digit[ind]
  elif c in punc:
    j=punc.index(c)
    ind=(j+k)%33
    ct+=punc[ind]
  elif c in abc:
    j=abc.index(c)
    ind=(j+k)%26
    ct+=abc[ind]
  elif c in Abc:
    j=Abc.index(c)
    ind=(j+k)%26
    ct+=Abc[ind]
  else:
    ct+=c

print("\nCeaser Cipher")
print(f"Shifted by {k} keys")
print("Plain Text:",pt)
print("Cipher Text:",ct)
