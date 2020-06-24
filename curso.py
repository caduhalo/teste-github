"""
a=2
b=0

try:
	print(a/b)
except:#Excecao para nao travar o programa quando algum erro estiver propenso
	print("Nao e permitido a divisao por 0!")
"""
nota1 = int(input("Digite a nota1:"))
nota2 = int(input("Digite a nota2:"))

soma = (nota1+nota2)/2

if soma >= 6:
	print("APROVADO!")
else:
	print("REPROVADO!")

	
