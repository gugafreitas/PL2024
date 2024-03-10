# PL2024

## Gonçalo Lobo Freitas, A96136

- query_language: Lista de tuplos que contêm pares (nome do token, expressão regular) para definir os tipos de tokens na linguagem de query.

- lexer(query): Função principal que recebe uma consulta como entrada e retorna uma lista de tokens encontrados.

- Exemplo de Uso: A consulta de exemplo "Select id, nome, salario From empregados Where salario >= 820" é processada pelo analisador léxico e os tokens resultantes são exibidos.
