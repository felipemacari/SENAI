#pede as hooras trabalhadas
normal = float(input("Quantas horas você trabalhou: "))
extra = float(input("Quantas horas extras você realizou: "))
#llugar das contas
horanormal = normal * 10
horaextra = extra * 15
salariobruto = horanormal + horaextra
salarioliquido = salariobruto * 0.9
#imprime o resultado
print("O salário bruto é de:",salariobruto)
print("O salário líquido é de:",salarioliquido)