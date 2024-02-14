# Função para ler o arquivo CSV manualmente
def ler_csv(nome_arquivo):
    with open(nome_arquivo,'r',encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = [linha.strip().split(',') for linha in linhas[1:]]
        dataset = [dict(zip(cabecalho, linha)) for linha in dados]
    return dataset


# Leitura do dataset a partir de um arquivo CSV
nome_arquivo = 'emd.csv'
dataset = ler_csv(nome_arquivo)

#1 Lista ordenada alfabeticamente das modalidades desportivas
modalidades = sorted(set(line['modalidade'] for line in dataset))
print(f'Lista ordenada alfabeticamente das modalidades: {modalidades}')

#2 Percentagens de atletas aptos e inaptos para a prática desportiva
aptos = sum(line['resultado']=='true' for line in dataset)
inaptos = sum(line['resultado']=='false' for line in dataset)
total = len(dataset)

percentagem_aptos = (aptos / total) * 100
percentagem_inaptos = (inaptos / total) * 100
print(f'Percentagens de atletas aptos para a prática desportiva: {percentagem_aptos}%')
print(f'Percentagens de atletas inaptos para a prática desportiva: {percentagem_inaptos}%')

#3 Distribuição de atletas por escalão etário (intervalo de 5 anos)
idades = [int(line['idade']) for line in dataset]
idades.sort()

intervalos_etarios = [(i, i + 4) for i in range(idades[0], idades[-1], 5)]
distribuicao_etaria = {f'[{inicio}-{fim}]': sum(1 for idade in idades if inicio <= idade <= fim) for inicio, fim in intervalos_etarios}

print('Distribuição de atletas por escalão etário:')
for intervalo, quantidade in distribuicao_etaria.items():
    print(f'{intervalo}: {quantidade} atletas')