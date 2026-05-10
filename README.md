🏦 API Bancária com FastAPI

Uma API RESTful assíncrona para gerenciamento de operações bancárias, incluindo depósitos, saques e extratos de contas correntes, com autenticação JWT segura.

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=json-web-tokens&logoColor=white)

## 📋 Descrição

Este projeto implementa uma API bancária moderna utilizando FastAPI, oferecendo operações assíncronas eficientes para depósitos e saques, com validações robustas e segurança através de tokens JWT. Desenvolvido como desafio técnico para demonstrar boas práticas em desenvolvimento de APIs backend.

## ✨ Funcionalidades

- 🔐 **Autenticação JWT**: Sistema seguro de login com tokens JWT
- 💰 **Gerenciamento de Contas**: Criação e gerenciamento de contas correntes
- 📈 **Transações**: Depósitos e saques com validações automáticas
- 📊 **Extrato**: Visualização completa do histórico de transações
- ✅ **Validações**: Prevenção de valores negativos e saldos insuficientes
- 📚 **Documentação Automática**: OpenAPI/Swagger integrada

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework web assíncrono para APIs REST
- **Python 3.12+**: Linguagem de programação
- **Pydantic**: Validação de dados e serialização
- **JWT**: Autenticação baseada em tokens
- **PassLib**: Hashing seguro de senhas
- **Uvicorn**: Servidor ASGI

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.12 ou superior
- Git

### Passos para Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/api-bancaria.git
   cd api-bancaria
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   uvicorn main:app --reload
   ```

A API estará disponível em: http://127.0.0.1:8000

## 📖 Documentação da API

### Endpoints Principais

#### 🔓 Público
- `POST /token` - Autenticação e obtenção de token JWT
- `POST /accounts` - Criação de nova conta corrente

 🔒 Autenticado (requer Bearer Token)
- `POST /transactions` - Criar nova transação (depósito/saque)
- `GET /accounts/{account_id}/statement` - Obter extrato da conta

 Documentação Interativa

Acesse http://127.0.0.1:8000/docs para a documentação interativa Swagger UI, onde você pode testar todos os endpoints diretamente no navegador.

🔧 Exemplos de Uso

1. Criar uma conta
```bash
curl -X POST http://127.0.0.1:8000/accounts
```

**Resposta:**
```json
{
  "id": 1,
  "balance": 0.0,
  "transactions": []
}
```

 2. Fazer login
```bash
curl -X POST "http://127.0.0.1:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user1&password=pass1"
```

**Resposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

3. Criar um depósito
```bash
curl -X POST "http://127.0.0.1:8000/transactions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "type": "deposit",
    "amount": 100.0,
    "account_id": 1
  }'
```

4. Verificar extrato
```bash
curl -X GET "http://127.0.0.1:8000/accounts/1/statement" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

🔒 Segurança

- **JWT Tokens**: Autenticação stateless com expiração configurável
- **Validações**: Verificação de saldos e valores positivos
- **Hashing**: Senhas armazenadas com PBKDF2-SHA256
- **HTTPS Recomendado**: Para produção, utilize HTTPS

🏗️ Arquitetura

```
api-bancaria/
├── main.py          # Aplicação principal FastAPI
├── models.py        # Modelos Pydantic
├── auth.py          # Lógica de autenticação JWT
├── requirements.txt # Dependências Python
├── .gitignore       # Arquivos ignorados pelo Git
└── README.md        # Este arquivo
```

🧪 Testes

Para testar a API, utilize as ferramentas:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **cURL**: Exemplos fornecidos acima
- **Postman/Insomnia**: Importe a documentação OpenAPI

🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

