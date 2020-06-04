import time
import json
def search(word):
    f1=open(fname,encoding="utf8", errors='ignore')
    s=""
    count=0
    s=f1.readline()
    l=s.split()
    print(l)
    while(s):
        s=f1.readline()
        l=s.split()
        if word in l:
            print("line number:",count,":",s)
        count+=1

def delete(lineno):
    print(lineno)
    f=open(fname,'r+')
    d = f.readlines()
    f.seek(0)
    for i in d:
         if i != lineno:
               f.write(i)
    f.truncate()

def FINDANDreplace():
       f1=open(fname,encoding="utf8", errors='ignore')
       s=f1.read()
       f2=input("enter the word:\n")
       search(f2)
       f3=input("enter the word to be replaced\n")
       replaced_value=s.replace(f2,f3)
       f1=open(fname,"wt")
       f1.write(replaced_value)
       print(f2 +"  is replaced by "+f3 +"  in file succesfully\n")
       word=f3
       f1.close()

       f1=open(fname,encoding="utf8", errors='ignore')
       count=0
       print("the word to be replaced lie in:\n")
       s=f1.readline()
       l=s.split()
       print(l)
       while(s):
            s=f1.readline()
            l=s.split()
            if word in l:
                print("line number:",count,":",s)
            count+=1
 
def displayspec(wlines):
     f1=open(fname,encoding="utf8", errors='ignore')
     count=0
     data=f1.readlines()
     for line in data:
         if count in wlines:
             print("lineno: "+ str(count) +" -> " +line)
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

def delete():
    f1=open(fname,encoding="utf8", errors='ignore')
    data=f1.readlines()
    word=input("enter the word or sentance to search and delete")
    search(word)
    deline=int(input("enter the line no to delete"))
    
    del data[deline]
    f1=open(fname,"wt")
    str1 = ''.join(data)
    f1.write(str1)

def lineIndex(fName):
    d = {}
    with open(fName, 'r') as f:       
        content = f.readlines()
        lnc = 0
        result = {}
        for line in content:
            line = line.rstrip()
            words = line.split(" ")
            for word in words:
                tmp = result.get(word)
                if tmp is None:
                    result[word] = []
                if lnc not in result[word]:
                    result[word].append(lnc)

            lnc = lnc + 1
        with open('result.json','w+') as fp:
            json.dump(result,fp,indent=2)
        return result

def searcindex():
    fp=open('result.json','r')
    data=json.load(fp)
    string=str(input("enter the word "))
    a=data[string]
    #print(a)
    #print(type(a))
    displayspec(a)

def viewindex():
    with open('result.json','w+') as fp:
         result=lineIndex(fname)
         print(json.dumps(result, indent=2, sort_keys=True))


print("welcome to document processing\n")
print("choose any of below options\n")
fname=str(input( "enter the file name\n"))
t1=t2=0
print( " 1 -> insert \n 2 -> display \n 3 -> search \n 4 -> replace \n 5 -> delete \n 6 ->  Build Index \n 7 -> search using index \n 8 -> view index \n 9 -> quit")
ch=int(input())
while(ch!=9):
    if(ch==1):
        t1=time.time()    
        insert()
        t2=time.time()
        lineIndex(fname)
       # print("time="+str(t2-t1)+"sec")
        break
    if(ch==2):
        print("press 1 to display full txtfile\n")
        print("press 2 to display selective lines\n")
        choice=int(input())
        if(choice==1):
            t1=time.time()
            display()
            t2=time.time()
            #print("time="+str(t2-t1)+"sec")
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
            #print("time="+str(t2-t1)+"sec")
            break
        else:
            print ("invalid choice\n")
            break
        break
    if(ch==3):
        t1=time.time()
        word=input("enter the word to be searched:\n")
        search(word)
        t2=time.time()
        #print("time="+str(t2-t1)+"sec")
        break
    if(ch==4):
        t1=time.time()
        FINDANDreplace()
        t2=time.time()
        lineIndex(fname)
        #print("time="+str(t2-t1)+"sec")
        break
    if(ch==5):
        t1=time.time()
        delete()
        t2=time.time()
        lineIndex(fname)
        #print("time="+str(t2-t1)+"sec")
        break
    if(ch==6):
        lineIndex(fname)
        print("index built succesfully nd saved as result.json")
        break
    if(ch==7):
        searcindex()
        break
    if(ch==8):
        viewindex()
        break
print("program done\n")

        




   




