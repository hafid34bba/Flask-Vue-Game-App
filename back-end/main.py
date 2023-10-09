from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, ressources={r"/*":{'originis':"*"}})

@app.route("/", methods = ['GET'])
def greetings(): 
    return ("Hello World")

@app.route("/shark", methods = ['GET'])
def shark():
    return ("Shark from flask")

GAMES =[
    {

        "id" : '1',
        'title': '2k21',
        'genre': 'sports',
        'played': True
    },
     {  "id" : '2',
        'title': 'Evil Within',
        'genre': 'horror',
        'played': False
    },
     {  "id" : '3',
        'title': 'The last of us',
        'genre': 'survival',
        'played': True
    }, 
    {   "id" : '4',
        'title': 'days gone',
        'genre': 'horror/survival',
        'played': False
    },
     {  "id" : '5',
        'title': 'mario',
        'genre': 'retro',
        'played': True
    }
]


@app.route('/games', methods = ['GET', 'POST'])
def all_games():
    return jsonify(
        {
            'games':GAMES,
            'status': 'sucess'
        }
    )

@app.route('/game', methods = ['POST', 'DELETE'])
def game():
    global GAMES
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        
        GAMES.append(
            {"id": uuid.uuid4().hex ,**post_data}
        )
        response_object['message'] = 'Game Added'

        return jsonify(response_object)
    # elif request.method == "DELETE":
    #     post_data = request.get_json()
    #     print(GAMES, post_data)
    #     GAMES = [game for game in GAMES if game!=post_data]
    else : 
        return ('Get not implimented yet :(')
@app.route('/game/<game_id>', methods= ['PUT'])
def update_single_game(game_id):

    response_object = {'status':'success'}
    if request.method=="PUT":
        put_data = request.get_json()
        for game, index in zip(GAMES, range(len(GAMES))):
            if game["id"] == game_id:
                print(game, put_data)
                GAMES[index] = {"id":game_id,**put_data}
    response_object['message'] = 'Game Updated'


    return jsonify(response_object)


@app.route('/game/<game_id>', methods=["DELETE"])
def remove_game(game_id):
    global GAMES
    response_object = {'status':'success'}
    print(game_id)
    
    GAMES = [game for game in  GAMES if game["id"]!=game_id]
    print(GAMES)
    
    response_object['message'] = 'Game deleted'
    return jsonify(response_object)



if __name__ == '__main__':
    app.run(debug=True)