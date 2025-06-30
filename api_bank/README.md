# API Bank - Backend FastAPI

Este é o backend de um sistema bancário simples, desenvolvido em FastAPI, com autenticação JWT, controle de usuários, contas e transações.

---

## **Requisitos**

- Python 3.10+
- [Poetry](https://python-poetry.org/)
- SQLite (já incluso no projeto)

---

## **Instalação**

1. **Clone o repositório:**
   ```sh
   git clone <url-do-repo>
   cd api_bank
   ```

2. **Instale as dependências:**
   ```sh
   poetry install
   ```

3. **(Opcional) Inicialize o banco de dados:**
   ```sh
   poetry run python init_db.py
   ```

---

## **Rodando o Backend**

```sh
poetry run uvicorn src.main:app --reload
```

A API estará disponível em:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

A documentação interativa estará em:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## **Autenticação**

A API utiliza autenticação JWT.  
Para acessar rotas protegidas, siga os passos:

1. **Faça login (ou registre um usuário) para obter o token.**
2. **Use o token no header das requisições:**
   ```
   Authorization: Bearer SEU_TOKEN_AQUI
   ```

---

## **Exemplo de uso (Thunder Client, Insomnia, Postman, cURL)**

### **Login**
```http
POST /auth/login
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```
**Resposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### **Listar usuários**
```http
GET /users/
Authorization: Bearer SEU_TOKEN_AQUI
```

### **Criar conta**
```http
POST /accounts/
Authorization: Bearer SEU_TOKEN_AQUI
Content-Type: application/json

{
  "campo1": "valor",
  ...
}
```

---

## **Estrutura do Projeto**

```

---

## **Observações**

- O backend está pronto para integração com frontend (exemplo: React, Vue, etc).
- O banco de dados padrão é SQLite, mas pode ser adaptado para outros bancos facilmente.
- O sistema utiliza autenticação JWT segura, com expiração de token.

---

## **Dúvidas ou problemas?**

Abra uma issue ou entre em contato!

---