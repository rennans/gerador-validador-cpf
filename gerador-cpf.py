import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

resultado_digito_1 = 0
contador_regressivo_1 = 10 # Começa com 10 e vai até 2

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0 # Evita que o digito seja 10, se o valor for menor ou igual a nove continua sendo o mesmo

resultado_digito_2 = 0
contador_regressivo_2 = 11 # Começa com 11 e vai até 2
dez_digitos = nove_digitos + str(digito_1)
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf = nove_digitos + str(digito_1) + str(digito_2)
print(cpf)

