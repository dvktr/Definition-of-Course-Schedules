# README - Organizador de Cursos

## Introdução

Este script em Python utiliza a biblioteca Z3 para resolver um problema de alocação de cursos em slots de horários, considerando restrições específicas. O objetivo é determinar uma alocação satisfatória dos cursos dentro dos slots disponíveis, respeitando as restrições fornecidas.

## Problemática
### Definição dos Horários de Cursos em um Evento
Um evento vai oferecer k minicursos de uma hora de duração cada. Dessa forma, os organizadores do evento vão definir os horários em slots de uma hora de duração, por exemplo, 8:00-9:00, 9:00-10:00, 10:00-11:00, e assim por diante. Os participantes podem se inscrever em mais de um minicurso. Logo, a organização do evento deseja agendar os horários dos minicursos de forma a atender as inscrições dos participantes, ou seja, minicursos que possuem inscrições de um mesmo participante não podem ser ofertados no mesmo horário.

Por conta das condições mencionadas, os organizadores querem saber se é possível reservar apenas m slots para ofertar todos os cursos respeitando as inscrições dos participantes. Além do número de cursos k e do número de horários m, também já temos acesso ao conjunto P com os pares de cursos com inscrições em comum. Ou seja, se o par (i, j) está em P, então o curso i e o curso j possuem inscrições em comum.

Usando satisfatibilidade da lógica proposicional, você deve criar um programa que, dados como entrada o número de cursos k, o número de slots m e o conjunto P de minicursos com inscrições em comum, determine se é possível agendar m horários diferentes para ofertar os k minicursos de forma que minicursos com participantes em comum não sejam ofertados no mesmo horário. Caso seja possível, seu programa também deve dizer o slot de tempo que cada curso deve ser ofertado.

Veja um exemplo de entrada e de saída a seguir. As primeiras linhas representam a identificação e nome de cada minicurso. Por exemplo, o minicurso de HTML é identificado pelo número 1. Depois temos o número de slots que é 3. Em seguida, os pares de números representam os cursos que possuem alunos em comum. Por exemplo, a linha com 1 2 representa que os minicursos HTML e PHP têm participantes em comum inscritos. Na saída, temos o horário em que cada curso foi definido. Por exemplo, o curso 2 ficou definido no terceiro slot. Seu programa deve funcionar para qualquer entrada que tenha essas informações.
```
Entrada:
Minicursos:
1 HTML
2 PHP
3 MySQL
4 Swift
Slots: 3
Pares de minicursos com inscrições em comum:
1 2
2 3
2 4
3 4

Saída:
1 s1
2 s3
3 s1
4 s2
```

Use variáveis atômicas da forma X ᶜ,ˢ para representar que o minicurso é ofertado no slot s. Por exemplo, a cláusula ¬(x_1,1 ∧ x_2,1) representa que os cursos 1 e 2 não podem ser realizados juntos no primeiro slot. Dessa forma, você vai construir uma fórmula da lógica proposicional que representa as restrições do problema e, em seguida, vai verificar se essa fórmula é satisfatível. Se a fórmula for satisfatível, a definição dos horários dos minicursos deve ser extraída de uma valoração que deixa a fórmula verdadeira. Veja que, a partir de uma entrada, temos que construir uma fórmula da lógica proposicional que é satisfatível se e somente se for possível usar m slots para ofertar os minicursos respeitando as inscrições em comum. Portanto, se a fórmula for insatisfatível, então não é possível usar apenas m slots. Além disso, se a fórmula for satisfatível, então a valoração que satisfaz a fórmula deve ter as informações necessárias para definir os slots dos minicursos. Você deve construir sua fórmula a partir das restrições descritas em linguagem natural a seguir:

 1. Cada minicurso deve ser ofertado em pelo menos um slot.
 2. Cada minicurso deve ser ofertado em no máximo um slot.
 3. Minicursos com inscrições em comum não podem ser ofertados no mesmo slot.
     
A partir dessas restrições, você deve construir uma fórmula que as representa. Observe que as fórmulas que serão construídas dependem da entrada, ou seja, da quantidade de cursos k, da quantidade de slots m e do conjunto P. Em seguida, você deve verificar se essa fórmula é satisfatível. Você deve usar a ferramenta PySAT para criar as fórmulas e verificar a satisfatibilidade (PySAT trocada por Z3).

## Processos

### 1. Leitura de Arquivos de Entrada

O script permite a leitura de informações sobre os cursos e restrições a partir de arquivos de entrada localizados na pasta "inputs". O arquivo de entrada deve seguir um formato específico, incluindo informações sobre os cursos, número de slots disponíveis e pares de cursos com inscrições em comum.

