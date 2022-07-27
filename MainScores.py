from flask import Flask

app = Flask(__name__)  # Run service of display main score


@app.route("/")  # accessed via <HOST>:<PORT>/
def welcome():
    return score_server(), 200  # status code


# This function will serve the score. It will read the score from the Scores.txt file and will return an HTML
def score_server():
    # player_score = 0    # ???
    # str_for_html = ""   # ???

    try:
        score_file = open("Scores.txt", "r")
        player_score = score_file.read()
        str_for_html = f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>Welcome to the World Of Games! </h1>
                    <h3 style="color:blue;">Your score is: <span id="score">{player_score}</span></h3>
                </body>
            </html>
        """
        score_file.close()
    except:
        error = exec()
        str_for_html = f""""
                    <html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>Welcome to the World Of Games! </h1>
                            <h3><span id="score" style="color:red">{error}</span></h3>
                        </body>
                    </html>
                """

    return str_for_html


def run_score_service():
    if __name__ == '__main__':
        app.run(host='127.0.0.1', debug=True, port=5000)


run_score_service()
