from general_functions import  getJson
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

CONFIANCA_MINIMA = 0.70

class CarlosBot():  
    def __init__(self):
        self.greetings = getJson("/util/data/greetings.json")
        self.bot = ChatBot("Carlos Atendente",
        read_only = True,
        logic_adapters = [
            {
                "import_path": "chatterbot.logic.BestMatch"
            }
        ])
        self.train

    def train(self):
        self.trainer = ListTrainer(self.bot)
        self.treiner.train(self.greetings)

    def ask(self, question):
        response = self.bot.get_response(question)
        if float(response.confidence) > 0.5:
            return f'🤖Carlos bot: {response}'
        else:
            return '🤖Carlos bot: Ainda não sei responder esta pergunta'