### 2. Extração de Dados

As funções `openArchive`, `getCourses`, `getSlots`, e `getPairs` são responsáveis por extrair as informações do arquivo de entrada.
- ```python
  from z3 import *
  from utils.CourseInformationReader import *

  archive_name = "input.txt"
  slots = getSlots(archive_name)
  courses = getCourses(archive_name)
  common_inscriptions_courses = getPairs(archive_name)

### 3. Representação Lógica das Restrições

`convertCommonEnrollmentsToPropositionalLogic`: Dois cursos com inscrições comuns não podem estar no mesmo slot. Consiste em negar cada combinação de cursos de inscrição comuns no mesmo slot.
![LOGIC](https://github.com/dvktr/Definition-of-Course-Schedules/assets/61356918/c3607b67-9dfe-4d39-8aa9-da17d439aba5)

`atLeastInOneSlot`: Um curso tem que estar em pelo menos um slot.
![LOGIC](https://github.com/dvktr/Definition-of-Course-Schedules/assets/61356918/e166e88b-4066-4828-abb7-10920105eb1c)

`maxInOneSlot`: Um curso não pode estar em mais do que um slot.
![LOGIC](https://github.com/dvktr/Definition-of-Course-Schedules/assets/61356918/08c323f4-aaf6-4c19-a6ff-95985530d3cc)

Aplicando todas as restrições
- ```python
  for course_pair in common_inscriptions_courses:
    if course_pair == common_inscriptions_courses[0]:
        common_inscriptions_courses_restrictions = convertCommonEnrollmentsToPropositionalLogic(course_pair[0], course_pair[1], slots)
    else:
        common_inscriptions_courses_restrictions = And(common_inscriptions_courses_restrictions, convertCommonEnrollmentsToPropositionalLogic(course_pair[0], course_pair[1], slots))

    solver = Solver()
    
    at_least_in_one_slot_restrictions = None
    max_in_one_slot_restrictions = None
    
    for course_number in range(1, len(courses) + 1):
        if course_number == 1:
            at_least_in_one_slot_restrictions = atLeastInOneSlot(course_number, slots)
            max_in_one_slot_restrictions = maxInOneSlot(course_number, slots)
        else:
            at_least_in_one_slot_restrictions = And(at_least_in_one_slot_restrictions, atLeastInOneSlot(course_number, slots))
            max_in_one_slot_restrictions = And(max_in_one_slot_restrictions, maxInOneSlot(course_number, slots))
    
    all_restrictions = And(And(max_in_one_slot_restrictions, at_least_in_one_slot_restrictions), common_inscriptions_courses_restrictions)

### 4. Resolução do Problema

O script utiliza um solver Z3 para verificar a satisfatibilidade das restrições e encontrar uma solução para o problema de alocação dos cursos nos slots disponíveis. Aqui, adiciona-se a fórmula ao solver e verifica-se a sua compatibilidade. Se for satisfatória, é impressa a disciplina que está em que slot, se não, é impressa uma mensagem de erro.
- ```python
    solver.add(all_restrictions)

    isSatisfatible = solver.check() == sat and slots > 0
    
    if isSatisfatible:
        model = solver.model()
    
        truly_course_variables = []
    
        for variable in model:
            if model[variable]:
                truly_course_variables.append(str(variable))
    
        for course_variable in truly_course_variables:
            splitted_course_variable = course_variable.split("_")
            course_number = int(splitted_course_variable[1])
            slot_number = int(splitted_course_variable[2])
            course_name = courses[course_number]
    
            print(f"O curso {course_name}", end=' ')
            print(f'ficará no slot de horário {slot_number}\n')
    else:
        print("É impossível organizar os cursos com a quantidade de slots e restrições fornecidas.")

## Utilização

1. No arquivo "input.txt", localizado dentro da pasta iputs, coloque seu problema no formato do exemplo a seguir:
-     # Minicursos:
      1 Javascript
      2 Python
      3 Ruby 
      4 Flutter  
      5 SQL
      6 React Native
      # Slots: 2
      # Pares de minicursos com inscrições em comum:
      1 2
      2 3
      2 5
      3 4
      3 6
      5 6
  
  
2. Execute o script:

    ```bash
    python main.py
    ```

## Requisitos

- Python 3.x
- Biblioteca Z3 (`pip install z3-solver`)

## Observações

- Certifique-se de que os arquivos de entrada seguem o formato esperado.
- O script utiliza a biblioteca Z3 para resolver o problema de satisfatibilidade lógica, logo é necessário fazer a instalação da mesma.

A disposição para quaisquer dúvidas.
