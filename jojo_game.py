from jojo_class import Stand
from jojo_class import Usuario
import os
import sys
import time

#----------DICIONÁRIOS----------#
dados_do_starplatium = {
    "nome": "Star Platium",
    "fala_de_ataque": "ORA ORA ORA ORA!"
}
dados_do_jotarokujo = {
    "nome": "Jotaro Kujo",
    "hp_normal": 150,
    "hp_apelao": 500
}
starplatium = Stand(dados_do_starplatium)
jotarokujo = Usuario(dados_do_jotarokujo, starplatium)

dados_do_heiriphantgreen = {
    "nome": "Heierophant Green",
    "fala_de_ataque": "Receba isso! ESMERALD SPLASH" 
}
dados_do_kakyoinnoriaki = {
    "nome": "Kakyoin Noriaki",
    "hp_normal": 100,
    "hp_apelao": 250
}

heiriphantgreen = Stand(dados_do_heiriphantgreen)
kakyoinnoriaki = Usuario(dados_do_kakyoinnoriaki, heiriphantgreen)

dados_do_silverchariot = {
    "nome": "Silver Chariot",
    "fala_de_ataque": "Despedace, Silver Chariot !" 
}
dados_do_jeanpierrepolnareff = {
    "nome": "Jean Pierre Polnareff",
    "hp_normal": 110,
    "hp_apelao": 280
}

silverchariot = Stand(dados_do_silverchariot)
jeanpierrepolnareff = Usuario(dados_do_jeanpierrepolnareff, silverchariot)

dados_do_magicansred = {
    "nome": "Magician's Red",
    "fala_de_ataque": "YES, I AM! Avassale, CROSSFIRE HURRICANE HURRICANE!" 
}
dados_do_muhammadavdol = {
    "nome": "Muhammad Avdol",
    "hp_normal": 115,
    "hp_apelao": 270
}

magicansred = Stand(dados_do_magicansred)
muhammadavdol = Usuario(dados_do_muhammadavdol, magicansred)

dados_do_hermitpurple = {
    "nome": "Hermit Purple",
    "fala_de_ataque": "Sua próxima linha será... Overdrive de Hamon" 
}
dados_do_josephjoestar = {
    "nome": "Joseph Joestar",
    "hp_normal": 100,
    "hp_apelao": 240
}

hermitpurple = Stand(dados_do_hermitpurple)
josephjoestar = Usuario(dados_do_josephjoestar, hermitpurple)

dados_do_theworld = {
    "nome": "The World",
    "fala_de_ataque": "MUDA MUDA MUDA MUDA !"
}

dados_do_dio = {
    "nome": "Dio",
    "hp_normal": 300,
    "hp_apelao": 600
}

theworld = Stand(dados_do_theworld)
dio = Usuario(dados_do_dio, theworld)

dados_do_towerofgray = {
    "nome": "Tower of Gray",
    "fala_de_ataque": "Minha agulha vai rasgar sua língua! Hahaha!"
}
dados_do_grayfly = {
    "nome": "Gray Fly",
    "hp_normal": 105,
    "hp_apelao": 300
}
towerofgray = Stand(dados_do_towerofgray)
grayfly = Usuario(dados_do_grayfly, towerofgray)

dados_do_yellowtemperance = {
    "nome": "Yellow Temperance",
    "fala_de_ataque": "Meu Stand não tem fraquezas! Ele vai te devorar!"
}
dados_do_rubbersoul = {
    "nome": "Rubber Soul",
    "hp_normal": 70,
    "hp_apelao": 350
}
yellowtemperance = Stand(dados_do_yellowtemperance)
rubbersoul = Usuario(dados_do_rubbersoul, yellowtemperance) 

dados_do_hangedman = {
    "nome": "Hanged Man",
    "fala_de_ataque": "Eu estou no world dos espelhos! Você nunca vai me tocar!"
}
dados_do_jgeil = {
    "nome": "J. Geil",
    "hp_normal": 110,
    "hp_apelao": 320
}
hangedman = Stand(dados_do_hangedman)
jgeil = Usuario(dados_do_jgeil, hangedman)

dados_do_judgement = {
    "nome": "Judgement",
    "fala_de_ataque": "HAIL 2 U! Seus desejos soterraram você!"
}
dados_do_cameo = {
    "nome": "Cameo",
    "hp_normal": 85,
    "hp_apelao": 310
}
judgement = Stand(dados_do_judgement)
cameo = Usuario(dados_do_cameo, judgement)

