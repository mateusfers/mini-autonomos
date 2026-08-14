\# MiniAutônomos: Do Grid à Decisão Autônoma



Mini-projeto de 4 dias para estudo de agentes autônomos, aprendizado por reforço, visão computacional e integração de sistemas.



\## Estrutura do Projeto



```

mini-autonomos/

├── dia1/

│   └── dia1\_grid.py              # Agente com regra determinística (Pygame)

├── dia2/

│   └── dia2\_qlearning.py         # Aprendizado por reforço (Q-learning)

├── dia3/                         # Percepção com visão computacional (OpenCV)

├── dia4/                         # Integração: percepção + decisão

├── requirements.txt

└── README.md

```



\## Como Rodar



\### Pré-requisitos



\- Python 3.12+

\- Pygame

\- Gymnasium

\- OpenCV

\- NumPy



\### Instalação



```bash

git clone https://github.com/mateusfers/mini-autonomos.git

cd mini-autonomos

python -m venv venv

source venv/bin/activate  # No Windows: venv\\Scripts\\activate

pip install -r requirements.txt

```



\### Executar Cada Dia



Dia 1: Agente com Regra Determinística



```bash

python dia1/dia1\_grid.py

```



Dia 2: Aprendizado por Reforço (Q-learning)



```bash

python dia2/dia2\_qlearning.py

```



Dia 3: Percepção com Visão Computacional



```bash

python dia3/dia3\_opencv.py

```



Dia 4: Integração - Percepção e Decisão



```bash

python dia4/dia4\_integracao.py

```



\## Objetivo



1\. Regras determinísticas - agente segue uma regra fixa

2\. Aprendizado por reforço - agente aprende por tentativa e erro

3\. Percepção artificial - agente enxerga obstáculos

4\. Integração - percepção e decisão trabalhando juntas



\## Tecnologias



\- Python 3.12

\- Pygame (visualização)

\- Gymnasium (aprendizado por reforço)

\- OpenCV (visão computacional)

\- NumPy



\## Status



Concluído



