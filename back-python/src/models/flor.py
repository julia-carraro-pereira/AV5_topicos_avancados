from config import *
class Flor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.String(200), nullable=False)
    cor = db.Column(db.String(200), nullable=True)
    simbologia = db.Column(db.String(200), nullable=False)
    
    

    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "preco":self.preco,
            "cor":self.cor,
            "simbologia":self.simbologia
            
            }
