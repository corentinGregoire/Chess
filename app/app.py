from flask import Flask, render_template, request
import chess
import chess.svg

app = Flask(__name__)

player1_moves = []
player2_moves = []

def render_board(board):
    return chess.svg.board(board=board)

def is_checkmate(board):
    return board.is_checkmate()

@app.route('/')
def index():
    board = chess.Board()
    print("Player 1 Moves:", player1_moves)
    print("Player 2 Moves:", player2_moves)
    return render_template('index.html', board=board, render_board=render_board, is_checkmate=is_checkmate,
                           player1_moves=player1_moves, player2_moves=player2_moves)

@app.route('/move', methods=['POST'])
def move():
    global player1_moves, player2_moves

    fen = request.form['fen']
    move_str = request.form['move']
    
    board = chess.Board(fen)
    move = chess.Move.from_uci(move_str)
    
    if move in board.legal_moves:
        board.push(move)
        if board.turn == chess.WHITE:
            player1_moves.append(move_str)
        else:
            player2_moves.append(move_str)

    print("Player 1 Moves:", player1_moves)
    print("Player 2 Moves:", player2_moves)
    
    return render_template('index.html', board=board, render_board=render_board, is_checkmate=is_checkmate,
                           player1_moves=player1_moves, player2_moves=player2_moves)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
