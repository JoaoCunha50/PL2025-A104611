# TPC3 - Conversor de Markdown para HTML (21/02/2024)

- **Nome:** João Manuel Machado da Cunha
- **Nº:** A104611
- **Foto:**

![foto](https://avatars.githubusercontent.com/u/131183584?v=4)

## Resumo
Este script foi desenvolvido para converter arquivos Markdown em HTML, implementando as funcionalidades básicas do Markdown. O programa processa elementos como cabeçalhos, texto em negrito, itálico, listas numeradas, links e imagens.

#### Funcionalidades Suportadas:
- **Cabeçalhos**: Conversão de # para `<h1>`, ## para `<h2>`, ### para `<h3>`
- **Formatação de Texto**: 
  - Negrito (`**texto**` → `<b>texto</b>`)
  - Itálico (`*texto*` → `<i>texto</i>`)
- **Listas Numeradas**: Conversão para elementos `<ol>` e `<li>`
- **Links**: Conversão de `[texto](url)` para tags `<a>`
- **Imagens**: Conversão de `![alt](src)` para tags `<img>`

## Arquivos do Projeto:
- [MDtoHTML.py](MDtoHTML.py) - Script principal do conversor
- [exemplo.md](exemplo.md) - Arquivo Markdown de exemplo
- [output1.html](output1.html) - Resultado da conversão do exemplo

## Utilização:
Para converter um arquivo Markdown para HTML, execute:
```bash
python MDtoHTML.py input.md output.html
```

### Exemplo de Input (exemplo.md):
```markdown
# Título Principal
Este é um texto com **negrito** e *itálico*.

1. Primeiro item
2. Segundo item

[Link](https://exemplo.com)
![Imagem](imagem.jpg)
```

### Output Correspondente (output1.html):
```html
<h1>Título Principal</h1>
Este é um texto com <b>negrito</b> e <i>itálico</i>.

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
</ol>

<a href="https://exemplo.com">Link</a>
<img src="imagem.jpg" alt="Imagem"/>
```