dados_do_bastet = {
    "nome": "Bastet",
    "fala_de_ataque": "Sinta a força da atração magnética! Esmagado pelo ferro!"
}
dados_do_mariah = {
    "nome": "Mariah",
    "hp_normal": 120,
    "hp_apelao": 290
}
bastet = Stand(dados_do_bastet)
mariah = Usuario(dados_do_mariah, bastet)

#----------FLUXO DE FASES----------#

fases_do_jogo = [
    {
        "local": "Hong Kong",
        "data": "4 de dezembro de 1988",
        "heroi_correto": kakyoinnoriaki,
        "id_heroi": 1,
        "vilao_da_fase": grayfly,             
        "texto_chegada": "Vocês desembarcam em Hong Kong. O clima é tenso e, de repente, um inseto bizarro ataca no avião!"
    },
    {
        "local": "Cingapura",
        "data": "13 de Dezembro de 1988",
        "heroi_correto": jotarokujo,
        "id_heroi": 2,
        "vilao_da_fase": rubbersoul,
        "texto_chegada": "Chegando em Cingapura, em um hotel luxuoso, um aliado parece agir de forma muito estranha..."
    },
    {
        "local": "Índia (Calcutá)",
        "data": "20 de Dezembro de 1988",
        "heroi_correto": jeanpierrepolnareff,
        "id_heroi": 3,
        "vilao_da_fase": jgeil,
        "texto_chegada": "Nas ruas movimentadas de Calcutá, a chuva começa a cair e um reflexo mortal aparece nos espelhos."
    },
    {
        "local": "Mar Vermelho",
        "data": "28 de Dezembro de 1988",
        "heroi_correto": muhammadavdol,
        "id_heroi": 4,
        "vilao_da_fase": cameo,
        "texto_chegada": "Em uma ilha deserta no Mar Vermelho, desejos do passado ganham vida de forma assustadora."
    },
    {
        "local": "Egito (Luxor)",
        "data": "16 de Janeiro de 1989",
        "heroi_correto": josephjoestar,
        "id_heroi": 5,
        "vilao_da_fase": mariah,
        "texto_chegada": "Já em solo egípcio, na cidade de Luxor, uma tomada misteriosa em uma rocha desperta uma força magnética."
    },
    {
        "local": "Egito (Cairo)",
        "data": "21 de Janeiro de 1989",
        "heroi_correto": jotarokujo,
        "id_heroi": 2,
        "vilao_da_fase": dio,
        "texto_chegada": "O confronto final nas ruas escuras do Cairo. O próprio tempo parece parar diante da presença maligna de DIO!"
    }
]

#----------SAUDAÇÕES----------#

def saudacao_inical():
    print("\n-----BEM-VINDO AO GAME DE JOJO'S BIZARRES ADVENTURE EM PYTHON !-----\n")
    print("Nesse jogo você irá controlar o grupo de amigos liderados por Joseph Joestar e Jotaro Kujo em sua jornada para o Egito na caça de Dio, para salvar a vida de Holy Joestar !\n")
    input("Tecle enter para seguir para as regras do jogo\n")
    regras_do_jogo()

def regras_do_jogo():
    os.system('cls')
    print('-----REGRAS DO GAME-----\n')
    print('O game consiste em acompanhar a narrativa da jornada de Jojo e seus amigos até ao Egito em busca de derrotar Dio !\n')
    print('Durante a jornada, você precisará escolher os personagens corretos para vencer os vilões que forem aparecendo no caminho, uma escolha errada fará você perder o jogo !\n')
    #input('Vamos Nessa ? (Tecle enter para começar)\n')
    #texto_de_introducao("DATA: 28 de Novembro de 1988\nLOCAL: Prisão de Tóquio, Japão\nUm jovem de 17 anos, Jotaro Kujo, trancou-se em uma cela alegando estar possuído por um 'espírito maligno'. Mal sabia ele que essa força é um Stand, uma manifestação de sua própria energia vital, despertada pelo retorno do arqui-inimigo de sua família: DIO.\nCom a vida de sua mãe, Holy Joestar, correndo perigo devido à febre do Stand, o relógio começa a correr. Joseph Joestar, Jotaro, Avdol, Kakyoin e Polnareff iniciam uma jornada desesperada de 50 dias rumo ao Egito. O destino do sangue Joestar será decidido agora!")
    input('\n(Tecle Enter)')
    narrativa_do_jogo()


