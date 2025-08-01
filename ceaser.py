import string

abc=string.ascii_letters
digit=string.digits
punc=" "+string.punctuation

pt=input("Enter a message: ")

while True:
  try:
    k=int(input("Enter a key: "))
    break
  except Exception:
    print("Enter an integer value")

ct=""
for i,c in enumerate(pt):
  if c.isdigit():
    j=digit.index(c)
    ct[i]=digit[j+k]
  elif c in punc:
    ct[i]=c
  elif c.isalpha():
    j=abc.index(c)
    ct[i]=abc[j+k]
  else:
    ct[i]=c

print("Ceaser Cipher")
print(f"Shifted by {k} keys")
print("Plain Text:",pt)
print("Cipher Text:",ct)
