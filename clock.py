from itertools import cycle
import time

list = []
cycleList = cycle(list)        


def insertPage(page):
    list.append(page)

def listPages():
    count = 1
    for page in cycleList:
        print("Página atual: {0} bit R {1}".format(count, page[0]))
        count = count + 1



def main():       
    #pointer = cycleList(0)
    while(True):
        option = input("Deseja fazer o que?\n (1) Inserir página \n (2) Listar páginas")
        if(option == '1'):
            if(len(list) <= 10):
                insertPage((1,time.time()))
            else:
                
        elif (option == '2'):
            listPages()
        else:
            continue

main()  



