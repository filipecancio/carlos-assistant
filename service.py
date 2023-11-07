from bot import CarlosBot
from flask import Flask

bot = CarlosBot()
app = Flask(__name__)

@app.route("/ask/<mensagem>")
def ask_bot(mensagem):
    resposta = bot.ask(mensagem)

    return resposta

if __name__ == "__main__":
    app.run()