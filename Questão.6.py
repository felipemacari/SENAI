#valores dos produtos
lata = 0.350
garrafa = 0.600
litro = 2
#pede quais produtos vai ser comprado
compralata = int(input("Digite quantas latas vai comprar: "))
compragarrafa= int(input("Digite quantas garrafas vai comprar: "))
compralitro = int(input("Digite quantos litros vai comprar: "))
#contas para saber quantos litros de refriferante foi comprado
totallata = compralata * lata
totalgarrafa = compragarrafa * garrafa
totallitro = compralitro * litro

total = totallata + totalgarrafa + totallitro
#mostra o total
print("O cliente comprou",total,"litros de refrigerante")
