# **Mini Blockchain**

Um projeto simples que implementa uma blockchain local em Python. Este projeto é educacional e demonstra os conceitos básicos por trás de uma blockchain, incluindo:
- Encadeamento de blocos.
- Hashing dos dados.
- Validação de Proof of Work (PoW).
- Verificação de integridade da cadeia.

---

## **Características**
- Criação de blocos contendo dados e hashes vinculados ao bloco anterior.
- Implementação de **Proof of Work (PoW)** para mineração de blocos.
- Validação da cadeia de blocos para garantir a integridade dos dados.
- Estrutura modular para facilitar a expansão e manutenção.

---

## **Pré-requisitos**

Certifique-se de ter os seguintes requisitos antes de começar:

- **Python 3.8+** instalado no seu sistema.
- Ambiente virtual configurado (opcional, mas recomendado).

---


## **Estrutura do Projeto**

mini_blockchain/
│
├── blockchain/                  # Módulo principal da blockchain
│   ├── __init__.py              # Inicialização do módulo
│   ├── block.py                 # Classe Block
│   ├── blockchain.py            # Classe Blockchain
│   └── utils.py                 # Funções utilitárias
│
├── tests/                       # Testes automatizados
│   ├── __init__.py              # Inicialização do módulo de testes
│   ├── test_block.py            # Testes para a classe Block
│   ├── test_blockchain.py       # Testes para a classe Blockchain
│   └── test_utils.py            # Testes para as funções utilitárias
│
├── scripts/                     # Scripts executáveis
│   └── run_blockchain.py        # Script principal para rodar o projeto
│
├── requirements.txt             # Dependências do projeto
├── .gitignore                   # Arquivo para ignorar arquivos desnecessários no Git
├── README.md                    # Documentação do projeto
└── LICENSE                      # Licença do projeto (opcional)
