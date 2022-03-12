size=int(input("Enter size of the NxN matrix: "))
list=[]
flag="y"
l=[]
life=0
count=0
initial=0
temp=0
t=1
c=0
ball_count=3
ball=size//2
dir=""
for j in range(size):
    for i in range(size):
        l.append("W")
    list.append(l)
    l=[]
    
for i in range(1,size-1):
        for j in range(1,size-1):
            list[i][j]=" "
            
for i in range(1,size-1):
    list[size-1][i]="G"

    
while 1:
    row,column,typ=input("Enter the briks position and the brick type : ").split(" ")
    row=int(row)
    column=int(column)
    
    if row>=size or column>=size or row<1 or column<1 :
        print("***invalid input value of rows,column***")
        continue    
    if typ=="de" or typ=="DE" or typ=="ds" or typ=="DS" or typ=="b" or typ=="B":
        list[row][column]=typ
    else:
        typ=int(typ)
        list[row][column]=typ
    flag=input("Do you want to continue(Y or N)")
    if flag=="n" or flag=="N":
        ball_count=int(input("Enter Ball count "))
        while ball>=size:
            ball=int(input("invalid ball count please input coorect ball count : "))
        list[size-1][ball]="o"
        break   
        
        
while t:   
    
    list[size-1][ball]="o"
    for i in list:
        print(*i)
    print(f"Ball count is {ball_count}")
    
    
    count=0
    for i in range(1,size-1):
        for j in range(1,size-1):
            if list[i][j]==" ":
                count+=1
    
    
    if count==(size-2)*(size-2):
        print("You win HURRAY...!!")
        t=0
        
        continue
    if ball_count==0:
        print("Game over..!!")
        t=0
        continue



    dir=input("Enter the direction in which the ball need to traverse : ")
    if dir=="st" or dir=="ST":
        for i in range(size-2,0,-1):
            initial=ball
            if list[i][ball]=="w":
                break
                
            elif list[i][ball]=="b" or list[i][ball]=="B":
                list[i][ball]=" "
                
                for i in range(1,((size-2)//2)+1):
                    if list[size-1][ball+i]!="_" and list[size-1][ball+1]!="W":
                        list[size-1][ball+i]="_"
                        break
                    elif list[size-1][ball-i]!="_" and list[size-1][ball-i]!="W":
                        list[size-1][ball-i]="_"
                        break
                break
                

                    
            
            elif list[i][ball]=="de" or list[i][ball]=="DE":
                for j in range(1,size-1):
                    list[i][j]=" "
                
            elif list[i][ball]=="ds" or list[i][ball]=="DS":
                
                if list[i][ball]!="w":
                    list[i][ball]=" "
                if list[i+1][ball+1]!="w":
                    list[i+1][ball+1]=" "
                if list[i+1][ball-1]!="w":
                    list[i+1][ball-1]=" "
                if list[i-1][ball+1]!="w":
                    list[i-1][ball+1]=" "
                if list[i-1][ball-1]!="w":
                    list[i-1][ball-1]=" "
                if list[i-1][ball]!="w":
                    list[i-1][ball]=" "
                if list[i][ball+1]!="w":
                    list[i][ball+1]=" "
                if list[i][ball-1]!="w":
                    list[i][ball-1]=" "
                break
                    
                
                
                
            elif list[i][ball]!=" ":
                list[i][ball]-=1
                
                if list[i][ball]<=0:
                    list[i][ball]=" "
                break
                
                
    elif dir=="ld" or dir=="LD": 
        
        list[size-1][ball]="G"
        
        if ball<=1:
            continue
        #ball=ball-1
        c=0
        
        for i in range(size-2,-1,-1):
            
            if list[i][ball-1]!="W" and c!=1 :
                ball-=1
            
            elif c==2:
                print("Game over...!!!")
                t=0
                
                list[size-1][ball]="o"
                
                break
            elif c==1:
                ball=ball+1
                
            if list[i][ball]=="W":
                c+=1
                
                
                if c==2:
                    
                    list[size-1][3]="o"
                    ball=size//2
                    ball_count-=1
                    if ball_count==0:
                        print("game over ...!!!")
                        t=0
                        
                        exit()
                    elif ball_count!=0:
                        ball=3
                if c!=2:
                    ball=ball+2
                    
            #elif list[i][ball]!="W" and c!=1 :
             #   ball-=1
            
                

            if list[i][ball]=="de" or list[i][ball]=="DE":
                for j in range(1,size-1):
                    list[i][j]=" "
                if list[size-1][ball]=="_":
                    list[size-1][initial]="_"
                    list[size-1][ball]="o"
                    life+=1
                    
                else:
                    list[size-1][ball]="o"
                break
                
            
            elif list[i][ball]=="ds" or list[i][ball]=="DS":
                print("yes")
                
                if list[i][ball]!="W":
                    list[i][ball]=" "
                if list[i+1][ball+1]!="W":
                    list[i+1][ball+1]=" "
                if list[i+1][ball-1]!="W":
                    list[i+1][ball-1]=" "
                if list[i-1][ball+1]!="W":
                    list[i-1][ball+1]=" "
                if list[i-1][ball-1]!="W":
                    list[i-1][ball-1]=" "
                if list[i-1][ball]!="W":
                    list[i-1][ball]=" "
                if list[i][ball+1]!="W":
                    list[i][ball+1]=" "
                if list[i][ball-1]!="W":
                    list[i][ball-1]=" "
                if list[size-1][ball]=="_":
                    list[size-1][initial]="_"
                    list[size-1][ball]="o"
                    life+=1
                    
                else:
                    list[size-1][ball]="o"
                
                break
                    
                    
            elif list[i][ball]!=" " and list[i][ball]!="W":
                list[i][ball]-=1
                if list[i][ball]<=0:
                    list[i][ball]=" "
                if list[size-1][ball]=="_":
                    list[size-1][initial]="_"
                    list[size-1][ball]="o"
                    life+=1
                    
                else:
                    list[size-1][ball]="o"
                
                break
        if initial!=ball and life!=1:
            ball_count-=1
            life=0
                    
                    
    elif dir=="rd" or dir=="RD":
        list[size-1][ball]="G"
        #ball=ball+1
        
        if ball>=size-2:
            continue
        c=0
        
        for i in range(size-2,-1,-1):
            
            if list[i][ball]!="w" and c!=1:
                ball+=1
            
            elif c==2:
                print("game over..!!")
                t=0
                list[size-1][ball]=="o"
                break
            elif c==1:
                ball=ball-1
            if list[i][ball]=="W":
                c+=1
                
                if c==2:
                    list[size-1][3]="o"
                    ball=size//2
                    ball_count-=1
                    if ball_count==0:
                        print("Gmae over ..!!")
                        t=0
                        exit()
                if c!=2:
                    ball=ball-2
                    
           # elif list[i][ball]!="w" and c!=1:
            #    ball+=1
            
                
                
            
            
            if list[i][ball]=="de" or list[i][ball]=="DE":
                
                for j in range(1,size-1):
                    list[i][j]=" "
                if list[size-1][ball]=="_":
                    list[size-1][initial]="_"
                    list[size-1][ball]="o"
                    life+=1
                    
                else:
                    list[size-1][ball]="o"
                break
                
                
            elif list[i][ball]=="ds" or list[i][ball]=="DS":
                
                if list[i][ball]!="W":
                    list[i][ball]=" "
                if list[i+1][ball+1]!="W":
                    list[i+1][ball+1]=" "
                if list[i+1][ball-1]!="W":
                    list[i+1][ball-1]=" "
                if list[i-1][ball+1]!="W":
                    list[i-1][ball+1]=" "
                if list[i-1][ball-1]!="W":
                    list[i-1][ball-1]=" "
                if list[i-1][ball]!="W":
                    list[i-1][ball]=" "
                if list[i][ball+1]!="W":
                    list[i][ball+1]=" "
                if list[i][ball-1]!="W":
                    list[i][ball-1]=" "
                if list[size-1][ball]=="_":
                    list[size-1][initial]="_"
                    list[size-1][ball]="o"
                    life+=1
                    
                else:
                    list[size-1][ball]="o"
                break
                    
                    
                    
            elif list[i][ball]!=" " and list[i][ball]!="W":
                list[i][ball]-=1
                if list[i][ball]<=0:
                    list[i][ball]=" "
                if list[size-1][ball]=="_":
                    list[size-1][initial]="_"
                    list[size-1][ball]="o"
                    life+=1
                    
                else:
                    list[size-1][ball]="o"
                
                
                break
        if initial!=ball and life!=1:
            ball_count-=1
            
            life=0
    
    elif dir=="exit"or dir=="EXIT":
        print("Tankyou for playing...")
        t=0
    else:
        print("invalid direction..!!")
    
        
  
    
            
            
                    
                    
            
            

            

    
    



