class cal:
  def add(self):
    value1=int(input("Enter 1st value: "))
    value2=int(input("Enter 2nd value: "))
    print(value1+value2)
  
  def sub(self):
    value1=int(input("Enter 1st value: "))
    value2=int(input("Enter 2nd value: "))
    print(value1-value2)
  
  def mul(self):
    value1=int(input("Enter 1st value: "))
    value2=int(input("Enter 2nd value: "))
    print(value1*value2)
  
  def divide(self):
    value1=int(input("Enter 1st value: "))
    value2=int(input("Enter 2nd value: "))
    try:
      print(value1/value2)
    except ZeroDivisionError:
      print("cannot divide by zero")
c=cal()
while True:
  print("enter 1=add, 2=subtract, 3=multiply, 4=divide")
  choice=int(input("Enter your choice: "))
  if choice==1:
    c.add()
  elif choice==2:
    c.sub()
  elif choice==3:
    c.mul()
  elif choice==4:
    c.divide()
  else:
    print("Invalid choice")
  print("Do you want to continue?(y/n): ")
  question=input("enter your decision:")
  if question.lower()=='no':
    break
