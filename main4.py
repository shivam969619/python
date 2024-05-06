import time

timestamp= time.strftime('%H:%M%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
minute=int(time.strftime('%M'))
print(minute)
second=int(time.strftime('%S'))
print(second)
if(hour>12):
    print("Good after Noon")

elif(hour<12):
     print("Good Morning ")

elif(hour>20):
       print("Good night ")
