import re

def markdown_to_html(markdown_text):
    # Cabeçalhos
    markdown_text = re.sub(r'^#\s(.+)$', r'<h1>\1</h1>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^##\s(.+)$', r'<h2>\1</h2>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^###\s(.+)$', r'<h3>\1</h3>', markdown_text, flags=re.MULTILINE)

    # Bold
    markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown_text)

    # Itálico
    markdown_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdown_text)

    # Lista numerada
    markdown_text = re.sub(r'^\d+\.\s(.+)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'(?<=<\/li>)\s*(?=\d+\.)', r'<li>', markdown_text)

    if re.search(r'<li>', markdown_text):
        markdown_text = f'<ol>{markdown_text}</ol>'

    # Link
    markdown_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', markdown_text)

    # Imagem
    markdown_text = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', markdown_text)

    return markdown_text

# Exemplo de uso
markdown_input = """
# Título
Este é um **exemplo** de conversor de *Markdown* para HTML.

## Lista
1. Primeiro item
2. Segundo item
3. Terceiro item

## Link e Imagem
Como pode ser consultado em [página da UC](http://www.uc.pt).
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com).
"""

html_output = markdown_to_html(markdown_input)
print(html_output)
