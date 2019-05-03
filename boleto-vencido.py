#!/usr/bin/env python3
# coding=utf-8

from datetime import *

# Calculando de dias em atraso
print('Digite a data no seguinte formato: 01/11/2222')
datav = str(input('Informe a data de vencimento: '))
datav = datetime.strptime(datav, '%d/%m/%Y').date()
datap = str(input('Informe a data de pagamento: '))
datap = datetime.strptime(datap, '%d/%m/%Y').date()
delta = datap - datav
print(delta.days, 'dias de atraso')

# Guardando o valor do boleto
print('Coloque ponto no lugar da vírgula, exemplo R$ 40,50, informe somente: 40.50')
valor = float(input('Digite o valor do boleto: '))

# Calculo da multa
print('Informe somente o valor sem o simbolo "%" e se tiver vírgula coloque ponto no lugar')
multa = float(input('Digite a porcentagem da multa: '))
multa = (valor * (multa / 100))
print('Valor do boleto com multa é: ', round(multa, ndigits=2))

# Calculo do juros
print('Informe somente o valor sem o simbolo "%" e se tiver vírgula coloque ponto no lugar')
juros = float(input('Digite a porcentagem do juros: '))
juros = (valor * (juros / 100 * (delta.days)))
print('Valor do boleto com juros é: ', round(juros, ndigits=2))

# Soma do juros e multa
mj = multa + juros
print('Total de multa e juros é: ', round(mj, ndigits=2))

# Total
total = valor + mj
print('Valor total a pagar é: ', round(total, ndigits=2))
