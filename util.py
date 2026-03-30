import random

def inputint(msg="Digite um valor inteiro: ",min=None,max=None):
    """
    Permite obter uma entrada de dados no formato inteiro fornecida pelo usuário.

    :param msg: Mensagem a ser apresentada para o usuário
    :param min: Menor valor que pode ser aceito para um número inteiro
    :param max: Maior valor que pode ser aceito para um número inteiro
    :raises ValueError: Caso o valor fornecido não seja um número inteiro
    :raises Exception: Caso o valor inteiro fornecido não esteja dentro dos parâmetros aceitos de min e max
    :return: Um número inteiro 
    """
    erro = True
    while erro == True:
        try:
            valor = int(input(msg))
            if min!=None and type(min)!=int:
                raise Exception(f'ERRO: O valor mínimo deve ser inteiro e não {min}')
            if max!=None and type(max)!=int:
                raise Exception(f'ERRO: O valor máximo deve ser inteiro e não {max}')
            if min!=None and valor < min:
                raise Exception(f'ERRO: valor é menor do que o mínimo permitido de {min}')
            if max!=None and valor > max:
                raise Exception(f'ERRO: valor é maior do que o máximo permitido de {max}')
            erro = False
            return valor
        except ValueError:
            print ('ERRO: Valor informado não é inteiro!')
        except Exception as e:
            print(e)

def inputfloat(msg="Digite um número real: ",min=None,max=None):
    erro = True
    while erro == True:
        try:
            valor = float(input(msg))
            if min!=None and valor < min:
                raise Exception(f'ERRO: valor é menor do que o mínimo permitido de {min}')
            if max!=None and valor > max:
                raise Exception(f'ERRO: valor é maior do que o máximo permitido de {max}')
            erro = False
            return valor
        except ValueError:
            print ('ERRO: Valor informado não é um número real!')
        except Exception as e:
            print(e)

def gerar_palavra(min=4,max=10):
    qtde_letras = random.randrange(min,max+1)
    palavra=''
    for _ in range(qtde_letras):
        palavra += chr(random.randrange(65,91))
    return palavra

