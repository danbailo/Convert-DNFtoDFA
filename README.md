## Converter automatos formais não deterministicos para automatos formais deterministicos

### pré-requisitos
* python3
### executar
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
onde a primeira linha indica o nome dos estados
a segunda indica o alfabeto
logo depois irá vir 3 linhas indicando a matriz delta
a sexta linha indica o estado inicial
e a ultima linha indica os estados finais

a saida do programa para essa entrada será:

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
