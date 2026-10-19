from config import *
from models.flor import Flor

def criar_flor(data):
    # criar uma flor
    flor = Flor(
        nome=data['nome'],
        preco=data['preco'],
        cor=data['cor'],
        simbologia=data.get('simbologia')
    )
    
    # salvar no banco de dados
    db.session.add(flor)
    db.session.commit()
    
    return flor

def retornar_flor():
    # buscar todas as flores no 
    # banco de dados
    flor = Flor.query.all()
    
    return flor
