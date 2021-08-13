
def cal():
    print("1.ADDITION\t2.SUBTRACTION\t3.MULTIPLICATION\t4.DIVISION")
    opt=int(input("enter an option:"))

    if opt==1:
        num_1=float(input("enter the first number:"))
        num_2=float(input("enter the second number:"))
        print(num_1,"+",num_2,"=",num_1+num_2)

    elif opt==2:
        num_1=float(input("enter the first number:"))
        num_2=float(input("enter the second number:"))
        print(num_1,"-",num_2,"=",num_1-num_2)

    elif opt==3:
        num_1=float(input("enter the first number:"))
        num_2=float(input("enter the second number:"))
        print(num_1,"x",num_2,"=",num_1*num_2)

    elif opt==4:
        num_1=float(input("enter the first number:"))
        num_2=float(input("enter the second number:"))
        print(num_1,"/",num_2,"=",num_1/num_2)

    else:
        print("INVALID OPTION!!!")


cal()
