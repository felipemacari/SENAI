ano_nasc = int(input("Ano de nascimento: "))#pede quanto nesceu
ano_atual = int(input("Ano atual: "))#pede em que ano estamos
#calculos
anos = ano_atual - ano_nasc
meses = anos * 12
dias = anos * 365
semanas = dias / 7
#exibe
print(f"Idade: {anos} anos, {meses} meses, {dias} dias, {semanas:.1f} semanas")