nome = input('Digite o nome do herói: ')
XP = int(input('Digite a quantidade de XP: '))

if XP < 1000:
    nivel = 'Ferro'
elif XP > 1001 and XP <= 2000:
    nivel = 'Bronze'
elif XP > 2001 and XP <= 5000:
    nivel = 'Prata'
elif XP > 5001 and XP <= 7000:
    nivel = 'Ouro'
elif XP > 7001 and XP <= 8000:
    nivel = 'Platina'
elif XP > 8001 and XP <= 9000:
    nivel = 'Diamante'
elif XP > 9001 and XP <= 10000:
    nivel = 'Mestre'
elif XP >= 10001:
    nivel = 'Grão-Mestre'
else:
    nivel = 'Nível não encontrado'

print(f'O Herói de nome {nome} está no nível {nivel}')
