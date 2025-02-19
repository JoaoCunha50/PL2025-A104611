# TPC2 - Trabalho Prático semana 2 (19/02/2024)

- **Nome:** João Manuel Machado da Cunha
- **Nº:** A104611
- **Foto:**

![foto](https://avatars.githubusercontent.com/u/131183584?v=4)

## Resumo
Este script foi desenvolvido no âmbito da UC de Processamento de Linguagens para processar um arquivo CSV contendo informações sobre obras musicais. O programa analisa o conteúdo do arquivo e gera três relatórios diferentes:

- Lista ordenada alfabeticamente de compositores
- Distribuição de obras por período musical
- Lista de títulos organizados por período

#### Componentes Principais:
- **Parser CSV**: Processa o arquivo CSV usando expressões regulares para lidar corretamente com campos que contêm aspas e ponto e vírgula
- **Geração de Relatórios**: Cria três arquivos de texto separados com as informações processadas
- **Organização de Dados**: Utiliza estruturas de dados como sets e dicionários para organizar e classificar as informações

## Lista de Resultados:
Os seguintes arquivos são gerados pelo script:
- [compositores.txt](compositores.txt) - Lista ordenada de todos os compositores
- [obras_por_periodo.txt](obras_por_periodo.txt) - Contagem de obras por período musical
- [titulos_por_periodo.txt](titulos_por_periodo.txt) - Títulos das obras organizados por período
- [parser.py](parser.py) - O script de leitura e processamento do csv
- [obras.csv](obras.csv) - O csv com os dados do TPC

## Utilização:
Para executar o script, utilize o seguinte comando no terminal:
```
python3 parser.py
```