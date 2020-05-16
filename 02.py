# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais
# baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um
# dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser
# dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser
# informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
# além da média das alturas e dos pesos dos clientes.
cod = 1
dados = list()
cliente = list()
altura = codGeral = maiorPeso = 0
menorAltura = menorPeso = 10000
media = loop = 0
while True:
    if cod == 0:
        break
    cod = int(input('Informe o código do cliente ou digite zero para encerrar\n'))
    if cod !=0:
       
        dados.append(cod)
        dados.append(float(input(f'Informe altura para o cliente com código {cod}\n')))
        dados.append(float(input(f'Informe o peso para o cliente com o código {cod}\n')))
        cliente.append(dados[:])
        dados.clear()
        
for p in cliente:
    aux = p[1]
    if aux > altura:
        codGeral = p[0]
        altura = aux
print('Cliente com maior altura')
print('*'*20)
print(f'Código: {codGeral} Altura: {altura :.2f}m')

for p in cliente:
    aux = p[1]
    if aux < menorAltura:
        codGeral = p[0]
        menorAltura = aux
print('*'*20)
print('Cliente com menor altura')
print('*'*20)
print(f'Código: {codGeral} Altura: {menorAltura :.2f}m ')
print('*'*20)

for p in cliente:
    aux = p[2]
    if aux > maiorPeso:
        codGeral = p[0]
        maiorPeso = aux
print('*'*20)
print('Cliente com maior peso')
print('*'*20)
print(f'Código: {codGeral} Peso: {maiorPeso :.2f}KG ')
print('*'*20)


for p in cliente:
    aux = p[2]
    if aux < menorPeso:
        codGeral = p[0]
        menorPeso = aux
print('*'*20)
print('Cliente com menor  peso')
print('*'*20)
print(f'Código: {codGeral} Peso: {menorPeso :.2f}KG ')
print('*'*20)

if cod != 0:
    for p in cliente:
        media = media + p[1]
        loop += 1 
    media = media / loop
    print('Média das alturas')
    print('*'*20)
    print(f'{media :.2f}m')
    print('*'*20)
    media = 0 
    loop =0 
if cod != 0:
    for p in cliente :
        media = media + p[2]
        loop += 1
    media =  media / loop
    print('Média dos pesos')
    print('*'*20)
    print(f'{media :.2f}kgs')
    print('*'*20)



