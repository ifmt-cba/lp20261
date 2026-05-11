import random
from util import inputint, inputfloat, gerar_palavra
'''
Lista de Exercícios referentes a coleções e arquivos em python
'''
VERMELHO: Final = '\033[31m'
VERDE: Final = '\033[32m'
RESET: Final = '\033[m'

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(15)]
    #forma extensa da linha anterior:
    #for _ in range(15):
    #    numeros.append(random.randrange(200))

    print(numeros)
    numero: int = inputint('Digite o número a ser localizado na lista: ')
    try:
        posicao: int = numeros.index(numero)
    except ValueError:
        print('Número não encontrado!')
    else:
        print(f'Número localizado na posição: {posicao}')

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada. (ASCII 65-90)
def q2() -> None:
    letras: list[str] = [chr(random.randrange(65,91)) for _ in range(10)]
    # tipo enumerate cria automaticamente um contador para os elementos da lista começando em 0
    for posicao, letra in enumerate(letras):
        print(f'[{posicao}]: {letra}')

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)
def q21() -> None:
    tamanho_senha: int = inputint('Informe a qtde de caracteres para senha (4-32): ', min=4, max=32)
    senha: list[str] = [chr(random.randrange(40,127)) for _ in range(tamanho_senha)]
    print(f'Senha gerada: {"".join(senha)}')

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q3() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(15)]
    for posicao, numero in enumerate(numeros):  
        print(f'[{str(posicao):<2}]: {str(numero):>3} ({"PAR" if numero%2==0 else "IMPAR"})')

#3.1 Construa uma programa que armazene 15 números em uma lista e salve o resultado
# de uma listagem numerada contendo o número e uma das mensagens: par ou ímpar em um arquivo
def q31() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(15)]
    with open('resultado_q31.txt','a') as arquivo:
        arquivo.write('=======================================================\n')
        for posicao, numero in enumerate(numeros):  
            print(f'[{str(posicao):<2}]: {str(numero):>3} ({"PAR" if numero%2==0 else "IMPAR"})')
            arquivo.write(f'[{str(posicao):<2}]: {str(numero):>3} ({"PAR" if numero%2==0 else "IMPAR"})\n')

#3.2 Construa uma programa que leia 15 números de um arquivo e salve o resultado
# de uma listagem numerada contendo o número e uma das mensagens: par ou ímpar em um arquivo
def q32() -> None:
    numeros: list[int] = []
    with open ('q32_input.txt','r') as arquivo:
        for linha in arquivo:
            numeros.append(int(linha))

    with open('q32_output.txt','a') as arquivo:
        arquivo.write('=======================================================\n')
        for posicao, numero in enumerate(numeros):  
            print(f'[{str(posicao):<2}]: {str(numero):>3} ({"PAR" if numero%2==0 else "IMPAR"})')
            arquivo.write(f'[{str(posicao):<2}]: {str(numero):>3} ({"PAR" if numero%2==0 else "IMPAR"})\n')

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q4() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(8)]
    print(numeros)
    multiplos6: int = sum(1 for n in numeros if n % 6 == 0)
    print(f'Qtde de números que são múltiplos de 6: {multiplos6}')

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q5() -> None:
    alunos: list[dict] = []
    # alimenta uma lista com 15 alunos
    for c in range(1,16):
        aluno: dict = {}
        aluno['matricula']: int = c
        aluno['nome']: str = gerar_palavra(max=5)
        aluno['nota1']: float = round(random.random()*10,1)
        aluno['nota2']: float = round(random.random()*10,1)
        aluno['media']: float = round((aluno['nota1'] + aluno['nota2'])/2,1)
        aluno['situacao']: str = 'Aprovado' if aluno['media'] >= 6 else 'Reprovado'
        alunos.append(aluno)
    # Percorrer a lista de alunos para imprimir o diário
    print('MAT\tNOME\tN1\tN2\tMED\tSITUACAO')
    for aluno in alunos:
        print(f'{aluno["matricula"]}\t{aluno["nome"]}\t{aluno["nota1"]}\t{aluno["nota2"]}\t{aluno["media"]}\t{aluno["situacao"]}')

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
def q7() -> None:
    QTDE_MAX: int = 5
    qtde_10: int = 0
    qtde_10_20: int = 0
    qtde_20:int = 0
    compra: list[float] = [round(random.random()*5000,2) for _ in range(QTDE_MAX)]
    venda: list[float] = []
    lucro: list[float] = []
    for pos in range(QTDE_MAX):
        valor_venda:int  = 0
        while valor_venda <= compra[pos]:
            valor_venda = round(random.random()*10000,2)
        venda.append(valor_venda)
        lucro_monetario = venda[pos] - compra[pos]
        lucro_percentual = 1-lucro_monetario/venda[pos]
        lucro.append(round(lucro_percentual*100,2))
        if lucro_percentual < 0.1:
            qtde_10 += 1
        elif lucro_percentual <= 0.2:
            qtde_10_20 += 1
        else:
            qtde_20 += 1
    print(compra)
    print(venda)
    print(lucro)
    print(f'Qtde de produtos com lucro inferior a 10%: {qtde_10}')
    print(f'Qtde de produtos com lucro entre 10% e 20%: {qtde_10_20}')
    print(f'Qtde de produtos com lucro superior a 20%: {qtde_20}')

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.

#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#uma lista e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')
