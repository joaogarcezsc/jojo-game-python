class Stand:
    def __init__(self, nome, ataques_normais, ataques_apeloes):
        self.nome = nome
        self.ataques_normais = ataques_normais
        self.ataques_apeloes = ataques_apeloes

    def atacar(self, fala_de_ataque):
        self.fala_de_ataque = fala_de_ataque
        print(fala_de_ataque)
        
class Usuario:
    def __init__(self, nome, hp_normal, hp_apelao, stand):
        self.nome = nome
        self.hp_normal = hp_normal
        self.hp_apelao = hp_apelao
        self.stand = stand
        
    def apanhar_justo(self, dano_recebido):
        self.hp_apelao = self.hp_apelao - dano_recebido
        if(self.hp_apelao <= 0):
            print(f'{self.nome} FORA DE COMBATE !')

    def apanhar_injusto(self, dano_recebido):
        self.hp_normal = self.hp_normal - dano_recebido
        if(self.hp_normal <= 0):
            print(f'{self.nome} FORA DE COMBATE !')

        

            