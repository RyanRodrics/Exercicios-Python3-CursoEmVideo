def leiaDinheiro(msg):
    valid = False
    while not valid:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO! ""{entrada}"" não é um valor monetário válido. Tente novamente.\033[m')
        else:
            valid = True
            return float(entrada)
