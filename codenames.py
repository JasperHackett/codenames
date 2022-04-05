from flask import Flask
from flask import render_template
from flask import request
import random


wordlist = []
words = []
boardvalues = {}
shownvalues = {}
cssclass = []
with open("codenames.txt") as f:
    for line in f:
        word = line.rstrip()
        wordlist.append(word)


def getgrid():
    positions = []

    positions.append("R")
    positions.append("B")
    first_player = random.choice(positions)

    if first_player == "R" :
        print('red')
        positions.append("R")
    elif first_player == "B":
        print('blue')
        positions.append("B")

    for x in range(7):
        positions.append("R")
        positions.append("B")
        positions.append("i")

    positions.append("A")

    random.shuffle(positions)

    return positions

def getwords():
    # print(len(boardvalues))
    boardvalues.clear()
    shownvalues.clear()
    print(len(boardvalues))
    positions = getgrid()
    random.shuffle(wordlist)

    for x in range(25):
        new_word = wordlist[x]
        boardvalues[new_word] = positions[x]
        shownvalues[new_word] = 'wordbtn'
    return


getwords()
app = Flask(__name__)





@app.route('/')
@app.route('/board', methods=['GET','POST'])
def board():

    if request.method == 'POST':
        # grid_value = boardvalues[request.form['submit_button']]
        if shownvalues[request.form['submit_button']] == boardvalues[request.form['submit_button']]:
            shownvalues[request.form['submit_button']] = 'wordbtn'
        elif shownvalues[request.form['submit_button']] == 'wordbtn':
            shownvalues[request.form['submit_button']] = boardvalues[request.form['submit_button']]
        # print(grid_value)
        # if grid_value == "i":

        # request.form.content(style=class_"emptybtn")




    return render_template('board.html',boardvalues=shownvalues)

@app.route('/grid', methods=['GET','POST'])
def grid():

    # if request.method == 'GET':
    #     # print('LENGTHS:')
    #     #
    #     getwords()
    #     # print (len(boardvalues))
    #     # boardvalues.clear()
    #     # print (len(boardvalues))

    return render_template('grid.html',boardvalues=boardvalues)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
