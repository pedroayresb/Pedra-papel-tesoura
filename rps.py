import random

print('PEDRA PAPEL TESOURA')

wins = 0
losses = 0
ties = 0

while True:
    print(str(wins) +' vitórias', str(losses) +' derrotas', str(ties) + ' empates')
    while True:
        print('Jogue com R para Pedra, P para Papel e T para Tesoura')
        playerMove=input()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 't':
            break
        print('Jogue com R para Pedra, P para Papel e T para Tesoura')
    if playerMove == 'r':
        print('PEDRA vs...')
    elif playerMove == 'p':
        print('PAPEL vs...')
    elif playerMove == 't':
        print('TESOURA vs..')
    randomNum = random.randint(1,3)
    if randomNum == 1:
        compMove = 'r'
        print('PEDRA')
    elif randomNum == 2:
        compMove = 'p'
        print('PAPEL')
    elif randomNum == 3:
        compMove = 't'
        print('TESOURA')
    if playerMove == compMove:
        print('EMPATE')
        ties=ties+1
    elif playerMove=='r' and compMove=='t':
        print('VITÓRIA')
        wins=wins+1
    elif playerMove=='r' and compMove=='p':
        print('DERROTA')
        losses=losses+1
    elif playerMove=='p' and compMove=='r':
        print('VITÓRIA')
        wins=wins+1
    elif playerMove=='p' and compMove=='t':
        print('DERROTA')
        losses=losses+1
    elif playerMove=='t' and compMove=='r':
        print('DERROTA')
        losses=losses+1
    elif playerMove=='t' and compMove=='p':
        print('VITÓRIA')
        wins=wins+1