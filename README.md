# AC Blockchain

**AC Blockchain** é uma implementação de blockchain projetada para demonstrar os principais conceitos da tecnologia blockchain, incluindo descentralização, mecanismos de consenso e segurança criptográfica. Este projeto foi criado para fins educacionais e pode servir como base para aplicativos blockchain mais avançados.

## Recursos

- **Rede descentralizada**: uma rede ponto a ponto que permite que os nós se comuniquem e compartilhem dados sem uma autoridade central.
- **Mecanismo de consenso**: implementa um algoritmo de prova de trabalho (PoW) para validar e adicionar novos blocos ao blockchain.
- **Segurança criptográfica**: usa hash SHA-256 para garantir a integridade e a segurança dos dados.
- **Sistema de transações**: oferece suporte a transações básicas entre os participantes da rede.
- **Livro-razão imutável**: uma vez que um bloco é adicionado ao blockchain, ele não pode ser alterado, garantindo a imutabilidade dos dados.

### Uso

- **Criar uma transação**:
  Usar a API ou CLI para criar e transmitir transações para a rede.

- **Mine um bloco**:
  Iniciar o processo de mineração para adicionar transações pendentes a um novo bloco.

- **Visualizar blockchain**:
  Ver o estado atual do blockchain para ver todos os blocos e transações.

### Pontos de extremidade da API

- `GET /blocks`: Recuperar o blockchain inteiro.
- `POST /transactions`: Criar uma nova transação.
- `GET /mine`: Minerar um novo bloco.
- `POST /nodes/register`: Registrar um novo nó na rede.
- `GET /nodes/resolve`: Resolver conflitos e obter consenso entre os nós.

### Solicitações de exemplo

- Crie uma transação:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
"sender": "Alice",
"recipient": "Bob",
"amount": 50
}' http://localhost:3000/transactions
```

- Minere um bloco:

```bash
curl http://localhost:3000/mine
```

- Visualize o blockchain:

```bash
curl http://localhost:3000/blocks
```

## Licença

Este projeto é licenciado sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## Inspirado no whitepaper original do Bitcoin por Satoshi Nakamoto.

## Contato

- **André Carvalho**
- GitHub: [carvalhoandre](https://github.com/carvalhoandre)
- E-mail: [carvalho.devel@gmail.com](mailto:carvalho.devel@gmail.com)
