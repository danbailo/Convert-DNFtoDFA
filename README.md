## Converter Autômatos Finitos Não-determinísticos para Automatos Finitos determinísticos

### Pré-requisitos
* python3
### Observações
* Considerar os colchetes '[ ]' como sendo o símbolo para representar um conjunto, visto que este é representado com chaves '{ }'.
* Por exemplo: Seguindo a observação acima, o conjunto vazio será representado por [ ] .
### Executar
Basta executar <code>$ python3 main.py nome_do_arquivo.txt</code><br>
Onde o arquivo "nome_do_arquivo.txt" deve seguir o seguinte formato para o autômato representado
pelo diagrama de transições a seguir:

<image src="afn.png"></image>

o nome_do_arquivo.txt terá de seguir o seguinte formato:

    'q1','q2','q3'
    ab
    ['q3'],[],        ['q2']
    [],['q2','q3'], ['q3']
    [] ,['q1']       , []
    'q1'
    'q1'
Onde a<br>
<b>Primeira linha: </b>Indica o nome dos estados<br>
<b>Segunda linha: </b>Indica o alfabeto<br>
<b>Terceira, quarta e quinta linha: </b>Indicando a matriz delta considerando a primeira coluna como a transição após a leitura da palavra vazia<br>
<b>Obs:</b> Considerando que este autômato possui três estados, a matriz terá tres linhas, logo, as duas últimas linhas sempre serão estado inicial e estado final, respectivamente.<br>
<b>Sexta linha: </b> Indica o estado inicial<br>
<b>Sétima linha: </b> Indica os estados finais<br>

Nesta pasta contém dois automatos([Automato 1](automato1.txt) e [Automato 2](automato1.txt)) no formato apresentado acima.
O [Automato 1](automato1.txt) é o exemplo do diagrama mostrado acima. Ao executar <code>$ python3 main.py automato1.txt</code><br>
A saída do programa será:


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
