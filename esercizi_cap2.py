print("Esercizio 1")

def minuti_in_ore(minuti):
    ore=int(minuti/60)
    minuti=minuti%60
    print("I minuti in ore sono {} ore e {} minuti.".format(ore,minuti))

minuti=538

minuti_in_ore(minuti)

print("   ")
print("Esercizio 2")
print("   ")

def lettera_nella_parola(parola,lettera):
    tot=0
    for i in range(len(parola)):
        if parola[i]==lettera:
            tot=tot+1
        
    return tot

parola="allattare"
lettera="a"

totale_lettere=lettera_nella_parola(parola,lettera)
print(totale_lettere)



print("   ")
print("Esercizio 3")
print("   ")

def palindromo(stringa):
    
    temp=0
    
    for i in range(len(stringa)):
        for j in range(len(stringa)):
            if stringa[i]!=stringa[-j]:
                temp=temp+1
            else: 
                temp=temp
    
    return temp

stringa="anna"
temp=0

temp=palindromo(stringa)
          
if temp==0:
        print("La parola è palindroma")
else: 
        print("La parola non è palindroma")  
        

print("   ")
print("Esercizio 4")
print("   ")              

def triangolo(a,b,c):
    if( a+b >= c and a+c >= b and b+c >= a):
        print("Le misure non permettono di costruire un triangolo")
    else:
        print("Le misure permettono di costruire un triangolo")
        
        if( a==b or b==c or c==a):
                print("Il triangolo è isoscele.") 
        elif (a==b and b==c and c==a):
                print("Il triangolo è equilatero.")
        else:
                print("Il triangolo è scaleno.")  
        
triangolo(5,7,9)  


print("   ")
print("Esercizio 5")
print("   ")     

