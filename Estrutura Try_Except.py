
entrada_bruta = input('Digite um número:')
try:
 entrada_inteira = int(entrada_bruta)
except:
 entrada_inteira = -1
if entrada_inteira > 0 :
 print('Bom trabalho!!')
else:
 print('Não é um número!!')
