terms=int(input('Enter the number of terms: '))
m, n= 0, 1
times=0
if terms<=0:
          print('')
elif terms==1:
    print("0")
else:
    while times<terms:
        print(m)
        z=m+n
        m=n
        n=z
        times+=1
