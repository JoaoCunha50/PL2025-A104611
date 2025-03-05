import re
import sys

def tokenize(code):
    token_specification = [
        ('COMMENT',    r'#[^\n]*'),                    # Comments
        ('STRING',     r'"[^"]*"'),                    # String literals
        ('VARIABLE',   r'\?[a-zA-Z][a-zA-Z0-9]*'),     # Variables starting with ?
        ('KEYWORD',    r'(?i)(select|where|LIMIT)'),   # Keywords
        ('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9]*(?::[a-zA-Z][a-zA-Z0-9]*)*'),  # Identifiers
        ('SPECIAL',    r'[{}.@]'),                     # Special characters
        ('NEWLINE',    r'\n'),                         # Line endings
        ('SKIP',       r'[ \t]+'),                     # Skip over spaces and tabs
        ('ERRO',       r'.'),                          # Any other character
    ]
    
    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg) in token_specification])
    reconhecidos = []
    linha = 1
    
    for m in re.finditer(tok_regex, code):
        tipo = m.lastgroup
        dic = m.groupdict()
        valor = dic[tipo]  # Obtém o valor correto do grupo correspondente
        
        if tipo == 'NEWLINE':
            linha += 1
            continue
        elif tipo == 'SKIP':
            continue
        elif tipo == 'STRING':
            valor = valor[1:-1]  # Remove as aspas
        
        if tipo != 'ERRO':
            token = (tipo, valor, linha, m.span())
            reconhecidos.append(token)
        else:
            print(f"Símbolo ilegal na linha {linha}: {valor}")
            
    return reconhecidos

def main():
    query = '''select ?nome ?desc where {
            ?s a dbo:MusicalArtist.
            ?s foaf:name "Chuck Berry"@en .
            ?w dbo:artist ?s.
            ?w foaf:name ?nome.
            ?w dbo:abstract ?desc
            } LIMIT 1000'''

    for tok in tokenize(query):
        print(tok)

if __name__ == "__main__":
        main()
