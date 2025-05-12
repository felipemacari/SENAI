altura_pessoa = float(input("Sua altura: "))#pede a altura
sombra_pessoa = float(input("Sombra da pessoa: "))#pede a sombra
sombra_predio = float(input("Sombra do prédio: "))#pede a sombra do predio
altura_predio = (sombra_predio * altura_pessoa) / sombra_pessoa#calcula a altura do predio
print("Altura do prédio:",altura_predio,"metros")