ct1=0
ct2=0
ct3=0
ctb=0
ctn=0
def menu():
    print('Bem vindo ao menu de votação\n'
          'Digite o Número do candidato ou voto nulo/branco\n'
            '1-candidato 1\n'
            '2-canditado 2\n'
            '3-candidato 3\n'
            '4-voto nulo\n'
            '5-voto branco\n'
          )

votos={
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
    }
while True:
        menu()
        num=int(input('Digite o número do candidato: '))
        if num ==0:
            break
        elif num in votos:

            input('Aperte Enter para confirmar')
            print('voto confirmado\n')
            votos[num]+=1
        else:
            print('Número invalido')
            input('Aperte Enter para retornar')
            menu()


total=sum(votos.values())
ct1=votos[1]
ct2=votos[2]
ct3=votos[3]
ctb=votos[4]
ctn=votos[5]
perc_nulos=(ctn/total)*100
perc_brancos=(ctb/total)*100

vencedor = max(votos[1], votos[2], votos[3])

if vencedor == votos[1]:
    print('O candidato 1 venceu a eleição')
elif vencedor == votos[2]:
    print('O candidato 2 venceu a eleição')
else:
    print('O candidato 3 venceu a eleição')


print('Resultado das eleições\n')
print(f'O total de votos do candidato 1 é {ct1}')
print(f'O total de votos do candidato 2 é {ct2}')
print(f' total de votos do candidato 3 é {ct2}')
print(f'Votos nulos: {ctn}')
print(f'percentual de votos nulos: {perc_nulos:.2f}')
print(f'percentual de votoss brancos: {perc_brancos:.2f}')
print(f'Votos brancos: {ctb}')