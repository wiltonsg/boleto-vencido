#!/usr/bin/env python3
# coding=utf-8

from datetime import *

# Calculando dias de atraso
'''d0 é a Data do vencimento
   d1 é a Data de pagamento
'''
d0 = datetime.strptime('10/11/2018', '%d/%m/%Y')
d1 = datetime.strptime('20/11/2018', '%d/%m/%Y')
delta = d1 - d0
print(delta.days)

# Guardando o valor do boleto
valor = float(input('Digite o valor do boleto: '))

# Calculo da multa
multa = float(input('Digite a porcentagem da multa: '))
multa = (valor * (multa / 100))
print('Valor do boleto com multa é: ', round(multa, ndigits=2))

# Calculo do juros
juros = float(input('Digite a porcentagem do juros: '))
juros = (valor * (juros / 100 * (delta.days)))
print('Valor do boleto com juros é: ', round(juros, ndigits=2))

# Soma do juros mais multa
mj = multa + juros
print('A soma da multa mais o juros é: ', round(mj, ndigits=2))

# Total
total = valor + mj
print('Valor total a pagar é: ', round(total, ndigits=2))