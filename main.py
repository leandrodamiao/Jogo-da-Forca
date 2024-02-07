from lib import enforcado
from random import choice
from time import sleep


lista = ('PATO', 'CAHORRO', 'GALINHA', 'CODORNA', 'GATO', 'MESA', 'CARRO', 'BICICLETE', 'ONIBUS', 'COZINHA', 'SALA', 'ALMOFADA', 'ESCOLA', 'LIVRO', 'CELULAR', 'ANDARILHO', 'COCHILAR', 'ESCOVAR', 'DIRIGIR', 'COZINHAR', 'COMPRAR', 'MERGULHAR', 'ESCALAR', 'PINTAR', 'ESCULPIR', 'FAZER', 'ARMARIO', 'VENTILADOR', 'TEMPO', 'PORTA', 'PORTAO', 'PEIXE', 'BANANA', 'ABACATE', 'COSTELA', 'BIFE', 'ALMONDEGA', 'COMPANHIA', 'CARTAO', 'CARTA', 'BOLSA', 'SAPATO', 'LUVA', 'CAMISA', 'BOTAO', 'BOTA', 'CASACO')
jogando = True
while jogando:
  palavra = choice(lista)
  erro = 0
  acerto = list('_' *len(palavra))

  while True:
    enforcado(erro)     
    for l in acerto:
      print(l, end=' ')
    palpite = str(input('\n\nPalpite: ')).strip().upper()[0]
    
    if palpite not in palavra:
      erro += 1
    else:
      for n, letra in enumerate(palavra):
        if letra == palpite:
          acerto[n] = letra
  
    if erro >= 7:
      print('Voce perdeu!')
      sleep(1)
      print(f'A palafra era {palavra}')
      break
    elif list(acerto) == list(palavra):
      print(f'A palavra é {palavra}')
      sleep(1)
      print('PARABÈNS!!!!')
      sleep(1)
      print('Voce acertou!')
      break
    else:
      continue

  while True:
    op = str(input('Deseja jogar mais uma partida? ')).strip().upper()[0]
    if op == 'S':
      break
    elif op == 'N':
      print('Foi muito bom jogar com você!')
      sleep(1)
      print('Volte sempre.')
      jogando = False
      break
    else:
      print('Opção inválida')