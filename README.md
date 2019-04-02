## Converter Autômatos Finitos Não-determinísticos para Automatos Finitos determinísticos

### Pré-requisitos
* python3
### Executar
Basta executar <code>python3 main.py nome_do_arquivo.txt</code><br>
Onde o arquivo "nome_do_arquivo.txt" deve seguir o seguinte formato para o autômato representado
pelo diagrama de transições a seguir:

<image src="afn.png"></image>

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


	Estados:
	['[]', "['q1']", "['q2']", "['q3']", "['q1', 'q2']", "['q1', 'q3']", "['q2', 'q3']", "['q1', 'q2', 'q3']"]

	Sigma:
	['a', 'b']

	Delta:
	['[]', '[]']
	['[]', "['q2']"]
	["['q2', 'q3']", "['q3']"]
	["['q1', 'q3']", '[]']
	["['q2', 'q3']", "['q2', 'q3']"]
	["['q1', 'q3']", "['q2']"]
	["['q1', 'q2', 'q3']", "['q3']"]
	["['q1', 'q2', 'q3']", "['q2', 'q3']"]

	Estado inicial:
	['q1', 'q3']

	Estados finais:
	["['q1']", "['q1', 'q2']", "['q1', 'q3']", "['q1', 'q2', 'q3']"]
