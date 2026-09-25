# Pet Adoption API

REST API developed with **FastAPI** for managing a pet adoption process: animal registration, adopter registration, and adoption records, linking each pet to its new owner.

## Features

* Animal registration (name, breed, sex, age), with automatic adoption status ("Available")
* Adopter registration (name, CPF, age, email)
* Adoption registration, linking an animal to an adopter
* Duplicate adoption prevention: an already adopted animal cannot be adopted again
* Query registered animals, adopters, and adoptions
* Error handling with appropriate HTTP status codes (404 for resource not found, 409 for conflict)

## Technologies

* Python 3
* **FastAPI** — framework for building the API
* **Pydantic** — data validation and input typing
* **Uvicorn** — ASGI server for running the application

## How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Once the server is running, the API's interactive documentation is automatically available at:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Animals

| Method | Route               | Description                  |
| :----- | :------------------ | :--------------------------- |
| `GET`  | `/consultar/animal` | Lists all registered animals |
| `POST` | `/registrar/animal` | Registers a new animal       |

**Request body — `POST /registrar/animal`:**

```json
{
  "nome": "Rex",
  "raca": "Vira-lata",
  "sexo": "M",
  "idade": 2
}
```

### Adopters

| Method | Route                 | Description                   |
| :----- | :-------------------- | :---------------------------- |
| `GET`  | `/consultar/adotante` | Lists all registered adopters |
| `POST` | `/registrar/adotante` | Registers a new adopter       |

**Request body — `POST /registrar/adotante`:**

```json
{
  "nome": "Maria Silva",
  "cpf": "000.000.000-00",
  "idade": 30,
  "email": "maria@email.com"
}
```

### Adoptions

| Method | Route               | Description                                       |
| :----- | :------------------ | :------------------------------------------------ |
| `GET`  | `/consultar/adocao` | Lists all registered adoptions                    |
| `POST` | `/registrar/adocao` | Registers the adoption of an animal by an adopter |

**Request body — `POST /registrar/adocao`:**

```json
{
  "animal_id": 1,
  "adotante_id": 1
}
```

Returns `404` if the specified animal or adopter does not exist, and `409` if the animal has already been adopted.

## Concepts Practiced

* Building a REST API from scratch with FastAPI
* Input data validation with Pydantic (`BaseModel`)
* Appropriate HTTP error handling with `HTTPException` (404 and 409), instead of always returning `200 OK`
* Modeling relationships between entities (animal, adopter, and adoption)
* Applying business rules in the API (preventing an animal from being adopted more than once)

## Next Steps

* Data persistence using a database (currently, data is stored only in memory and is lost when the server restarts)
* CPF and email validation
* Route to cancel or undo an adoption
