import function

wrong = [] #letra ERRADAS e REPETIDAS
right = [] #lista com as letras CERTAS
word = list('ABCDE') #Palavra da forca

function.startup(right,len(word)) #inicializa com "_"

correct = 0
loser = winner = 0


while(True):
    letter = str(input("\033[1;34mEnter a letter: \033[m")).upper()

    if (len(letter)>1 or function.letterandNumbers(letter)== 0):
        correct = 1
    else :
        correct = 0
    
    if (correct == 0):
        if (letter in word):
            if (letter not in wrong):
                function.AddLetter(word,right,letter)
                wrong.append(letter)
                print(f"\033[1;40m{letter} -> Letter Right\033[m")
                function.Print(right)
                winner += 1
            else :
                print(f"\033[1;35m{letter} -> Repeated command!!!\033[m",end=' :')
                function.Print(wrong)
        else :
           print(f"\033[1;36m{letter} -> Letter Wrong!!!\033[m",end=' :') 
           wrong.append(letter)
           function.Print(wrong)
           loser += 1
    else :
        print("\033[1;39mInvalid,try again !!!\033[m")

    function.DesignGame(loser)
    if (function.Result(loser,winner,word) == 0 or function.Result(loser,winner,word) == 1):
        break


if (function.Result(loser,winner,word) == 0):
    print("\033[1;31mYOU LOSER !!!!!\033[m")
else :
    print("\033[1;31mYOU WIN !!!!!\033[m")




































































  















