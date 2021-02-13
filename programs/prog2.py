#Program to print 5 times “jay Ganesh” on screen.

def PrintString(Str,iNo):
    i=1

    while i<=iNo:
        print("",Str)
        i=i+1

def main():
    print("Enter any string..")
    Strname=input()
    print("Enter how many time you want to print String")
    iValue=int(input())
    ret=PrintString(Strname,iValue)

if __name__ =="__main__":
    main()
