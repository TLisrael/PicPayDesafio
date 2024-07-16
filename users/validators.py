from django.core.exceptions import ValidationError

def validate_cpf(value):
    #remove os pontos 
    cpf = ''.join([char for char in value if char.isdigit()])
    
    #verifica se possui 11 digitos
    if len (cpf) != 11:
        print('Aqui 3')
        raise ValidationError('CPF Inválido')
    #verifica se todos os digitos sao iguais
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido')
    
    #calcula digitos verificadores
    def calcular_digito(cpf, digits):
        soma = sum(
            int(cpf[i]) * digits[i]
            for i in range(len(digits))
            )
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    primeiro_multi = list(range(10,1,-1))
    primeiro_digit = calcular_digito(cpf, primeiro_multi)
    
    
    segundo_multi = list(range(11,1,-1))
    segundo_digit = calcular_digito(cpf, segundo_multi)
    
    if not (cpf[-2] == str(primeiro_digit) and cpf[-1] == str(segundo_digit)):
        raise ValidationError('CPF inválido')