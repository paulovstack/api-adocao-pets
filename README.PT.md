# API de Adoção de Pets

API REST desenvolvida com **FastAPI** para gestão de um processo de adoção de animais: cadastro de animais, cadastro de adotantes e registro de adoções, vinculando cada pet ao seu novo tutor.

## Funcionalidades

- Cadastro de animais (nome, raça, sexo, idade), com status de adoção automático ("Disponível")
- Cadastro de adotantes (nome, CPF, idade, e-mail)
- Registro de adoção, vinculando um animal a um adotante
- Bloqueio de adoção duplicada: um animal já adotado não pode ser adotado novamente
- Consulta de animais, adotantes e adoções já registrados
- Tratamento de erros com códigos HTTP corretos (404 para recurso não encontrado, 409 para conflito)

## Tecnologias

- Python 3
- **FastAPI** — framework para construção da API
- **Pydantic** — validação e tipagem dos dados de entrada
- **Uvicorn** — servidor ASGI para rodar a aplicação

## Como executar

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Com o servidor rodando, a documentação interativa da API fica disponível automaticamente em:

```
http://127.0.0.1:8000/docs
```

## Endpoints

### Animais

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/consultar/animal` | Lista todos os animais cadastrados |
| `POST` | `/registrar/animal` | Cadastra um novo animal |

**Corpo da requisição — `POST /registrar/animal`:**
```json
{
  "nome": "Rex",
  "raca": "Vira-lata",
  "sexo": "M",
  "idade": 2
}
```

### Adotantes

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/consultar/adotante` | Lista todos os adotantes cadastrados |
| `POST` | `/registrar/adotante` | Cadastra um novo adotante |

**Corpo da requisição — `POST /registrar/adotante`:**
```json
{
  "nome": "Maria Silva",
  "cpf": "000.000.000-00",
  "idade": 30,
  "email": "maria@email.com"
}
```

### Adoções

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/consultar/adocao` | Lista todas as adoções registradas |
| `POST` | `/registrar/adocao` | Registra a adoção de um animal por um adotante |

**Corpo da requisição — `POST /registrar/adocao`:**
```json
{
  "animal_id": 1,
  "adotante_id": 1
}
```

Retorna `404` se o animal ou o adotante informado não existirem, e `409` se o animal já tiver sido adotado anteriormente.

## Conceitos praticados

- Construção de uma API REST do zero com FastAPI
- Validação de dados de entrada com Pydantic (`BaseModel`)
- Tratamento de erros HTTP apropriado com `HTTPException` (404 e 409), em vez de retornar sempre `200 OK`
- Modelagem de relacionamento entre entidades (animal, adotante e adoção)
- Regras de negócio aplicadas na API (impedir readoção de um animal já adotado)

## Próximos passos

- Persistência de dados em banco de dados (hoje os dados ficam apenas em memória, e se perdem ao reiniciar o servidor)
- Validação de CPF e e-mail
- Rota para cancelar/desfazer uma adoção
