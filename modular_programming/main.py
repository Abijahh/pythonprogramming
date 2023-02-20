#import operators module
import operators
import others
import trig

#build a better calculator
x = others.cube(9)
y = operators.add(7,8)

print(y)

#get numbers
operator=input("Enter operator")
if operator=="cube":
    num=eval(input("Enter number:"))
else:
     num1 = eval(input("Enter number 1:"))
     num2 = eval(input("Enter number 2:" ))
    

    if operator == "+":
      x = operators.add(num1,num2)
      print(x)
    
 elif operator == "-":
        x = operators.subtract(num1,num2)
        print(x)
    
elif operator == "*" or "x" or "X":
        x = operators.multiply(num1,num2)
        print(x)
    
elif operator == "/":
        x = operators.divide(num1,num2)
        print(x)
    
elif operator == "sin":
    angle =eval(input("Enter angle in degrees:"))
    sin_of_angle = trig.get_sine(angle)
    print(sin_of_angle)
   
   
 elif operator == "tan":
     angle = eval(input("Enter angle in degrees:"))
     print(trig.get_tan(angle))
    
 elif operator == "cos":
     angle = eval(input("Enter angle in degrees:"))
     print(trig.get_cos(angle))
    
 else:
     num1 = eval(input("Enter number 1:"))
     num2 = eval(input("Enter number 2:" ))
    
    if operators == "+":
      x = operators.add(num1,num2)
      print (x)

    elif operators == "-":
        x = operators.subtract(num1,num2)
        print(x)
        
        