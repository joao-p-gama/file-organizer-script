import os


text = open("lista-bordados.txt","w")

def dive(root,files): 
  for dirs, subdirs, file in os.walk(root):
    #print("estamos na pasta",dirs)
    for filename in file:
      if filename.endswith("pes"):
        temp=os.path.join(dirs,filename)
        print(temp)
        text.write(temp+"\n")


  return


      
## test


def show(c):
  for i in c:
    print(i)


r="E:"
files=[]

#for i in range(5):

def z():
    dive(r,files)
    #show(r)
    #print("-"*20)

z()

