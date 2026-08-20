import pygame
import sys


def escolher(msg, opcoes):
    while True:
        r = input(msg).strip().lower()
        if r in opcoes:
            return r
        print("⚠️ Opção inválida. Tente novamente.")

state = {"vida": 3, "inv": []}

def pegar(item):
    if item not in state["inv"]:
        state["inv"].append(item)
        print(f"🎒 Item obtido: [{item.upper()}]")

def curar(pts):
    state["vida"] = min(5, state["vida"] + pts)
    print(f"❤️ Você recuperou vida! Vida atual: {state['vida']}/5")

def dano(pts):
    state["vida"] -= pts
    print(f"💥 Você sofreu dano! Vida atual: {state['vida']}/5")

def nivel_01_inicio():
    print("\n--- NÍVEL 1: O BURACO NA SELVA ---")
    print("Você acorda na selva e há um enorme buraco cobrindo a trilha.")
    op = escolher("1) Tentar pular o buraco  2) Passar por uma árvore caída: ", ["1", "2"])
    if op == "1":
        dano(1)
        return "nivel_02_espinhos" if state["vida"] > 0 else "fim_ruim"
    pegar("galho_forte")
    return "nivel_02_espinhos"

def nivel_02_espinhos():
    print("\n--- NÍVEL 2: OS ESPINHOS ---")
    print("Arbustos cheios de espinhos bloqueiam a passagem.")
    op = escolher("1) Forçar passagem  2) Usar pedra para cortar caminho: ", ["1", "2"])
    if op == "1":
        dano(1)
        return "nivel_03_caverna" if state["vida"] > 0 else "fim_ruim"
    pegar("pedra_afiada")
    return "nivel_03_caverna"

def nivel_03_caverna():
    print("\n--- NÍVEL 3: A CAVERNA ESCURA ---")
    print("Começa a chover forte e você encontra uma caverna com morcegos.")
    op = escolher("1) Entrar no escuro  2) Fazer uma tocha improvisada: ", ["1", "2"])
    if op == "2" and "galho_forte" in state["inv"]:
        print("Você acende uma tocha e espanta os morcegos!")
        pegar("tocha")
        return "nivel_04_rio"
    dano(1)
    return "nivel_04_rio" if state["vida"] > 0 else "fim_ruim"

def nivel_04_rio():
    print("\n--- NÍVEL 4: O RIO DAS PIRANHAS ---")
    print("Você chega a um rio agitado e cheio de piranhas.")
    op = escolher("1) Nadar rápido  2) Montar uma pequena jangada: ", ["1", "2"])
    if op == "1":
        dano(2)
        return "nivel_05_acampamento" if state["vida"] > 0 else "fim_ruim"
    print("Você atravessa em segurança com a jangada!")
    return "nivel_05_acampamento"

def nivel_05_acampamento():
    print("\n--- NÍVEL 5: ACAMPAMENTO ABANDONADO ---")
    print("Você acha uma barraca velha com suprimentos.")
    op = escolher("1) Pegar o kit médico  2) Pegar o mapa antigo: ", ["1", "2"])
    if op == "1":
        curar(2)
    else:
        pegar("mapa")
    return "nivel_06_pantano"

def nivel_06_pantano():
    print("\n--- NÍVEL 6: PÂNTANO MOVEDIÇO ---")
    print("Você começa a afundar na lama movediça!")
    op = escolher("1) Debater-se para sair  2) Manter a calma e usar cipó/raiz: ", ["1", "2"])
    if op == "1":
        dano(1)
        return "nivel_07_frutas" if state["vida"] > 0 else "fim_ruim"
    pegar("cipo")
    return "nivel_07_frutas"

def nivel_07_frutas():
    print("\n--- NÍVEL 7: FRUTAS MISTERIOSAS ---")
    print("Você encontra frutas brilhantes em uma árvore.")
    op = escolher("1) Comer as frutas  2) Ignorar e continuar: ", ["1", "2"])
    if op == "1":
        print("As frutas eram venenosas!")
        dano(1)
        return "nivel_08_ponte" if state["vida"] > 0 else "fim_ruim"
    return "nivel_08_ponte"

def nivel_08_ponte():
    print("\n--- NÍVEL 8: A PONTE DE CORDA ---")
    print("Há um abismo com uma ponte velha caindo aos pedaços.")
    op = escolher("1) Correr pela ponte  2) Usar cipó como tirolesa: ", ["1", "2"])
    if op == "2" and "cipo" in state["inv"]:
        print("Você desliza pela tirolesa com sucesso!")
        return "nivel_09_onca"
    print("A ponte quebra! Você cai e se machuca.")
    dano(1)
    return "nivel_09_onca" if state["vida"] > 0 else "fim_ruim"

