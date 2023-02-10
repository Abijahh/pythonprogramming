# my first python list
numbers=[45,67,34,76,23,45]

print(len(numbers))#get the length of my list
print(sum(numbers))
for i in range(len(numbers)):
    print(numbers[i])
    
    
    
  
    
#count
print(numbers.count(67))
print(numbers.pop(2))

#INSERT
numbers.insert(2,100)
for i in range(len(numbers)):
    print(numbers[i])
    
    #REMOVE
numbers.remove(67) 

#SORT -arranges the list in order
numbers.sort()
#add a new line for formatted output
print("\n") 

for i in range(len(numbers)):
    print(numbers[i])
    
#creating lists
even_nums =[]
   
for i in range (len(nums)):
    print(nums[i]) 
    
nums=[]
for num in range(20):
    if(num % 2==0):
        even_nums.append(num)
for i in range(len(even_nums)):
    print(even_nums[i])        
    
    