print('Bem vindo ao verificador de CPF')
cpf = input('Por favor, coloque o CPF(somente números): ')
cpf_new = cpf[:-2]
cpf_temp = ''
multi1 = 10
multi2 = 11
result1 = 0
result2 = 0

for x in cpf_new:
    k = int(x)
    cpf_temp += x
    if multi1 <= 10:
        num1 = k * multi1
        result1 += num1
        multi1 -= 1
d1 = (result1 * 10) % 11
cpf_temp += str(d1)

for y in cpf_temp:
    o = int(y)
    if multi2 <= 11:
        num2 = o * multi2
        result2 += num2
        multi2 -= 1
d2 = (result2 * 10) % 11
cpf_temp += str(d2)

if cpf == cpf_temp:
    print('CPF válido!')
else:
    print('CPF inválido!')
