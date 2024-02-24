# PL2024
## Gonçalo Lobo Freitas, A96136


Este é um simples script em Python que converte texto em formato Markdown para HTML. Ele utiliza expressões regulares para reconhecer e transformar elementos específicos do Markdown em suas contrapartes HTML.

### Funcionalidades Suportadas

#### Cabeçalhos: 
Converte os cabeçalhos Markdown (#, ##, ###) para tags HTML correspondentes (h1, h2, h3).

#### Negrito (Bold): 
Transforma o texto entre duplos asteriscos em texto em negrito usando a tag <b>.

#### Itálico: 
Transforma o texto entre asteriscos simples em texto em itálico usando a tag <i>.

#### Listas Numeradas: 
Converte listas numeradas Markdown para listas ordenadas HTML.

#### Links: 
Transforma links Markdown [texto](URL) em links HTML usando a tag <a>.

#### Imagens: 
Converte imagens Markdown ![alt text](URL) em tags de imagem HTML usando a tag <img>.