import time
N1 = int(input("digite um número par:"))
if (N1 >= 0):
 if (N1%2) == 0:
    print('""P-A-R""')

 else:
    print("tente outra vez!!!")
else:
 print("tente outra vez!!!")
time.sleep(3)
