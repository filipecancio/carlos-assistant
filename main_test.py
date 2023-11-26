import unittest
from bot import CarlosBot, MINIMAL_CONFIDENCE
        

class TestGreetings(unittest.TestCase):

    def setUp(self):
        self.bot = CarlosBot()

    def testar_oi_ola(self):
        greetings = [ "oi", "olá" ]

        for word in greetings:
            print(f"testando saudação {word}")

            resposta = self.bot.ask(word)
            self.assertGreaterEqual(resposta.confidence, MINIMAL_CONFIDENCE)
            self.assertIn(
                "Olá, sou Carlos, seu atendente de barbearia. Como posso te ajudar?", 
                resposta.text
            )

    def testar_boa_tarde_boa_noite(self):
        greetings = ["Boa noite"]

        for word in greetings:
            print(f"testando saudação {word}")

            resposta = self.bot.ask(word.lower())
            self.assertGreaterEqual(resposta.confidence, MINIMAL_CONFIDENCE)
            self.assertIn(
                word + ", sou Carlos, seu atendente de barbearia. Como posso te ajudar?",
                resposta.text
            )
            
    def assertBotText(phraseList,expectedPrase):
        for phrase in phraseList:

            response = self.bot.ask(phrase.lower())
            self.assertGreaterEqual(response.confidence, MINIMAL_CONFIDENCE)
            self.assertIn(
                expectedPrase,
                response.text
            )

if __name__ == "__main__":
    loader = unittest.TestLoader()
    testList = unittest.TestSuite()

    testList.addTest(loader.loadTestsFromTestCase(TestGreetings))

    executor = unittest.TextTestRunner()
    executor.run(testList)
