import unicodedata
import re

def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')

    # Substituições apenas para tokens relevantes ao chatbot
    substituicoes = {
        "pq": "porque",
        "por que": "porque",
        "cm": "como",
        "qm":"quem",
        "qnd": "quando",
        "qdo": "quando",
        "prox jogo": "proximojogo",
        "proximo jogo": "proximojogo",
        "line": "lineup",
        "função": "funcao",
    }

    for de, para in substituicoes.items():
        texto = re.sub(rf'\b{de}\b', para, texto)

    texto = re.sub(r'[^\w\s]', '', texto)
    return texto.strip()

def proximo_jogo_furia():
    data = "🗓 10/05/2025 às 14:00"
    campeonato = "🏆 IEM Dallas 2025"
    formato = "🎯 MD3"
    adversario = "⚔ FURIA vs The MongolZ"
    return f"📣 Próximo jogo da FURIA!\n{data}\n{adversario}\n{campeonato}\nFormato: {formato}\n🔥 Vamos pra cima!"

def responder(mensagem):
    msg = normalizar_texto(mensagem)

    def resposta_padrao():
        return "🤔 Não entendi muito bem... Pergunte sobre os jogadores, a história ou o próximo jogo da FURIA! 🎮"

    # QUEM
    if "quem" in msg:
        if any(x in msg for x in ["fallen", "gabriel", "toledo"]):
            return ("🎯 FalleN (Gabriel Toledo) é uma lenda do CS brasileiro! 🇧🇷\n"
                    "Bicampeão mundial, atualmente lidera a FURIA como IGL. 🧠🔫")
        if any(x in msg for x in ["kscerato", "kaike", "cerato"]):
            return ("🔥 KSCERATO (Kaike Cerato) é o rifler consistente da FURIA desde 2018! 💥\n"
                    "Conhecido por sua mira precisa e leitura de jogo. 🧠💣")
        if any(x in msg for x in ["yuurih", "yuri", "santos"]):
            return ("⚡ Yuurih (Yuri Santos) é conhecido por sua agressividade controlada! 🚀\n"
                    "Desde 2018 na FURIA, é uma peça-chave com impacto gigante! 🐾")
        if any(x in msg for x in ["molodoy", "danil", "golubenko"]):
            return ("🧊 Molodoy (Danil Golubenko) é o novo AWP da FURIA! 🇰🇿\n"
                    "Chegou em abril de 2025 trazendo mira afiada e sangue novo pro time! 💥🔭")
        if any(x in msg for x in ["yekindar", "mareks", "galinskis"]):
            return ("🔥 YEKINDAR (Mareks Gaļinskis) é o stand-in da FURIA desde abril de 2025! ⚔\n"
                    "Conhecido por seu estilo agressivo e entradas impactantes. 💣")
        if "fundou" in msg or "criador" in msg:
            return "📜 A FURIA foi fundada por Jaime 'raizen' Pádua e André Akkari em 2017. 🐾"
        if any(x in msg for x in ["coach", "treinador", "sidde", "sid"]):
            return ("🧠 Sidnei 'sidde' Macedo é o atual treinador principal da FURIA no CS2!\n"
                    "Assumiu o cargo em julho de 2024, trazendo estratégias inovadoras para o time. 🎯")

    # QUANDO
    if "quando" in msg:
        if "criada" in msg or "fundada" in msg:
            return "📆 A FURIA foi criada em 2017."
        if "fallen" in msg and "entrou" in msg:
            return "📥 FalleN entrou na FURIA em julho de 2023. 🔥"
        if "yekindar" in msg and "entrou" in msg:
            return "📥 YEKINDAR chegou à FURIA em abril de 2025 como stand-in."
        if "molodoy" in msg and "entrou" in msg:
            return "📥 Molodoy se juntou à FURIA em abril de 2025."
        if "proximojogo" in msg:
            return proximo_jogo_furia()

    # PORQUE
    if "porque" in msg:
        if "fallen" in msg and "furia" in msg:
            return "🧠 FalleN entrou na FURIA para trazer experiência, tática e liderança ao time! 🇧🇷"
        if "yekindar" in msg:
            return "⚔ YEKINDAR se juntou à FURIA como stand-in para fortalecer a equipe em 2025."
        if "molodoy" in msg:
            return "🔫 Molodoy foi contratado para reforçar a AWP da FURIA com sua mira precisa."
        if "mudou" in msg and "lineup" in msg:
            return "🔄 A FURIA mudou sua lineup em 2025 buscando renovar e melhorar resultados internacionais."
        if "furia" in msg and "agressiva" in msg:
            return "🔥 A agressividade é marca registrada da FURIA, sufocando os adversários desde o início!"

    # QUAL
    if "qual" in msg:
        if "lineup" in msg:
            return ("🧑‍💻 Line-up 2025:\n"
                    "- FalleN (IGL)\n"
                    "- KSCERATO (Rifler)\n"
                    "- yuurih (Rifler)\n"
                    "- molodoy (AWP)\n"
                    "- YEKINDAR (Rifler)")
        if "funcao" in msg and "fallen" in msg:
            return "🎯 FalleN é o IGL (líder de jogo) da FURIA."
        if "estilo" in msg and "yekindar" in msg:
            return "💣 YEKINDAR é conhecido por seu estilo agressivo e entradas impactantes!"
        if "ranking" in msg:
            return "📊 A FURIA está atualmente no Top 20 do ranking da HLTV (dados de 2025)."
        if "origem" in msg or "nome" in msg:
            return "🐾 O nome FURIA representa intensidade e garra — pilares da filosofia competitiva do time!"
        if "proximojogo" in msg:
            return proximo_jogo_furia()

    # COMO
    if "como" in msg:
        if "comecou" in msg and "furia" in msg:
            return "🚀 A FURIA começou sua jornada em 2017 com o objetivo de revolucionar os esports no Brasil."
        if "jogar" in msg and "furia" in msg:
            return "🎮 Para jogar na FURIA, é preciso se destacar no cenário competitivo e ter disciplina e mentalidade forte!"
        if "estreia" in msg:
            return "🌍 A estreia internacional da FURIA foi no Major de Katowice 2019."
        if "treina" in msg:
            return "🧠 A FURIA treina todos os dias com táticos, deathmatch, scrims e análise de demos!"
        if "estilo" in msg:
            return "🔥 O estilo da FURIA é agressivo e direto, sufocando os adversários com pressão constante!"

    return resposta_padrao()