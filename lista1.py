'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q1():
    print('João Paulo')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    media = (5+8+12)/3
    print(f'(5+8+12)/3 = {media}')

#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    numero = int(input('Digite um número inteiro: '))
    print(f'Você digitou: {numero}')

#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    num1 = float(input('Digite um número real: '))
    num2 = float(input('Digite outro número real: '))
    print(f'Os números digitados foram: {num1:.1f} e {num2:.2f}')

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    num = int(input('Digite um número inteiro: '))
    print(f'Sucessor: {num+1}')
    print(f'Antecessor: {num-1}')

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = input('Nome: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')
    print('\nNOME\t\tEND\t\tFONE')  # \t é tabulação (TAB) e \n é new line (quebra de linha)
    print(f'{nome}\t\t{endereco}\t\t{telefone}')

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    num1 = int(input('1 Número: '))
    num2 = int(input('2 Número: '))
    print(f'{num1}-{num2} = {num1-num2}')

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    num = float(input('Digite um número real: '))
    print(f'¼ de {num} = {num/4}')

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input('1 Número Real: '))
    num2 = float(input('2 Número Real: '))
    num3 = float(input('3 Número Real: '))
    media = (num1 + num2 + num3) / 3
    print(f'Média de {num1}, {num2} e {num3} é igual a {media:.2f}')

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1 = float(input('1 Número: '))
    num2 = float(input('2 Número: '))
    print(f'{num1}+{num2} = {num1+num2}')
    print(f'{num1}-{num2} = {num1-num2}')
    print(f'{num1}*{num2} = {num1*num2}')
    print(f'{num1}/{num2} = {num1/num2}')

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    num = float(input('Digite um número real: '))
    print(f'{num}*{num} = {num*num}')               # não recomendado
    print(f'math.pow({num},2) = {math.pow(num,2)}') # recomendado para float
    print(f'{num}**2 = {num**2}')                   # recomendado para int

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input('Digite o saldo da conta: R$ '))
    saldo = round(saldo, 2) # arredonda o valor para 2 casas decimais
    print(f'Saldo de R$ {saldo:.2f} + 2% = R$ {saldo*1.02}')

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).    
def q14():
    base = float(input('Digite a base do retângulo: '))
    altura = float(input('Digite a altura do retângulo'))
    print(f'Perímetro = {base*2 + altura*2}')
    print(f'Área: {base*altura}')

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    valor = round(float(input('Valor do produto: R$ ')), 2)
    desconto_desejado = float(input('% do desconto desejado: '))
    valor_desconto = valor*desconto_desejado/100
    print(f'Valor do desconto: R$ {valor_desconto:.2f}')
    print(f'Valor final do produto: R$ {valor-valor_desconto:.2f}')

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.

questao = input('Digite a questão a ser executada: ')
eval(f'q{questao}()')  # eval transforma uma string (texto) em comando python

