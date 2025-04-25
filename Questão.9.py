litro = float(input("Quantos litros de suco serão feitos? "))#pede quanto suco será feito
#divide quanto será agua e quanto será suco
divisao = litro / 10
agua = divisao * 8 
suco = divisao * 2
#exibe quanto precisa de água e suco para fazer o total que foi pedido
print("Para fazer",litro,"litros de suco, será preciso de",agua,"litros de água e",suco,"litros de suco")