def inputint(msg="Digite um valor inteiro: ",min=None,max=None):
    try:
        valor = int(input(msg))
        if min!=None and valor < min:
            raise Exception(f'ERRO: valor é menor do que o mínimo permitido de {min}')
        if max!=None and valor > max:
            raise Exception(f'ERRO: valor é maior do que o máximo permitido de {max}')
        return valor
    except ValueError:
        print ('ERRO: Valor informado não é inteiro!')
    except Exception as e:
        print(e)
    return -1

def inputfloat(msg="Digite um número real: ",min=None,max=None):
    try:
        valor = float(input(msg))
        if min!=None and valor < min:
            raise Exception(f'ERRO: valor é menor do que o mínimo permitido de {min}')
        if max!=None and valor > max:
            raise Exception(f'ERRO: valor é maior do que o máximo permitido de {max}')
        return valor
    except ValueError:
        print ('ERRO: Valor informado não é um número real!')
    except Exception as e:
        print(e)
    return -1