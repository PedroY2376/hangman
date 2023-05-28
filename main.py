import random, os

lista_palavras = ['Sardinha', 'Arte', 'Covarde', 'Poder', 'Trator', 'Fungo', 'Resposta', 'Marido', 'Acordado', 'Filho']
adivinhar_palavra = []
palavra_lista = []
letras_selecionadas = []
erros = 0

palavra = random.choice(lista_palavras).lower()
for l in palavra:
    adivinhar_palavra.append(' ')
    palavra_lista.append(l)

while True:
    os.system('cls')
    print('\033[37m')
    letras_selecionadas_mostrar = str(letras_selecionadas).strip('[]').replace(',', '-')
    print(f'Letras Selecionadas:\n{letras_selecionadas_mostrar}')

    for l in adivinhar_palavra:
        print(str(l).replace(' ', ' _'), end='')
    print()
    print()
    letra_adivinhar = input('Escolha uma letra: ').lower()

    try:
        if len(letra_adivinhar) != 1:
            print('\033[31m')
            print('Valor inválido - Digite apenas uma letra!')
            os.system('pause')
            continue

        elif int(letra_adivinhar):
            print('\033[31m')
            print('Valor inválido - Digite uma letra, nãu um número!')
            os.system('pause')
            continue
    
    except:
        if letra_adivinhar in palavra:

            if letra_adivinhar in letras_selecionadas:
                print('\033[33m')
                print('Essa palavra já foi selecionada')
                os.system('pause')
                continue
            
            letras_selecionadas.append(letra_adivinhar)
            posicao = palavra.index(letra_adivinhar)
            adivinhar_palavra[posicao] = letra_adivinhar
            print('\033[32m')
            print('Acertou')
            os.system('pause')
            if adivinhar_palavra == palavra_lista:
                os.system('cls')
                print('VOCÊ ACERTOU A PALAVRA!')
                print(palavra.title())
                break
        else:
            letras_selecionadas.append(letra_adivinhar)
            erros += 1
            print('\033[31m')
            print(f'MAIS {6 - erros}  ERROS PARA O FIM DO JOGO!')
            if erros >= 6:
                print('\033[31m')
                print('VOCÊ ERROU 6 VEZES - GAME OVER!')
                break
            print('\033[31m')
            print('Errou!')
            os.system('pause')