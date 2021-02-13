#1function accept nothing and return nothing
def fun():
    print("function fun")
#2function gun  accept  parameter nothing and return nothing
def gun(no):
    print("function gun inside gun",no)
#3function sun  accept  parameter nothing and return one parameter 
def sun(no):
    print("sun function return ",no)
    return no+1
#4 function accept multiple values and return multiple values
def AddSub(no1,no2):
    add=no1+no2
    sub=no1-no2
    return add,sub
#5 nested function defination not allowed  in c c++ and java but allowed in python 
def marvellus():
    print("inside marvellus")
    def Infosystems():
        print("inside infosystems")
    Infosystems()
def main():
    fun()
    gun(11)
    ret=sun(10)
    ret1,ret2=AddSub(12,13)
    print("Addition is :",ret1)
    print("Substraction  is :",ret2)
    
    print("function sun with parameter :",ret)
    marvellus()

if __name__=="__main__":
    main()
