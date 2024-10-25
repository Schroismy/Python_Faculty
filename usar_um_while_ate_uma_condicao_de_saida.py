
#Usar um while até uma condição de saída
entrada = input('Digite um ano ou FIM para sair: ')
while entrada != 'FIM':
  try:
    ano = int(entrada)
  except:
    print('Não é um número!!\n')
    entrada = input('Digite um ano ou FIM para sair: ')
    continue

  if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(f'O ano {ano} é bissexto (tem 366 dias)\n')
  else:
    print(f'O ano {ano} não é bissexto (tem 365 dias)\n')
  entrada = input('Digite um ano ou FIM para sair: ')

print('Obrigado!!')
