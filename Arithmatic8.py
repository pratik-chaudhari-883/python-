import marvellus
def main():
    no1=int(input("Enter first no.."))

    no2=int(input("Enter second Number..."))

    Ans=marvellus.Addition(no1,no2)  #function call

    print("Addition of two number is",Ans)
if __name__=="__main__":
    main()
