
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return(n1-n2)

def mul(n1,n2):
    return(n1*n2)

def div(n1,n2):
  return(n1/n2)

while True:
  n1=float(input("Enter First number \n"))
  n2=float(input("Enter Second number \n"))
  print("Select the operation to be performed:\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n")
  
  Operation=input("Enter choice (1/2/3/4) \n")

  if Operation  in('1','2','3','4'):
    try:
      if Operation == "1":
        print(n1,"+",n2,"=",add(n1,n2))

      elif Operation =="2":
        print(n1,"-",n2,"=",sub(n1,n2))

      elif Operation == "3":
        print(n1,"*",n2,"=",mul(n1,n2))

      elif Operation == "4":
        print(n1,"/",n2,"=",div(n1,n2))

    except ZeroDivisionError:
      print("Cannot divide by zero")

  else:
    print("Invalid Option")

  next_calc = input("Continue next calculation? (y/n/yes/no/Yes/No):\n")

  if next_calc.lower() in ("n", "no"):
    break