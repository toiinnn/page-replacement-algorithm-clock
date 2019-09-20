from itertools import cycle
import time

list = []

def insertPage(page):
    list.append(page)

def listPages():
    for index,page in enumerate(list):
        print("Página atual: {0} bit R {1}".format(index+1, page[0]))
    print('\n')

def verify():
    for index,page in enumerate(cycle(list)):
        if(page[0]==0):
            return index
        else:
            page[0] = 0

#falta criar a Thread que verificará os 10 seg automicamente
def main():       
    while(True):
        option = input("Deseja fazer o que?\n (1) Inserir página \n (2) Listar páginas\n (3) Sair\n \nSua opção:")
        if(option == '1'):
            if(len(list) <= 10):
                insertPage((1,time.time())) 
            else:
                index= verify()
                list[index] = (1,time.time())                
        elif (option == '2'):
            listPages()
        elif (option == '3'):
            break
        else:
            continue

main()  



