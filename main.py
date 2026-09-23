from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

anim = []
adot = []
adoc = []

class Animais(BaseModel):
    id: Optional[int] = None
    nome: str
    raca: str
    sexo: str
    idade: int
    status_ad: Optional[str] = None
    
    

class Adotantes(BaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str
    idade: int
    email: str


class Adocao(BaseModel):
    animal_id: int
    adotante_id: int

def listar_status():
    status_dog = ["Disponível",     "Adotado"]
    return status_dog

@app.get("/consultar/animal")
def lista_animal():
    return anim

@app.get("/consultar/adotante")
def lista_adotante():
    return adot

@app.get("/consultar/adocao")
def lista_adocao():
    return adoc

@app.post("/registrar/animal")
def registrar_animal(dados: Animais):
    novo_id = len(anim) + 1

    horario_atual = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    novo_animal = {
        "id": novo_id,
        "nome": dados.nome.upper(),
        "raca": dados.raca.upper(),
        "sexo": dados.sexo.upper(),
        "idade": dados.idade,
        "entrada": horario_atual,
        "status_ad": listar_status()[0]
    }

    anim.append(novo_animal)
    print(f"Data do registro: {horario_atual}")
    return {"Status": "Sucesso", "mensagem": f"Animal {dados.nome} da raça {dados.raca} foi registrado!"}

@app.post("/registrar/adotante")
def registrar_adotante(dados: Adotantes):
    novo_id = len(adot) + 1

    horario_atual = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    novo_adotante = {
        "id": novo_id,
        "nome": dados.nome.upper(),
        "cpf": dados.cpf,
        "idade": dados.idade,
        "email": dados.email,
        "entrada": horario_atual
    }
    adot.append(novo_adotante)
    print(f"Data do registro: {horario_atual}")
    return {"Status": "Sucesso", "mensagem": f"Adotante {dados.nome} cujo CPF:{dados.cpf} foi registrado!"}

@app.post("/registrar/adocao")
def registrar_adocao(dados: Adocao):

    animal_encontrado = next((a for a in anim if a["id"] == dados.animal_id), None)
    adotante_encontrado = next((ad for ad in adot if ad ["id"] == dados.adotante_id), None)

    if not animal_encontrado or not adotante_encontrado:
        print("Adoção não pode ser realizada")
        raise HTTPException(status_code=404, detail="Animal ou Adotante não cadastrado.")

    animal_encontrado["status_ad"] = listar_status()[1]
    horario_atual = datetime.now().strftime("%y-%m-%d %H:%M:%S")


    nova_adocao = {
        "id_adocao": len(adoc) + 1,
        "animal": animal_encontrado,
        "adotante": adotante_encontrado,
        "data_adocao": horario_atual
    }

    adoc.append(nova_adocao)
    return {"Status": "Sucesso", "mensagem": f"O pet {animal_encontrado['nome']} agora pertence a {adotante_encontrado['nome']}!"}

    




