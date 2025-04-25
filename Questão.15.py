salario = float(input("Digite o salário fixo: "))#pede o salario fixo do funcionario
venda = float(input("Digite o valor de suas vendas: "))#pede quanto o funcionario vendeu
#calcula a sua comissão
valor_comissão = venda * 0.04
comissão = salario + valor_comissão
#mostra os resultados
print("O valor da comissão ficou de R$",valor_comissão)
print("O salario com a comissão adicionada ficou no valor de R$",comissão)