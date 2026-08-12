Estudo de autônomos



Mini-projeto de 4 dias para estudo de agentes autônomos, aprendizado por reforço, visão computacional e integração de sistemas.



Estrutura do Projeto

mini-autonomos/

├── dia1/

│   └── dia1\_grid.py       # Agente com regra determinística (Pygame)

├── dia2/                  # Aprendizado por reforço (Q-learning)

├── dia3/                  # Percepção com visão computacional (OpenCV)

├── dia4/                  # Integração: percepção + decisão

├── requirements.txt

└── README.md

Como Rodar

Pré-requisitos

Python 3.12+

Pygame

Instalação

git clone https://github.com/mateusfers/mini-autonomos.git

cd mini-autonomos

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

Execução



Para executar a primeira etapa:



python dia1/dia1\_grid.py



As demais etapas serão executadas a partir dos respectivos diretórios e arquivos conforme forem desenvolvidas.



Objetivo



O projeto é dividido em quatro etapas:



Regras determinísticas

Criar um agente que toma decisões seguindo regras fixas em um ambiente em grid.

Aprendizado por reforço

Utilizar Q-learning para que o agente aprenda quais ações tomar por meio de tentativa e erro.

Percepção artificial

Utilizar OpenCV para permitir que o agente identifique informações do ambiente, como obstáculos.

Integração

Juntar percepção e tomada de decisão, criando um agente capaz de observar o ambiente e escolher ações de forma autônoma.

Tecnologias

Python 3.12

Pygame

Gymnasium

OpenCV

