#Accept one number from user and print that number of * on screen.
def PrintStar(iNo):
    while iNo!=0:
        print("*")
        iNo=iNo-1
        
def main():
    print("Enter any Number...")
    iValue=int(input())

    PrintStar(iValue)

if __name__=="__main__":
    main()