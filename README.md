## Converter Autômatos Finitos Não-determinísticos para Automatos Finitos determinísticos

### Pré-requisitos
* python3
### Executar
Basta executar <code>python3 fdn2fda.py [fdn.txt]</code>
o arquivo fdn.txt deve seguir o seguinte formato
por exemplo, para o seguinte automato

<image src="fdn.png"></image>

o fdn.txt terá de ser:

    'q1','q2','q3'
    ab
    ['q3'],[],        ['q2']
    [],['q2','q3'], ['q3']
    [] ,['q1']       , []
    'q1'
    'q1'
Onde:<br>
<b>Primeira linha: </b>indica o nome dos estados<br>
<b>Segunda linha: </b>indica o alfabeto<br>
<b>Terceira, quarta e quinta linha: </b>indicando a matriz delta considerando a primeira coluna como a transição após a leitura da palavra vazia<br>
<b>Sexta linha: </b> indica o estado inicial<br>
<b>Sétima linha: </b> indica os estados finais<br>

A saída do programa para essa entrada será:

    estados:
    ['[]', "['q1']", "['q2']", "['q3']", "['q1', 'q2']", "['q1', 'q3']", "['q2', 'q3']", "['q1', 'q2', 'q3']"]
    sigma:
    ['a', 'b']
    delta:
    ['[]', '[]']
    ["['q2']", '[]']
    ["['q3']", "['q2', 'q3']"]
    ['[]', "['q1', 'q3']"]
    ["['q2', 'q3']", "['q2', 'q3']"]
    ["['q2']", "['q1', 'q3']"]
    ["['q3']", "['q1', 'q2', 'q3']"]
    ["['q2', 'q3']", "['q1', 'q2', 'q3']"]
    inicial:
    ['q1', 'q3']
    finais
    ["['q1']", "['q1', 'q2']", "['q1', 'q3']", "['q1', 'q2', 'q3']"]
