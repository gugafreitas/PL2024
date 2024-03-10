# Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
# Select id, nome, salario From empregados Where salario >= 820

import re

# Definir a linguagem da query
query_language = [
    ('SELECT', r'SELECT'),
    ('FROM', r'FROM'),
    ('WHERE', r'WHERE'),
    ('ID', r'id'),
    ('NOME', r'nome'),
    ('SALARIO', r'salario'),
    ('NUMBER', r'\d+'),
    ('COMMA', r','),
    ('GREATER_EQUAL', r'>='),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Para identificadores como nomes de tabelas e colunas
]

def lexer(query):
    tokens = []

    # Construindo a expressão regular combinada
    regex_combined = '|'.join('(?P<%s>%s)' % pair for pair in query_language)
    pattern = re.compile(regex_combined)

    # Encontrando todos os tokens na consulta
    for match in pattern.finditer(query):
        for name, value in match.groupdict().items():
            if value is not None:
                tokens.append((name, value))

    return tokens

# Exemplo de uso
query = "Select id, nome, salario From empregados Where salario >= 820"
tokens = lexer(query)

# Exibindo os tokens encontrados
for token in tokens:
    print(token)
