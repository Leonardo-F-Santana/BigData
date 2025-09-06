import re
texto = "Onúmero de telefone Raphael é (123) 456-7890"
padrao = r'\(\d{3}\) \d{3}-\d{4}'
#padrão para encontrar números de telefone no formato (xxx) xxx-xxxx

resultado = re.search(padrao, texto)

if resultado:
    numero_telefone = resultado.group()
    print("Numero de telefone encontrato", numero_telefone)
else:
    print("Número de telefone não encontrado.")