def nivel_09_onca():
    print("\n--- NÍVEL 9: ATAQUE DA ONÇA ---")
    print("Uma onça-pintada surge rosnando na sua frente!")
    op = escolher("1) Lutar com as mãos  2) Espantar com o fogo da tocha: ", ["1", "2"])
    if op == "2" and "tocha" in state["inv"]:
        print("A onça se assusta com o fogo e foge!")
        return "nivel_10_templo"
    dano(2)
    return "nivel_10_templo" if state["vida"] > 0 else "fim_ruim"

def nivel_10_templo():
    print("\n--- NÍVEL 10: O ENIGMA DAS RUÍNAS ---")
    print("Enigma da porta: 'O que corre sem ter pernas?'")
    op = escolher("1) O vento  2) O rio: ", ["1", "2"])
    if op == "2":
        print("A porta se abre! Você acha um sinalizador.")
        pegar("sinalizador")
        return "nivel_11_labirinto"
    dano(1)
    return "nivel_11_labirinto" if state["vida"] > 0 else "fim_ruim"

def nivel_11_labirinto():
    print("\n--- NÍVEL 11: O LABIRINTO ---")
    print("Você entra em um corredor com vários caminhos.")
    op = escolher("1) Caminho da esquerda  2) Caminho da direita: ", ["1", "2"])
    if "mapa" in state["inv"]:
        print("Você usa o mapa e acha a saída facilmente!")
        return "nivel_12_ninho"
    if op == "1":
        dano(1)
        return "nivel_12_ninho" if state["vida"] > 0 else "fim_ruim"
    return "nivel_12_ninho"

def nivel_12_ninho():
    print("\n--- NÍVEL 12: NINHO DE COBRAS ---")
    print("O chão está repleto de cobras venenosas.")
    op = escolher("1) Andar devagar sem fazer barulho  2) Correr e pular: ", ["1", "2"])
    if op == "1":
        return "nivel_13_escalada"
    dano(1)
    return "nivel_13_escalada" if state["vida"] > 0 else "fim_ruim"

def nivel_13_escalada():
    print("\n--- NÍVEL 13: O PAREDÃO DE ROCHA ---")
    print("Você precisa escalar um paredão íngreme.")
    op = escolher("1) Subir pelas pedras soltas  2) Usar raízes firmes: ", ["1", "2"])
    if op == "2":
        return "nivel_14_tempestade"
    dano(1)
    return "nivel_14_tempestade" if state["vida"] > 0 else "fim_ruim"

def nivel_14_tempestade():
    print("\n--- NÍVEL 14: TEMPESTADE NO TOPO ---")
    print("Raios e ventos fortes atingem o alto da montanha.")
    op = escolher("1) Buscar abrigo nas rochas  2) Continuar andando no aberto: ", ["1", "2"])
    if op == "1":
        return "nivel_15_resgate"
    dano(1)
    return "nivel_15_resgate" if state["vida"] > 0 else "fim_ruim"

def nivel_15_resgate():
    print("\n--- NÍVEL 15: O RESGATE FINAL ---")
    print("Você ouve um helicóptero de resgate sobrevoando!")
    if "sinalizador" in state["inv"]:
        print("Você dispara o sinalizador! O helicóptero vê a luz e pousa!")
        return "fim_bom"
    op = escolher("1) Fazer fumaça com a tocha  2) Apenas gritar alto: ", ["1", "2"])
    if op == "1" and "tocha" in state["inv"]:
        print("A fumaça chama a atenção do piloto!")
        return "fim_bom"
    return "fim_ruim"

def fim_bom():
    print("\n🏆 🎉 PARABÉNS! Você superou todos os 15 níveis e foi resgatado!")
    print(f"Vida restante: {state['vida']}/5")
    print("Inventário final:", state["inv"])
    return "fim"

def fim_ruim():
    print("\n💀 GAME OVER! A selva foi implacável desta vez.")
    print("Inventário final:", state["inv"])
    return "fim"

cenas = {
    "inicio": nivel_01_inicio,
    "nivel_02_espinhos": nivel_02_espinhos,
    "nivel_03_caverna": nivel_03_caverna,
    "nivel_04_rio": nivel_04_rio,
    "nivel_05_acampamento": nivel_05_acampamento,
    "nivel_06_pantano": nivel_06_pantano,
    "nivel_07_frutas": nivel_07_frutas,
    "nivel_08_ponte": nivel_08_ponte,
    "nivel_09_onca": nivel_09_onca,
    "nivel_10_templo": nivel_10_templo,
    "nivel_11_labirinto": nivel_11_labirinto,
    "nivel_12_ninho": nivel_12_ninho,
    "nivel_13_escalada": nivel_13_escalada,
    "nivel_14_tempestade": nivel_14_tempestade,
    "nivel_15_resgate": nivel_15_resgate,
    "fim_bom": fim_bom,
    "fim_ruim": fim_ruim,
}

cena = "inicio"
while cena != "fim":
    cena = cenas[cena]()