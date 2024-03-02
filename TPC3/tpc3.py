import re

# def soma_digitos(texto):
#     somar = False
#     resultado = 0

#     for linha in texto:
#         if re.search(r"on", linha):
#             somar = True
#         if re.search(r"off", linha):
#             somar = False
#         if re.search(r"=",linha):
#             numeros = [int(digito) for digito in re.findall(r"\d+",linha)]
#             if somar:
#                 resultado += sum(numeros)
    
#     return resultado

def sum_digits(text: str):
  return sum(map(int,re.findall("\d+",text)))

def sum_digits_no_regex(text: str):
    digit_sum = 0
    current_num = ''
    for char in text:
        if char.isdigit():
            current_num += char
        else:
            if current_num:
                digit_sum += int(current_num)
                current_num = ''
    if current_num:
        digit_sum += int(current_num)
    return digit_sum

text = """
On 123 + 456 = 789 Off 10 + 20 = 30 On 40 + 50 =
"""

output = sum_digits_no_regex(text)
print(output)