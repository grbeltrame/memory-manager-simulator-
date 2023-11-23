Trabalho de Sistemas Operacionais:

------------      Simulador de Gerenciador de Memória         ------------ 

Integrantes:

Dário Chen
Estêvão Mori
Giovana Beltrame
João Pedro Sá
Júlia Câmara


Foram feitos 8 arquivos contendo as classes para o gerenciamento de memória, sendo eles:

gerenciador.py      (Gerenciador de Memória)
memoriaprincipal.py (Memória Principal)
memorisecundaria.py (Memória Secundária)
processo.py         (Processo)
tabelaquadros.py    ("Tabela" com os quadros do Processo)
imagemprocesso.py   (Imagem do processo)
entrada.py          (Entradas da TP e também utilizadas na tabela de quadros)
swapper.py          (Swapper, em LRU)

Algumas observações sobre o código:

O print da Tabela de Páginas é feito após a suspensão ou remoção de um processo e no final do código;

O print dos Quadros dos Processos é feito após a criação de um novo processo e no final do código;

Também há prints sobre como ocorre a adição do Processo quando um Processo é adicionado, dependendo se ele é novo ou se foi suspenso.

Os prints das instruções possuem: 
Mudanças de estado do processo
Qual ação foi realizada
Se a página utilizada foi incluida ou não na TP

Para a alocação dos processos, depois de um processo ser suspenso ou terminado, o novo processo não entra no número do quadro que o processo velho deixou disponível.
Ao invés disso, o processo novo simplesmente é escrito a partir último quadro utilizado.

Como dito no documento do trabalho, temos as seguintes instruções:
!!!!!!    Houveram algumas alterações em P e C    !!!!!!

P -  instrução a ser executada pela CPU
I -  instrução de I/O
C -  criação (submissão de um processo)
R - pedido de leitura em um endereço lógico
W - pedido de escrita em um endereço lógico de um dado valor
T - terminação de processo

 número-do-processo  P  endereço-lógico 
    é uma instrução sendo executada em CPU que está em um endereço lógico 
Ex. P1 P (1011011)2 --> é uma instrução executada em CPU (pode ser uma soma ou subtração) que está no endereço lógico (1011011)2

!!!!!!  A instrução precisa ser em binário (ou seja, em 1's e 0's)


número-do-processo  I  dispositivo
    é um pedido de I/O no dado dispositivo
Ex. P1 I disco --> agora será executado uma instrução de entrada e saída pedido por P1 em disco

número-do-processo  R endereço-lógico 
    leitura no endereço lógico de memória
Ex. P1 R 1024  --> leitura no endereço lógico 1024

número-do-processo  W endereço-lógico  valor
    gravação de valor  no endereço lógico de memória
Ex. P1 W 1024  100 --> grava o valor 100 no endereço lógico 1024

número-do-processo  C tamanho-do-processo
    pedido de criação de um processo cuja imagem tem um determinado tamanho
Ex. P1 C 320  --> cria P1 com 320 bytes

!!!!!!    O tamanho do processo é unicamente em bytes para facilitar a manipulação 


número-do-processo T
    terminação do processo
Ex. P1 T --> processo P1 termina