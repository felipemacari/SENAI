#pede os numeros
n1 = float (input("Digite o 1º número: "))
n2 = float (input("Digite o 2º número: "))
if n2 == 0:#se o 2º for 0 vai dar numero inválido
    print("Número inválido")
else:#senao ele faz a divisão
    total = n1 / n2
print("A divisão fica:",total)