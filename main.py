from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Função para embaralhar as cartas
def embaralhar_cartas():
    cartas = [
        '2♥️', '2♦️', '2♠️', '2♣️',  # Curingas
        '3♥️', '3♦️', '3♠️', '3♣️',
        '4♥️', '4♦️', '4♠️', '4♣️',
        '5♥️', '5♦️', '5♠️', '5♣️',
        '6♥️', '6♦️', '6♠️', '6♣️',
        '7♥️', '7♦️', '7♠️', '7♣️',
        '8♥️', '8♦️', '8♠️', '8♣️',
        '9♥️', '9♦️', '9♠️', '9♣️',
        '10♥️', '10♦️', '10♠️', '10♣️',
        'J♥️', 'J♦️', 'J♠️', 'J♣️',
        'Q♥️', 'Q♦️', 'Q♠️', 'Q♣️',
        'K♥️', 'K♦️', 'K♠️', 'K♣️',
        'A♥️', 'A♦️', 'A♠️', 'A♣️'
    ]
    random.shuffle(cartas)
    return cartas

# Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota da página do jogo
@app.route('/jogo')
def jogo():
    # Embaralha as cartas e distribui para os jogadores
    cartas = embaralhar_cartas()
    jogador1_cartas = cartas[:15]  # Jogador 1 recebe 15 cartas
    jogador2_cartas = cartas[15:30]  # Jogador 2 recebe 15 cartas

    # Passa as cartas dos jogadores para o frontend
    return render_template('jogo.html', jogador1_cartas=jogador1_cartas, jogador2_cartas=jogador2_cartas)

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
