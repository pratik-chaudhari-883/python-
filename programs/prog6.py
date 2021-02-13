# Accept on number from user if number is less than 10 then print 
#“Hello” otherwise print “Demo”.

def Display(iNo):
    if iNo<10:
        print("HELLO")
    else:
        print("DEMO")


def main():
    print("Enter Any Number..")
    iValue=int(input())

    Display(iValue)

if __name__=="__main__":
    main()