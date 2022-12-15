x=""
while x!="exit":
    while True:
        x=input("what opperation would you like to do? ")
        if x!="add"and x!="sub"and x!="div"and x!="mul" and x!="exit":
            print("dumbass")
        else x=="add"and x=="sub"and x=="div"and x=="mul" and x=="exit":
            y=input("first number ")

            a=input("second number ")

            if x=="add":
                result=int(y)+int(a)
                print((y)+"+"+(a)+"="+str(result))
            elif x=="sub":
                result=int(y)-int(a)
                print(y+"-"+a+"="+str(result))
            elif x=="mul":
                result=int(y)*int(a)
                print(y+"*"+a+"="+str(result))
            elif x=="div":
                result=int(y)/int(a)
                print(y+"/"+a+"="+str(result)) 

print("thank you!")

    
