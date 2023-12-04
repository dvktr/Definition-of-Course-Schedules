# README - Organizador de Cursos

## Introdução

Este script em Python utiliza a biblioteca Z3 para resolver um problema de alocação de cursos em slots de horários, considerando restrições específicas. O objetivo é determinar uma alocação satisfatória dos cursos dentro dos slots disponíveis, respeitando as restrições fornecidas.

## Funcionalidades

### 1. Leitura de Arquivos de Entrada

O script permite a leitura de informações sobre os cursos e restrições a partir de arquivos de entrada localizados na pasta "inputs". O arquivo de entrada deve seguir um formato específico, incluindo informações sobre os cursos, número de slots disponíveis e pares de cursos com inscrições em comum.

### 2. Extração de Dados

As funções `open_archive`, `get_all_courses`, `get_count_slots`, e `get_time_pairs` são responsáveis por extrair as informações relevantes do arquivo de entrada.

### 3. Representação Lógica das Restrições

As funções `turn_common_inscriptions_pair_minicourses_to_propositional_logic`, `at_least_in_one_slot`, e `max_in_one_slot` convertem as restrições do problema em lógica proposicional, utilizando a biblioteca Z3.

### 4. Resolução do Problema

O script utiliza um solver Z3 para verificar a satisfatibilidade das restrições e encontrar uma solução para o problema de alocação dos cursos nos slots disponíveis.

### 5. Apresentação dos Resultados

Caso uma solução satisfatória seja encontrada, o script exibe as alocações dos cursos nos respectivos slots. Caso contrário, uma mensagem indicando a impossibilidade de organizar os cursos é apresentada.

## Utilização

1. Coloque os arquivos de entrada na pasta "inputs".
2. Execute o script fornecendo o nome do arquivo de entrada, por exemplo:

    ```bash
    python nome_do_script.py input7.txt
    ```

## Requisitos

- Python 3.x
- Biblioteca Z3 (`pip install z3-solver`)

## Observações

- Certifique-se de que os arquivos de entrada seguem o formato esperado.
- O script utiliza a biblioteca Z3 para resolver o problema de satisfatibilidade lógica.

Este README fornece uma visão geral do funcionamento do script. Certifique-se de consultar os comentários no código-fonte para obter informações adicionais sobre implementações específicas e detalhes técnicos.
