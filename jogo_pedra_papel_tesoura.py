import random

def resultado(usuario, computador):
    if usuario == computador:
        return 'Empate'
    elif (usuario == 'pedra' and computador == 'tesoura') or \
         (usuario == 'papel' and computador == 'pedra') or \
         (usuario == 'tesoura' and computador == 'papel'):
        return 'Você ganhou!'
    else:
        return 'Você perdeu!'

def main():
    print('Bem-Vindo ao jogo de pedra, papel e tesoura\n')
    
    while True:
        usuario = input('Escolha entre pedra, papel e tesoura: ').lower()
        if usuario not in ['pedra', 'papel', 'tesoura']:
            print('Escolha inválida, tente novamente.')
            continue
        computador = random.choice(['pedra', 'papel', 'tesoura'])
        print(f'O computador escolheu {computador}')
        print(resultado(usuario, computador))
        
        opcao = input('Pressione c para continuar ou qualquer outra tecla para sair: ').lower()
        if opcao != 'c':
            break

    print('Obrigado por jogar!')
    
if __name__ == "__main__":
    main()
