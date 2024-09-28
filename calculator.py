print('Hi, please choose one of the operation to start operating!')
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
def addition(x , y):
  return(x + y)
  
def subtraction(x , y):
  return(x - y)
def multiplication(x , y):
  return(x * y)
def division(x , y):
  return(x / y)
while True:
  choice = input("Enter the operation number (1/2/3/4)")
  if choice in ('1','2','3','4'):
    try:
      num1 = input(float("Enter first number")
      num2 = input(float("Enter second number")
    except ValueError:
      print("Invalid Input! Enter the number again")
      continue
    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtraction(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiplication(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", division(num1, num2))
    again = input("Do you want more caculation? (y/n)")
    if again == 'n':
      break
  else:
    print('Invalid Input!')
