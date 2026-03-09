def inputint(msg):
    try:
        return int(input(msg))
    except ValueError:
        print('O valor informado não é um inteiro!')
    return None