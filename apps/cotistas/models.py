# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from apps import db, login_manager



class Cotistas(db.Model, UserMixin):
    __tablename__ = 'Cotistas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    cpf = db.Column(db.String(64), unique=True)
    birth = db.Column(db.String(64))
    telephone = db.Column(db.String(64))
    cell = db.Column(db.String(64))
    active = db.Column(db.Boolean)
    code = db.Column(db.String(64))
    income_tax = db.Column(db.Boolean)

    enderecos = relationship("Endereco", back_populates="cotista")

class Endereco(db.Model, UserMixin):
    __tablename__ = 'Endereco'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(128))
    number = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    cep = db.Column(db.String(64))
    cotistas_id = db.Column(db.Integer, db.ForeignKey('Cotistas.id'))

    cotista = relationship("Cotistas", back_populates="enderecos")



def add_cotista(name, email, cpf, birth, telephone, cell, active, code, income_tax):
    # Cria uma instância de Cotistas com os dados fornecidos
    new_cotista = Cotistas(
        name=name,
        email=email,
        cpf=cpf,
        birth=birth,
        telephone=telephone,
        cell=cell,
        active=active,
        code=code,
        income_tax=income_tax
    )
    # Adiciona o novo cotista à sessão
    db.session.add(new_cotista)
    try:
        # Faz commit na sessão para salvar o novo cotista no banco de dados
        db.session.commit()
        print(f"Cotista {name} adicionado com sucesso.")
    except Exception as e:
        # Se houver um erro, faz rollback na sessão
        db.session.rollback()
        print(f"Erro ao adicionar cotista: {e}")



def list_all_cotistas():
    try:
        # Consulta todos os registros da tabela Cotistas
        cotistas = Cotistas.query.all()
        return cotistas
    except Exception as e:
        print(f"Erro ao listar cotistas: {e}")
        return []

def view_id_cotistas(id):
    try:
        # Busca o cotista pelo ID
        cotista = Cotistas.query.get(id)
        return cotista
    except Exception as e:
        print(f"Erro ao buscar cotista por ID: {e}")
        return None


def add_endereco(cotistas_id: int, street: str, number: str, city: str, state: str, cep: str) -> bool:
    cotista = view_id_cotistas(cotistas_id)
    if not cotista:
        print(f"Cotista com ID {cotistas_id} não encontrado.")
        return False

    new_endereco = Endereco(
        street=street,
        number=number,
        city=city,
        state=state,
        cep=cep,
        cotistas_id=cotistas_id
    )
    db.session.add(new_endereco)
    try:
        db.session.commit()
        print(f"Endereço para o cotista {cotista.name} adicionado com sucesso.")
        return True
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao adicionar endereço: {e}")
        return False



