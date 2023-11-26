import unittest
from bot import CarlosBot, MINIMAL_CONFIDENCE
        

class TestGreetings(unittest.TestCase):

    def setUp(self):
        self.bot = CarlosBot()

    def testar_oi_ola(self):
        #Configuration
        phraseList = [ "oi", "olá" ]
        expectedPhrase = "Olá, sou Carlos, seu atendente de barbearia. Como posso te ajudar?"
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

    def testar_boa_tarde_boa_noite(self):
        #Configuration
        phraseList = [ "Boa noite", "noite" ]
        expectedPhrase = "Boa noite, sou Carlos, seu atendente de barbearia. Como posso te ajudar?"
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

    def testar_disponibilidade(self):
        #Configuration
        phraseList = [ "Há disponibilidade de corte?" ]
        expectedPhrase = "Tem sim, tem preferência de horário ou de cabelereiro?"
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

    def testar_barbeiro_jonatas(self):
        #Configuration
        phraseList = [ "Quantos clientes faltam para o barbeiro Jonatas?" ]
        expectedPhrase = "O Jonatas está livre, pode vir agora mesmo"
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

    def testar_horario(self):
        #Configuration
        phraseList = [ "Qual o horário de atendimento?" ]
        expectedPhrase = "Atendemos de segunda a sexta das 8h às 18h e aos sábados das 8h às 12h."
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

    def testar_pagamento(self):
        #Configuration
        phraseList = [ "Voces aceitam pix?" ]
        expectedPhrase = "sim, sim aceitamos pix. Aceitamos também cartão de crédito, débito e dinheiro."
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

    def testar_cortes(self):
        #Configuration
        phraseList = [ "Quais tipos de cortes voces fazem?" ]
        expectedPhrase = "realizamos todos os tipos de cortes, undercut, social, moicano.. Você pode trazer uma foto de referência se quiser. Veja também algum dos cortes presentes no nosso instagram @CarlosBarbearia."
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

    def testar_agua(self):
        #Configuration
        phraseList = [ "Vendem água e outros produtos?" ]
        expectedPhrase = "temos água, refrigerante e tudo mais"
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

    def testar_agendar_pedro(self):
        #Configuration
        phraseList = [ "Posso agendar com o barbeiro Pedro?" ]
        expectedPhrase = "O Pedro trabalha sexta das 8h às 18h e sábado das 8h às 12h."
        
        #Execution
        self.assertBotText(phraseList,expectedPhrase)

            
    def assertBotText(self,phraseList,expectedPrase):
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
