def inputint(msg):
    try:
        valor = int(input(msg))
        return valor
    except ValueError:
        print ('ERRO: Valor informado não é inteiro!')
    return -1

def inputfloat(msg):
    try:
        valor = float(input(msg))
        return valor
    except ValueError:
        print ('ERRO: Valor informado não é um número real!')
    return -1