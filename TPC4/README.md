# TPC4 - Analisador Léxico para Linguagem de Query (28/02/2024)

- **Nome:** João Manuel Machado da Cunha
- **Nº:** A104611
- **Foto:**

![foto](https://avatars.githubusercontent.com/u/131183584?v=4)

## Resumo
Este projeto implementa um analisador léxico para uma linguagem de query semelhante a SPARQL, utilizada para consultas em bases de dados como DBPedia. O programa analisa o texto de entrada e identifica diferentes tipos de tokens como palavras-chave, variáveis, strings e caracteres especiais.

#### Funcionalidades Suportadas:
- **Keywords**: Reconhecimento de palavras-chave como `select`, `where`, `LIMIT`
- **Variáveis**: Identificação de variáveis que começam com `?`
- **Strings**: Processamento de strings entre aspas duplas
- **Identificadores**: Reconhecimento de identificadores incluindo namespaces (ex: `dbo:MusicalArtist`)
- **Caracteres Especiais**: Identificação de caracteres como `{`, `}`, `.`, `@`
- **Comentários**: Processamento de comentários que começam com `#`

## Arquivos do Projeto:
- [analisadorLexico.py](analisadorLexico.py) - Script principal do analisador léxico

## Utilização:
Para executar o analisador léxico:
```bash
python analisadorLexico.py
```

## Exemplo de Query:
```sparql
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

## Exemplo de Saída:
```python
('KEYWORD', 'select', 1, (0, 6))
('VARIABLE', '?nome', 1, (7, 12))
('VARIABLE', '?desc', 1, (13, 18))
('KEYWORD', 'where', 1, (19, 24))
('SPECIAL', '{', 1, (25, 26))
# ... mais tokens ...
```