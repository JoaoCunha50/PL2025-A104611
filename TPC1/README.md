# TPC1

## Resumo - somadorOnOff
Este script foi realizado no âmbito da UC de Processamento de Linguagens e implementa um somador simples com uma funcionalidade de interruptor on/off. O principal objetivo do script é realizar operações de adição de sequências de dígitos com base no estado do interruptor. Quando o interruptor está ligado, o somador realiza a adição e retorna o resultado. Quando o interruptor está desligado, o somador não realiza nenhuma operação de adição, e procede normalmente para as outras situações (como o caso do '=').

## Componentes Principais:
 - **Somador**: Contém métodos para realizar a adição e gerir o estado on/off do interruptor.
 - **Estado do Interruptor**: Uma variável booleana que determina se o somador está ativo ou inativo.
 - **Método de Adição**: Um método que recebe uma linha do stdin com sequências de dígitos e retorna a sua soma se o interruptor estiver ligado.
 - **Gestão de Estado**: Métodos para ligar ou desligar o interruptor.

## **Lista de Resultados**: 
   - [somadorOnOff.py](./TPC1/somadorOnOff.py)

## Utilização:
 - Utilizar o seguinte comando:
    ```sh
    python3 somadorOnOff.py
    ```
 - De seguida introduzir o input que desejar! Por exemplo:
    ```
    olasjdahfa123 -3 oFf 123 oN 276
    ```