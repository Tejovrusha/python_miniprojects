import time
mytime=int(input("Enter time in seconds: "))
for x in range(mytime,0,-1):
    sec=x%60
    min=int(x/60)%60
    hrs=int(x/3600)
    print(f"{hrs:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("TIME'S UP!!!")
