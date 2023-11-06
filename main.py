from bot import CarlosBot

bot = CarlosBot()

while True:
    pergunta = input("Usuário: ")
    resposta = bot.ask(pergunta)
    print(resposta)