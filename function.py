
def letterandNumbers(num):
    if (num == '0'):
        return 0
    elif (num == '1'):
        return 0
    elif (num == '2'):
        return 0
    elif (num == '3'):
        return 0
    elif (num == '4'):
        return 0
    elif (num == '5'):
        return 0
    elif (num == '6'):
        return 0
    elif (num == '7'):
        return 0
    elif (num == '8'):
        return 0
    elif (num == '9'):
        return 0
    else :
        return 1

def startup(list,size):
    for i in range(size):
        list.append('_')

def AddLetter(list1,list2,letter):
    for pos,item in enumerate(list1):
        if (item == letter):
            list2[pos] = letter

def Print(list):
    for i in list:
        print(f"{i}",end=' ')



def Result(l,w,word):
    if (l == 6):
        return 0
    elif (w == len(word)):
        return 1

def DesignGame(loser):
    if (loser == 0):
        print("""
______
|     |  
|
|
|
|
______________________

        """)
    elif (loser == 1):
        print("""
______
|     |  
|     0 
|
|
|
______________________
        
        """)
    elif (loser == 2):
        print("""
______
|     |  
|     0
|     |  
|
|
______________________
        
        """)
    elif (loser == 3):
        print("""
______
|     |  
|     0__
|     |  
|
|
______________________
        
        """)
    elif (loser == 4):
        print("""
______
|     |  
|   __0__
|     |
|
|
______________________

        """)
    elif (loser == 5):
        print("""
______
|     |  
|   __0__
|     |
|      \    
|
______________________
        
        """)
    elif (loser == 6):
        print("""
______
|     |  
|   __0__
|     |
|    / \    
|
______________________

        """)