def texto_de_introducao(texto, velocidade=0.04):
    os.system('cls')
    for letra in texto:
        # sys.stdout.write joga a letra na tela sem pular linha automaticamente
        sys.stdout.write(letra)
        # sys.stdout.flush garante que o terminal mostre a letra NA HORA, sem travar
        sys.stdout.flush()
        # O programa espera um pouquinho antes de ir para a próxima letra
        time.sleep(velocidade)
    print()

#----------NARRATIVA----------#

def narrativa_do_jogo():
    for fase in fases_do_jogo:
        texto_de_introducao(f"DATA: {fase['data']}\nLOCAL: {fase['local']}\n{fase['texto_chegada']}")
        input()
        vilao = fase['vilao_da_fase']
        texto_de_introducao(f"Eu sou {vilao.nome}, usuário do stand {vilao.stand.nome} !\nFui enviado por Lord Dio para aniquilar vocês, e é isso que irei fazer.")
        input()
        vitoria = combate_narrativa(fase, vilao)
        if vitoria == True: 
            print('Vitória !')
            input()
        else: 
            print ('Derrota !')
            input()

#----------COMBATE----------#

def combate_narrativa(fase, vilao):
    os.system('cls')
    print(f"--- COMBATE EM {fase['local'].upper()} ---")
    print('Selecione um herói para enfrentar esse perigoso usuário de Stand:\n')
    heroi_selecionado = int(input('1)Kakyoin Noriaki\n2)Jotaro Kujo\n3)Jean Pierre Polnareff\n4)Muhammad Avdol\n5)Joseph Joestar\n'))
    hp_vilao = vilao.hp_normal
    hp_max_vilao = vilao.hp_normal

    if heroi_selecionado == fase['id_heroi']:
        heroi = fase['heroi_correto']
        hp_heroi = heroi.hp_apelao
        hp_max_heroi = heroi.hp_apelao
        
        combate_dano(heroi, vilao, hp_heroi, hp_vilao, hp_max_heroi, hp_max_vilao)
        return True
     
    else:
        if heroi_selecionado == 1: heroi = kakyoinnoriaki
        elif heroi_selecionado == 2: heroi = jotarokujo
        elif heroi_selecionado == 3: heroi = jeanpierrepolnareff
        elif heroi_selecionado == 4: heroi = muhammadavdol
        elif heroi_selecionado == 5: heroi = josephjoestar

        hp_heroi = heroi.hp_normal
        hp_max_heroi = heroi.hp_normal
        
        hp_vilao = vilao.hp_apelao       
        hp_max_vilao = vilao.hp_apelao

        combate_dano(heroi, vilao, hp_heroi, hp_vilao, hp_max_heroi, hp_max_vilao)
        return False
    
def combate_dano(heroi, vilao, hp_heroi, hp_vilao, hp_max_heroi, hp_max_vilao):
    while hp_vilao > 0 and hp_heroi > 0:
        os.system('cls')
        print(f'{heroi.stand.nome}: {heroi.stand.fala_de_ataque}')
        input()

        hp_vilao -= heroi.stand.ataque
        if hp_vilao < 0: hp_vilao = 0

        porcentagem_vilao = (hp_vilao / hp_max_vilao) * 100
        print(f"-> {vilao.nome} recebeu dano! HP Restante: {porcentagem_vilao:.0f}%\n")
        if hp_vilao <= 0: 
            print(f'{vilao.nome} FOI DERROTADO!')
            input('\n(Tecle Enter para continuar)')
            break

        print(f'{vilao.stand.nome}: "{vilao.stand.fala_de_ataque}"')
        input()
        hp_heroi -= vilao.stand.ataque
            
        if hp_heroi < 0: hp_heroi = 0
            
        porcentagem_heroi = (hp_heroi / hp_max_heroi) * 100
        print(f"-> {heroi.nome} recebeu dano! HP Restante: {porcentagem_heroi:.0f}%\n")
        if hp_heroi <= 0: 
            print(f'{heroi.nome} FOI DERROTADO!')
            input('\n(Tecle Enter para continuar)')
            break
            
        input('(Tecle Enter para o próximo turno...)')

saudacao_inical()


