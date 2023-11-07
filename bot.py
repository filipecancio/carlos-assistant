from general_functions import  getJson
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

MINIMAL_CONFIDENCE = 0.5

class CarlosBot():  
    def __init__(self):
        self.bot = ChatBot("Carlos Atendente",
        read_only = True,
        logic_adapters = [
            {
                "import_path": "chatterbot.logic.BestMatch"
            }
        ])
        self.pre_train()
        self.train()

    def pre_train(self):
        self.storage = []
        self.greetings = getJson("/util/data/greetings.json")

        self.storage.append(self.greetings["conversas"])

    def train(self):
        self.trainer = ListTrainer(self.bot)
        for talk in self.storage:
            for message in talk:
                request = message["mensagens"]
                response = message["resposta"]

                for req in request:
                    self.trainer.train([req, response])

    def ask(self, question):
        response = self.bot.get_response(question)
        if float(response.confidence) > MINIMAL_CONFIDENCE:
            return response
        else:
            return 'Ainda não sei responder esta pergunta'