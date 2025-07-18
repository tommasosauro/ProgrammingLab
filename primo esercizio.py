def sum_list(my_list):
    tot=0
    for i in range(len(my_list)):
        tot=tot + my_list[i]
        
    return tot

my_list=[1,2,5]

risultato=sum_list(my_list)
print(risultato)