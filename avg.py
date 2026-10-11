numbers=[]
for i in range(5):
    num=int(input("Enter a int number"))
    numbers.append(num)

for i in range(5):
    print(numbers[i])

print("Max number in the list is: ",max(numbers))
average=sum(numbers)/len(numbers)
print ("average is :",average)