#Arquivo Control
from model import somarInicioFim #Conecta a classe model e control
from model import tabuada
from model import inicioFim
from model import impares
from model import somar10Numeros
from model import calcularMedia
from model import ehPar
from model import fatorial
import this
this.opcao    = -1 #Declarando a variável
this.num      = -1 #Acionar o While.
this.i        = 0 #Contador
this.negativo = 0 #ContarNegativos

def exercicio01():
    inicio = int(input("Informe o início: "))
    fim    = int(input("Informe o fim: "))
    print(somarInicioFim(inicio,fim))

def exercicio02():
    num = int(input("Informe o número que deseja multiplicar: "))
    fim = int(input("Informe até onde deve ser multiplicado: "))
    print(tabuada(num,fim))

def exercicio03():
    inicio = int(input("Informe o valor inicial: "))
    fim    = int(input("Informe o valor final: "))
    print(inicioFim(inicio, fim))

def exercicio04():
    inicio = int(input("Informe o início: "))
    fim    = int(input("Informe o final: "))
    print(impares(inicio, fim))

def exercicio05():
    for i in range(0,10,1):
        num = int(input("Informe {}º número: ".format(i+1)))
        soma = somar10Numeros(num)
    print("A soma dos números digitados é: {}".format(soma))

def exercicio09():
    while(this.num != 0):
        this.num = int(input("Informe um valor: "))
        soma = somar10Numeros(this.num)
    print("A soma dos valores é: {}".format(soma))

def exercicio10():
    while(this.num != 0):
        this.num = int(input("Informe um número: "))
        if ehPar(this.num) == True:
            soma = somar10Numeros(this.num)
            this.i += 1 #Contar quantos números foram digitados
    print("A média dos núeros digitados é: {}".format(calcularMedia(soma,this.i)))

def exercicio11():
    while(this.num != 0):
        this.num = int(input("Informe um número"))
        #Primeira digitação do usuário
        if this.num != 0:
            if this.i == 0:
                maior = this.num
                menor = this.num
            this.i += 1
            #A partir da segunda volta...
            if this.num > maior:
                maior = this.num

            if this.num < menor:
                menor = this.num
    print(f"O maior número digitado é: {maior} \ne o menor número digitado é: {menor}")

def exercicio12():
    for i in range(20):
        this.num = int(input("Informe um valor: "))
        #a. a soma dos números positivos
        if this.num >= 0:
            soma = somar10Numeros(this.num)
        #b.a quantidade de valores negativos
        else:
            this.negativo += 1
    print(f"Há {this.negativo} números negativos\nA soma dos positivos é {soma}")

def exercicio13():
    num = int(input("Informe um número: "))
    print(fatorial(num))

def exercicio14():
    quantidade = int(input("Informe a quantidade de jogadores: "))
    for i in range(0,quantidade,1):
        altura = float(input(f"{i + 1}ª altura: "))

        while(altura <= 0):
            if altura <= 0:
                print("Erro! informe uma altura positiva!")
            altura = float(input(f"{i + 1}ª altura: "))


        soma = somar10Numeros(altura)
    print(f"A média de altura desse time é {calcularMedia(soma,quantidade)}")

def exercicio15():
    this.venc = ""
    for i in range(0, 16, 1):
        nota = float(input(f"{i+1}ª nota:"))
        while(nota < 0 or nota > 10):
            print("Erro, informe uma nota entre 0 e 10")
            nota = float(input(f"{i+1}ª nota:"))
        cand = input(f"{i+1}ª candidata: ")
        if i == 0:
            maior = nota
        if nota > maior:
            maior = nota
            this.venc  = cand
    print(f"A vencedora é: {this.venc}, sua nota foi: {maior}")





def menu():
    print("\nEscolha uma das opções abaixo: \n" +
          "0. Sair\n" +
          "1. Exercício 01\n" +
          "2. Exercício 02\n" +
          "3. Exercício 03\n" +
          "4. Exercício 04\n" +
          "5. Exercício 05\n" +
          "9. Exercício 09\n" +
          "10. Exercício 10\n" +
          "11. Exercício 11\n" +
          "12. Exercício 12\n" +
          "13. Exercício 13\n" +
          "14. Exercício 14\n" +
          "15. Exercício 15\n"
          )
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu() #Chamar o menu
        if this.opcao == 0:
            print("Obrigado!")
        elif this.opcao == 1:
            exercicio01()
        elif this.opcao == 2:
            exercicio02()
        elif this.opcao == 3:
            exercicio03()
        elif this.opcao == 4:
            exercicio04()
        elif this.opcao == 5:
            exercicio05()
        elif this.opcao == 9:
            exercicio09()
        elif this.opcao == 10:
            exercicio10()
        elif this.opcao == 11:
            exercicio11()
        elif this.opcao == 12:
            exercicio12()
        elif this.opcao == 13:
            exercicio13()
        elif this.opcao == 14:
            exercicio14()
        elif this.opcao == 15:
            exercicio15()
        else:
            print("Erro! Escolha uma opção válida!")