from config import *
from models.flor import Flor
import services.flor as flor_service


'''
--------------
LISTAR Flores
--------------
'''

'''
TESTE DE ROTA - Flor - GET

curl localhost:5000/flor
{
  "detalhes": [
    {
      "nome": "Rosas",
      "id": 1,
      "preco": "120",
      "cor": "Vermelhas",
      "simbologia": "amor"
    }
  ],
  "resultado": "ok"
}

'''

# rota para listar flores
# rota liberada para listagem pública :-) não requer JWT
@app.route('/flor', methods=['GET'])
def retornar_flor():

    # buscar as flores
    flores = flor_service.retornar_flor()
    
    # retornar a lista de flor em JSON
    return jsonify({
        "resultado":"ok",
        "detalhes":[flor.json() for flor in flores]
    })




'''
--------------
INCLUIR FLORES
--------------
'''

'''
TESTE DE ROTA - Flores - POST

curl http://localhost:5000/pessoa -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NDU4NDIwNCwianRpIjoiNDE0NWNhOTUtYzA0NS00Mjk2LThjZjctNjUxNzliZTA5ZTMzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODQ1ODQyMDQsImNzcmYiOiJhMmMxNTU4Yy1lNjI0LTQ2OTYtOWRlZi0wZGY5YTg4Mjc0MzMiLCJleHAiOjE3ODQ1ODUxMDR9.C2ZOz5K7Dm90QCXsiGC7BslmHn-DGYsVYRUtmmaPWsI" -H "Content-Type:application/json" -d '{"nome":"rosa", "preco":"30","cor":"vermelhas", "simbologia":"amor"}'
{"detalhes":{"":"nome": "rosa",
      "id": 1,
      "preco": "120",
      "cor": "vermelhas",
      "simbologia": "amor"},"resultado":"ok"}

'''

# rota para inserir uma flor
@app.route('/flor', methods=['POST'])
@jwt_required()  # exige que o usuário esteja autenticado para acessar esta rota
def criar_flor():
    # ler os dados em json
    dados = request.json
    
    # se faltou algum dado obrigatório...
    if not dados or not dados.get('nome') or not dados.get('preco') or not dados.get('cor') or not dados.get('simbologia'):
        # retorna erro
        return jsonify({"resultado":"erro", "detalhes":"Nome, preço, cor e simbologia são obrigatórios"}), 400
    
    # chama o serviço de criação de uma flor
    flor = flor_service.criar_flor(dados)    
    
    # retornar mensagem de sucesso :-)
    return jsonify({
        "resultado":"ok", 
        "detalhes":flor.json()
    }), 201

