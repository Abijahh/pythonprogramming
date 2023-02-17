numbers=[10,20,50,6]
numbers[2]=9
print(numbers)
cars=["BMW","Porsche","Jeep"]
cars.append("Toyota")
print(cars)
cars.remove("BMW")
print(cars)

numbers=[9,11,15,16]
numbers.pop(2)
print(numbers)

numbers=[3,5,6,77,8,8,45,8]
length=len(numbers)
print(length)
print(len("cars"))

numbers=[3,5,6,77,8,8,45,8]
length=numbers.count(8)
print(length)
numbers.reverse()
print(numbers)
for i in numbers:
    print(i)
    
for i in range(3):
    print(numbers[i])
    
