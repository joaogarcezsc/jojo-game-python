class Stand:
    def __init__(self, dicionario_stand):
        self.nome = dicionario_stand["nome"]
        self.fala_de_ataque = dicionario_stand["fala_de_ataque"]
        self.ataque = 100

    def atacar(self):
        print(self.fala_de_ataque)
        
class Usuario:
    def __init__(self, dicionario_usuario, stand):
        self.nome = dicionario_usuario["nome"]
        self.hp_normal = dicionario_usuario["hp_normal"]
        self.hp_apelao = dicionario_usuario["hp_apelao"]
        self.stand = stand
        
    def apanhar_justo(self, dano_recebido):
        self.hp_apelao = self.hp_apelao - dano_recebido
        if(self.hp_apelao <= 0):
            print(f'{self.nome} FORA DE COMBATE !')

    def apanhar_injusto(self, dano_recebido):
        self.hp_normal = self.hp_normal - dano_recebido
        if(self.hp_normal <= 0):
            print(f'{self.nome} FORA DE COMBATE !')

        

            