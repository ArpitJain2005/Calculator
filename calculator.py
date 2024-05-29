def calculator(n1,op,n2):
   
    if op =="+":
        return "sum is\n",n1+n2
    elif op =="-":
        return "difference is\n ",n1-n2
    elif op =="/":
        return "quetient is\n",n1/n2
    elif op =="*":
        return "product is\n",n1*n2
    elif op =="%":
        return "remainder is \n",n1%n2
    else:
        return "not defined\n"
    

num1 = float(input("enter the first no."))
operator = input("enter the operator")
num2 = float(input("enter the second no."))

print(calculator(num1,operator,num2))
