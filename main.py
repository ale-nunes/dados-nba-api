import csv
from flask import Flask, jsonify, request

# Criando o objeto da aplicação Flask
app = Flask(__name__)

# Definindo a rota para retornar todas as linhas do CSV
@app.route('/data', methods=['GET'])
def get_data():
    with open('data\data_players_2005_2023_v1.csv', encoding='UTF-8',  newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
    return jsonify({'data': rows})  

# Definindo a rota para retornar uma linha específica do CSV
@app.route('/data/<int:index>', methods=['GET'])
def get_row(index):
    with open('data\data_players_2005_2023_v1.csv', encoding='UTF-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
    if index < 0 or index >= len(rows):
        abort(404)
    return jsonify({'data': rows[index]})

# Definindo a rota para adicionar uma nova linha ao CSV
@app.route('/data', methods=['POST'])
def add_row():
    if not request.json or not 'nome' in request.json or not 'idade' in request.json:
        abort(400)
    with open('data\data_players_2005_2023_v1.csv', 'a', encoding='UTF-8', newline='') as csvfile:
        fieldnames = ['nome', 'idade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'nome': request.json['nome'], 'idade': request.json['idade']})
    return jsonify({'status': 'success'})

# Rodando a aplicação na porta 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)



