import time
def search():
    f1=open(fname,encoding="utf8", errors='ignore')
    word=input("enter the word to be searched:\n")
    s=""
    count=1
    s=f1.readline()
    l=s.split()
    print(l)
    while(s):
        s=f1.readline()
        l=s.split()
        if word in l:
            print("line number:",count,":",s)
        count+=1

def FINDANDreplace():
       f1=open(fname,encoding="utf8", errors='ignore')
       data=f1.read()
       f2=input("enter the word:\n")
       f3=input("enter the word to be replaced\n")
       replaced_value=data.replace(f2,f3)
       f1=open(fname,"wt")
       f1.write(replaced_value)
       print(f2 +"  is replaced by "+f3 +"  in file succesfully")
       f1.close()
 
def displayspec(wlines):
     f1=open(fname,encoding="utf8", errors='ignore')
     count=1
     data=f1.readlines()
     for line in data:
         if count in wlines:
             print(line)
         else:
            pass
         count+=1

def display():
     f1=open(fname,encoding="utf8", errors='ignore')
     data=f1.readlines()
     for line in data:
         print(line)

def insert():
    f1=open(fname,"a")
    txt=str(input("enter the line to add\n"));
    f1.write(txt+"\n")

print("welcome to document processing\n")
print("choose any of below options\n")
fname=str(input( "enter the file name\n"))
t1=t2=0
print( " 1 -> insert \n 2 -> display \n 3 -> search \n 4 -> replace \n 5 -> quit")
ch=int(input())
while(ch!=6):
    if(ch==1):
        t1=time.time()    
        insert()
        t2=time.time()
        print("time="+str(t2-t1)+"sec")
        continue
    if(ch==2):
        print("press 1 to display full txtfile\n")
        print("press 2 to display selective lines\n")
        choice=int(input())
        if(choice==1):
            t1=time.time()
            display()
            t2=time.time()
            print("time="+str(t2-t1)+"sec")
            break
        if(choice==2):
            r=input("enter begining  and ending line u wish to see seoerate by comma and press enter key\n")
            inp=r.split(',')
            wlines=[]
            for i in range(int(inp[0]),int(inp[1])):
                wlines.append(i)
            t1=time.time()
            displayspec(wlines)
            t2=time.time()
            print("time="+str(t2-t1)+"sec")
            break
        else:
            print ("invalid choice\n")
            break
           
        continue
    if(ch==3):
        t1=time.time()
        search()
        t2=time.time()
        print("time="+str(t2-t1)+"sec")
        continue
    if(ch==4):
        t1=time.time()
        FINDANDreplace()
        t2=time.time()
        print("time="+str(t2-t1)+"sec")
        continue
print("program done\n")

        




   




