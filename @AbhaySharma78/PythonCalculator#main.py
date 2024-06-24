A = int(input("Enter the First Number"))
B = int(input("Enter the another Number"))
C = input("Enter the operator +,-,*,/,**")
if (C=="+"):
  print("The value of A and B is", A+B)
elif (C=="-"):
  print("The value of A and B is", A-B)
elif (C=="*"):
  print("The value of A and B is",A*B)
elif (C=="/"):
  print("The value of A and B is",A/B)
elif (C=="**"):
  print("The value of A and B is",A^B)
else:
  print("Enter the Valid Operator")
