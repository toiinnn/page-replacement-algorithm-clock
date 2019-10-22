from itertools import cycle
import time
import threading

list = []

'''
	Apresenta todas as páginas, com seus bits marcados
'''
def listPages():
    for index,page in enumerate(list):
        print("\nPágina atual: {0} bit R {1}".format(index+1, page[0]))
    print('\n')

'''
	Zera as páginas que estiverem com 1 até encontrar a primeira que esteja com 0 e retorná-la
'''
def verify():
    for page in cycle(list):
        if(page[0]==0):
            return page
        else:
            page[0]=0

'''
	Troca todos os bits 1 para 0 e torna a apresentar o menu
'''
def atualize():
    while(True):
        time.sleep(10)
        for index, page in enumerate(list):
            if(page[0]==1):       
                print("\nPágina {0} teve seu bit R zerado!".format(index+1))
                page[0]=0         
        menu()

'''
	Menu de opções ao usuário,
	Op. 1 - Adiciona página à lista de páginas caso haja menos de 10, ou atualiza o horário 
	Op. 2 - Lista todas as páginas
'''
def menu():
    option = input("Deseja fazer o que?\n (1) Inserir página \n (2) Listar páginas \nSua opção:")
    if(option == '1'):
        if(len(list) < 10):
            list.append([1,time.time()])
        else:
            element = verify()
            list.remove(element)
            list.append([1,time.time()])                
    elif (option == '2'):
        listPages()

'''
	Cria a thread responsável por executar os métodos do programa. 
	Ela inicia no método 'atualize'
'''
def main():  
    toAtualize = threading.Thread(target=atualize,args=[])     
    toAtualize.start()
    while(True):
        menu()

main()  


