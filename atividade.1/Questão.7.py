#valores das moedas
um_c = 0.01
cinco_c = 0.05
dez_c = 0.10
vintecinco_c = 0.25 
cinquenta_c = 0.50
um_r = 1
#pede quantas moedas de cada valor tem no cofre
umcentavo = int (input("Quantas moedas de 1 centavo são: "))
cincocentavo = int (input("Quantas moedas de 5 centavos são: "))
dezcentavo = int (input("Quantas moedas de 10 centavos são: "))
vintecincocentavo = int (input("Quantas moedas de vinte cinco centavos são: "))
cinquentacentavo = int (input("Quantas moedas de cinquenta centavos são: "))
umreal = int (input("Quantas moedas de 1 real são: "))
#calcula
total_um_centavo = umcentavo * um_c
total_cinco_centavo = cincocentavo * cinco_c
total_dez_centavo = dezcentavo * dez_c
total_vinte_cinco_centavo = vintecincocentavo * vintecinco_c
total_cinquenta_centavo = cincocentavo * cinquenta_c
total_um_real = umreal * um_r

total = total_um_centavo + total_cinco_centavo + total_dez_centavo + total_vinte_cinco_centavo + total_cinquenta_centavo + total_um_real

print("O total que havia no cofre era:",total)# fala o valor total que tinha no cofre