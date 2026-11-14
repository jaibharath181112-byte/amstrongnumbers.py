print("===================================================")
print("first activity")
print("===================================================")
number=int(input("input your number:"))
digits=len(str(number))
resultnumber=0
temp=number
while temp>0:
    digit=temp%10
    resultnumber+=digit**digits
    temp//=10
if number==resultnumber:
        print(number,"is an amstrong number")
else:
        print(number,"is not an amstrng number")

print("===================================================")
print("second activity")
print("===================================================")
def print_factors(number):
       print("the factors of",number,"are:")
       for i in range("1,number+1"):
            if number%i==0:
                     print(i)
number=int(input("enter number to find its factor"))
print_factors(number)