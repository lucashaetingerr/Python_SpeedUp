import threading
import time

#funçao pra somar valores - sequencial
def soma_sequencial(lista):
    soma=0
    for numero in lista:#iteraçao sobre cada número na lista
        soma+=numero#adiciona o número à soma total
    return soma

lista_numeros=list(range(1000000))#lista de 0 ao numero do parametro -> se o range for baixo vai ficar com resultados com hexa e pode nao bater nas somas
inicio_sequencial=time.time()#marca o tempo de inicio para a execuçao sequencial
resultado_sequencial=soma_sequencial(lista_numeros)#execuçao da funçao sequencial
tempo_sequencial=time.time()-inicio_sequencial#calcula o tempo de execuçao para a soma sequencial

print("Resultado da soma sequencial:",resultado_sequencial)
print("Tempo de execução da soma sequencial:",tempo_sequencial,"segundos")

#funçao que soma valores - paralela
def soma_paralela(lista, resultado, index):
    soma=sum(lista)#soma os elementos da sublista
    resultado[index]=soma#armazena o resultado no indice apropriado da lista de resultado

#exemplo de uso pra soma paralela
num_threads=4
tamanho_parte=len(lista_numeros)//num_threads#calculando o tamanho de cada parte pra threads

threads=[]#lista para manter as threads
resultados=[0]*num_threads#lista para armazenar os resultados de cada thread
inicio_paralelo=time.time()#marca o tempo de inicio pra execuçao paralela

#cria e inicia as threads
for i in range(num_threads):
    parte_lista=lista_numeros[i*tamanho_parte:(i+1)*tamanho_parte]#particiona a lista pra cada thread
    thread=threading.Thread(target=soma_paralela,args=(parte_lista,resultados,i))#cria uma thread
    threads.append(thread)#adiciona a thread a lista de threads
    thread.start()

#espera todas as threads terminarem
for thread in threads:
    thread.join()

resultado_paralelo=sum(resultados)#soma os resultados de todas as threads pra ter o resultado final
tempo_paralelo=time.time()-inicio_paralelo

print("\nResultado da soma paralela:",resultado_paralelo)
print("Tempo de execução da soma paralela:",tempo_paralelo,"segundos")

speedup=tempo_sequencial/tempo_paralelo#calculo dos slides
print("\nSpeedup:", speedup)
