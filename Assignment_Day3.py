#Assignment 1
print("welcome to the Controlroom of Hyderabad ATC")
Altitude = 1500
if Altitude <= 1000:
  print('youre safe to land')
elif Altitude <=5000:
  print('Please Bring Down Altitude to 1000')
else :
  print('it is Danger now to land, please Turn around')

#Assignment2
for num in range(0,200):
  if num > 1:
    for i in range(2,num):
      if (num % i)== 0:
        break
    else :
      print(num)  