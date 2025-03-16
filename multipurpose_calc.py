import math
print("Welcome to multi purpose calculator")
print("Various operations available: ")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulo \n6. Power \n7. Square Root \n8. Area & Circumference of Circle \n9. Perimeter of Rectangle \n10.Area of Triangle \n11.Simple Interest Calculation \n12.Compound interest Calculation \n13.Fahrenheit to Celsius \n14.Celsius to Fahrenheit \n15.Largest of 3 numbers \n16.Factorial \n17.Greatest Common Divisor \n18.Least Common Multiple \n19.BMI calculation \n20.Average")
op=int(input("Enter the operation to perform: "))
if op==1:
	a=float(input("Enter first number: "))
	b=float(input("Enter second number: "))
	c=a+b
	print("The sum is: ",c)
elif op==2:
	a=float(input("Enter first number: "))
	b=float(input("Enter second number: "))
	c=a-b
	print("The difference is: ",c)
elif op==3:
	a=float(input("Enter first number: "))
	b=float(input("Enter second number: "))
	c=a*b
	print("The product is: ",c)
elif op==4:
	a=float(input("Enter first number: "))
	b = float(input("Enter second number: "))
	if b==0:
	    print("INVALID!!! DIVIDE-BY-ZERO ERROR.")
	else:
	    c=a/b
	    print("The quotient is: ",c)
elif op==5:
	a=int(input("Enter first number: "))
	b=int(input("Enter second number: "))
	c=a%b
	print("The remainder is: ",c)
elif op==6:
	a=float(input("Enter a number: "))
	b=int(input("Enter the power: "))
	c=pow(a,b)
	print(f"{a} to the power of {b} is: {c}")
elif op==7:
    a=float(input("Enter a number: "))
    if a < 0:
        print("INVALID!!! Negative numbers not allowed.")
    else:
        print("The squareroot of",a,"is",math.sqrt(a))
elif op==8:
    r=float(input("Enter the radius: "))
    a=math.pi*r*r
    c=math.pi*2*r
    print(f"Area: {a:.2f}")
    print(f"Circumference: {c:.2f}")
elif op==9:
    l=float(input("Enter the length: "))
    w=float(input("Enter the width: "))
    p=2*l+2*w
    print(f"Perimeter: {p:.2f}")
elif op==10:
    h=float(input("Enter the height: "))
    b=float(input("Enter the base: "))
    a=h*b/2
    print(f"Area: {a:.2f}")
elif op==11:
    p=float(input("Enter the initial principal balance: "))
    r=float(input("Enter the annual interest rate: "))
    t=int(input("Enter time (in years): "))
    a = p*(1 + (r/100)*t)
    print(f"Simple Interest: {a:.2f}")
elif op==12:
    p=float(input("Enter the initial principal balance: "))
    r=float(input("Enter the annual interest rate: "))
    n=int(input("Enter the no.of.times interest applied per time period: "))
    t=int(input("Enter time (in years): "))
    a=p*pow(1+((r/100)/n),n*t)
    print(f"Compound Interest: {a:.2f}")
elif op==13:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"Temperature in Celsius: {c:.2f}°C")
elif op==14:
    c= float(input("Enter temperature in Celsius: "))
    f=(c*9/5) + 32
    print(f"Temperature in Fahrenheit: {f:.2f}°F")
elif op==15:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print(f"The largest number is: {largest}")
elif op==16:
    num = int(input("Enter a number: "))
    if num < 0:
        print("INVALID!!! Negative numbers not allowed.")
    else:
        print("Factorial:", math.factorial(num))
elif op==17:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD:", math.gcd(a, b))
elif op==18:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("LCM:", abs(a * b) // math.gcd(a, b))
elif op==19:
    w = float(input("Enter weight (kg): "))
    h = float(input("Enter height (m): "))
    bmi = w / (h ** 2)
    print(f"BMI: {bmi:.2f}")
elif op==20:
    n = int(input("Enter the number of values: "))
    tot = 0
    for i in range(n):
        num = float(input(f"Enter number {i+1}: "))
        tot += num
    avg = tot / n
    print(f"The average of the {n} numbers is: {avg:.2f}")
else:
    print("You have entered invalid operator!!!")
