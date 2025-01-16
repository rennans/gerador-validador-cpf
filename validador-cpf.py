# Cálculo do primeiro digito do cpf
import re

entrada = input("CPF: ")
cpf = re.sub(
    r'[^0-9]', '',
    entrada
    )

if not cpf:
    print('CPF inválido: não foi informado nenhum dígito ou caractere inválido')
    exit()

cpf_formatado = cpf.replace('.', '').replace('-', '')
primeiro_caractere = cpf_formatado[0]
caractere_repetido = primeiro_caractere * len(cpf_formatado)
if caractere_repetido == cpf_formatado:
    print('CPF inválido: todos os dígitos são iguais')
    exit()

nove_digitos = cpf_formatado[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf_formatado[:10]
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

ultimos_dois_digitos = cpf_formatado[-2:]

if len(cpf_formatado) >= 11:
    if int(ultimos_dois_digitos[0]) == digito_1 and int(ultimos_dois_digitos[1]) == digito_2:
        print('CPF válido')
    else:
        print('CPF inválido')
else:
    print('CPF inválido: número de dígitos insuficiente')


