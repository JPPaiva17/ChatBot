import unicodedata
import re
import cloudscraper
from datetime import datetime
from bs4 import BeautifulSoup
import random

# Função para normalizar o texto, transformando tudo em minúsculo e removendo acentos
def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')

    # Substituições de tokens relevantes ao chatbot
    substituicoes = {
        "pq": "porque",
        "por que": "porque",
        "cm": "como",
        "qm": "quem",
        "qnd": "quando",
        "qdo": "quando",
        "prox jogo": "proximojogo",
        "proximo jogo": "proximojogo",
        "line": "lineup",
        "função": "funcao",
    }

    # Substitui os tokens no texto
    for de, para in substituicoes.items():
        texto = re.sub(rf'\b{de}\b', para, texto)

    # Remove caracteres especiais
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto.strip()

# Função para buscar o próximo jogo da FURIA no HLTV utilizando BeautifulSoup
def buscar_proximo_jogo_furia():

    url = "https://www.hltv.org/team/8297/furia#tab-matchesBox"

    scraper = cloudscraper.create_scraper()

    resposta = scraper.get(url)



    if resposta.status_code != 200:

        return "😕 Erro ao acessar o site da HLTV."



    soup = BeautifulSoup(resposta.text, "html.parser")

    tabelas = soup.find_all("table", class_="match-table")



    for tabela in tabelas:

        titulo = tabela.find_previous("h2")

        if not titulo or "upcoming" not in titulo.text.lower():

            continue



        linhas = tabela.find_all("tr")

        campeonato_atual = None



        for linha in linhas:

            if "event-header-cell" in linha.get("class", []):

                evento = linha.find("a", class_="a-reset")

                if evento:

                    campeonato_atual = evento.get_text(strip=True)

                continue



            if "team-row" in linha.get("class", []):

                adversario_tag = linha.find("a", class_="team-2") or linha.find("span", class_="team-2")

                adversario = adversario_tag.get_text(strip=True) if adversario_tag else "Adversário desconhecido"



                data_tag = linha.find("span", {"data-unix": True})

                if data_tag:

                    unix_time = int(data_tag["data-unix"]) // 1000

                    data_hora = datetime.fromtimestamp(unix_time).strftime("%d/%m/%Y %H:%M")

                else:

                    data_hora = "Data indisponível"



                link_tag = linha.find("a", class_="matchpage-button") or linha.find("a", class_="stats-button")

                link = f"https://www.hltv.org{link_tag['href']}" if link_tag else "#"



                return (

                    f"📣 Próximo jogo da FURIA!<br>"

                    f"🕒 {data_hora}<br>"

                    f"🆚 {adversario}<br>"

                    f"🏆 {campeonato_atual or 'Campeonato não identificado'}<br>"

                    f"🔗 <a href='{link}' target='_blank'>Link da próxima partida</a>"

                )



    return "😕 Nenhuma partida futura da FURIA foi encontrada."

# Função para pegar os ultimos 5 jogos da furia
def buscar_ultimos_resultados_furia():
    url = "https://www.hltv.org/team/8297/furia#tab-matchesBox"
    scraper = cloudscraper.create_scraper()
    resposta = scraper.get(url)

    if resposta.status_code != 200:
        return "😕 Erro ao acessar o site da HLTV."

    soup = BeautifulSoup(resposta.text, "html.parser")
    tabelas = soup.find_all("table", class_="match-table")

    resultados = []
    for tabela in tabelas:
        titulo = tabela.find_previous("h2")
        if not titulo or "results" not in titulo.text.lower():
            continue

        linhas = tabela.find_all("tr")
        for linha in linhas:
            if "event-header-cell" in linha.get("class", []):
                continue

            if "team-row" in linha.get("class", []):
                data_tag = linha.find("span", {"data-unix": True})
                if data_tag:
                    unix_time = int(data_tag["data-unix"]) // 1000
                    data_formatada = datetime.fromtimestamp(unix_time).strftime("%d/%m")
                else:
                    data_formatada = "??/??"

                adversario_tag = linha.find("a", class_="team-2") or linha.find("span", class_="team-2")
                adversario = adversario_tag.get_text(strip=True) if adversario_tag else "Desconhecido"

                placar_tag = linha.find("div", class_="score-cell")
                placar = placar_tag.text.strip() if placar_tag else "?"

                try:
                    s_furia, s_enemy = map(int, placar.split(":"))
                    emoji = "✅" if s_furia > s_enemy else "❌"
                except:
                    emoji = "⚔"


                resultados.append(f"{emoji} {data_formatada} — FURIA {placar} {adversario}")

            if len(resultados) == 5:
                break

    if not resultados:
        return "😕 Nenhum resultado recente encontrado."

    return "📊 Últimos 5 jogos da FURIA:<br><br>" + "<br>".join(resultados)

# Função para ver se a furia está jogando no momento
def status_ao_vivo_furia():
    url = "https://www.hltv.org/matches"
    scraper = cloudscraper.create_scraper()
    resposta = scraper.get(url)

    if resposta.status_code != 200:
        return "😕 Erro ao acessar o site da HLTV."

    soup = BeautifulSoup(resposta.text, "html.parser")
    partidas_ao_vivo = soup.find_all("div", class_="liveMatch")

    for partida in partidas_ao_vivo:
        equipes = partida.find_all("div", class_="matchTeamName")
        if not equipes or len(equipes) < 2:
            continue

        time1 = equipes[0].get_text(strip=True)
        time2 = equipes[1].get_text(strip=True)

        if "FURIA" in time1 or "FURIA" in time2:
            placar = partida.find("div", class_="matchScore")
            mapa = partida.find("div", class_="matchMeta")
            link_tag = partida.find("a", class_="a-reset")
            link = f"https://www.hltv.org{link_tag['href']}" if link_tag else "Link indisponível"

            return (
                f"🎮 Partida ao vivo da FURIA!\n"
                f"🆚 {time1} vs {time2}\n"
                f"📊 Placar: {placar.get_text(strip=True) if placar else 'Indisponível'}\n"
                f"🗺 Mapa: {mapa.get_text(strip=True) if mapa else 'Indisponível'}\n"
                f"🔗 <a href='{link}' target='_blank'>Acompanhe ao vivo</a>"
            )

    return "📭 A FURIA não está jogando no momento."

# Lista com mais de 20 perguntas que podem ser sugeridas
PERGUNTAS_SUGERIDAS = [
    "Quando é o próximo jogo da FURIA?",
    "Quem é o Fallen da FURIA?",
    "Quem é o novo AWP do time?",
    "Qual o mapa mais jogado pela FURIA?",
    "Qual foi o resultado do último jogo da FURIA?",
    "Quem fundou a FURIA?",
    "Quem é o treinador atual da FURIA?",
    "Qual é a lineup atual?",
    "Onde assistir aos jogos da FURIA?",
    "Quem é o capitão do time?",
    "Quantos títulos a FURIA tem?",
    "Quando o FalleN entrou na FURIA?",
    "Quem é o jogador mais experiente da equipe?",
    "Como posso jogar na FURIA?",
    "Quando a FURIA foi fundada?",
    "Qual é o estilo de jogo da FURIA?",
    "Qual foi o primeiro campeonato da FURIA?",
    "Quem é YEKINDAR?",
    "Molodoy é brasileiro?",
    "Quem são os riflers da FURIA?",
    "O que significa FURIA?",
]

# Função para responder às mensagens
def responder(mensagem):
    msg = normalizar_texto(mensagem)

    # Resposta padrão com perguntas aleatórias sugeridas
    def resposta_padrao():
        sugestoes = random.sample(PERGUNTAS_SUGERIDAS, 5)
        resposta = "🤔 Não entendi muito bem... Pergunte sobre os jogadores, a história ou o próximo jogo da FURIA! 🎮"
        resposta += "<br><br>Você pode tentar perguntar:<br>"
        for pergunta in sugestoes:
            resposta += f"• {pergunta}<br>"
        return resposta


    # Resposta para questões sobre quem é um jogador
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

    # Respostas para o tokens Quais
    if "Quais" in msg or "Quanto":
        if "resultado" in msg or "jogos" in msg:
            return buscar_ultimos_resultados_furia()

    # Resposta para questões sobre quando algo aconteceu
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
            return buscar_proximo_jogo_furia()

    # Resposta para questões sobre porque algo aconteceu
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

    # Resposta para questões sobre qual informação
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
            return "📊 A FURIA está atualmente no Top 17 do ranking da HLTV (dados de 2025)."
        if "origem" in msg or "nome" in msg:
            return "🐾 O nome FURIA representa intensidade e garra — pilares da filosofia competitiva do time!"
        if "proximojogo" in msg:
            return buscar_proximo_jogo_furia()

    # Resposta para questões sobre como algo aconteceu
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

    # Respostas sobre onde assistir
    if any(x in msg for x in ["assistir", "ver", "transmitido", "onde passa", "passa o jogo"]):
        return ("📺 BOTA NO GAU! Você pode assistir aos jogos da FURIA ao vivo no canal do Gaules na Twitch!\n"
            '<br><br>👉 <a href="https://www.twitch.tv/gaules" target="_blank">twitch.tv/gaules</a>')

    # Referencia ao contato inteligente
    if "whatsapp" in msg or "contato" in msg or "suporte" in msg or "ajuda" in msg:

        return ("📲 Você pode testar o Contato Inteligente da FURIA via WhatsApp!<br>"

            "👉 <a href='https://wa.me/5511993404466' target='_blank'>Clique aqui para abrir o WhatsApp</a><br>"

            "⚠ Disponível apenas para alguns torcedores em beta fechado.")
    
    # Resposta para status ao vivo
    if any(x in msg for x in ["jogo ao vivo", "partida ao vivo", "furia jogando agora", "status ao vivo", "está jogando", "jogando agora"]):
        return status_ao_vivo_furia()
    

    # Respostas por função dentro do time
    if any(x in msg for x in ["IGL", "igl", "Capitão"]):
        return "🎯 FalleN é o IGL (líder de jogo) da FURIA. 🧠"
    if any(x in msg for x in ["awp", "awper", "sniper"]):
        return "🧊 Molodoy é o AWP principal da FURIA. Mira fria e muito clutch! 🔭"
    if any(x in msg for x in ["entry", "entry fragger", "inicia"]):
        return "⚔ YEKINDAR costuma ser o entry fragger — o primeiro a abrir o bombsite com agressividade."
    if "rifler" in msg:
        return ("💥 KSCERATO e Yuurih são os riflers principais da FURIA.\n"
                "Consistência, impacto e domínio nos duelos! 💣")
    if any(x in msg for x in ["suporte", "apoio"]):
        return "🛡 FalleN e Yuurih também desempenham funções de suporte tático na FURIA."
    if "lurker" in msg:
        return "🕶 KSCERATO costuma ser o lurker da FURIA — ele pega os adversários de surpresa nas rotações!"
    if "clutch" in msg:
        return "🔐 KSCERATO e Molodoy são clutchers natos — sangue frio no fim de round!"
    if "coach" in msg or "treinador" in msg:
        return "🧠 Sidnei 'sidde' Macedo é o atual treinador da FURIA no CS2."

    # Respostas sobre redes sociais
    if any(x in msg for x in ["instagram", "insta"]):
        return "📸 Instagram oficial da FURIA: <a href='https://www.instagram.com/furiagg/' target='_blank'>@furiagg</a>"

    if any(x in msg for x in ["twitter", "x", "tweet"]):
        return "🐦 Perfil oficial da FURIA no X (antigo Twitter): <a href='https://twitter.com/furia' target='_blank'>@furia</a>"

    if "tiktok" in msg:
        return "🎵 TikTok da FURIA: <a href='https://www.tiktok.com/@furiagg' target='_blank'>@furiagg</a>"

    if any(x in msg for x in ["youtube", "yt"]):
        return "📺 Canal no YouTube da FURIA: <a href='https://www.youtube.com/@FURIAggCS' target='_blank'>youtube.com/furiagg</a>"

    if "twitch" in msg:
        return "🎮 Transmissões ao vivo na Twitch: <a href='https://www.twitch.tv/furiatv' target='_blank'>twitch.tv/furiatv</a>"


    # Resposta para "quais redes sociais"
    if any(x in msg for x in ["redes sociais", "contatos oficiais", "quais redes", "instagram", "twitter", "x", "tiktok", "youtube", "twitch"]):
        return (
                "🌐 Aqui estão as redes sociais oficiais da FURIA:<br><br>"
                "📸 <a href='https://www.instagram.com/furiagg/' target='_blank'>Instagram</a><br>"
                "🐦 <a href='https://twitter.com/furia' target='_blank'>X / Twitter</a><br>"
                "🎵 <a href='https://www.tiktok.com/@furiagg' target='_blank'>TikTok</a><br>"
                "📺 <a href='https://www.youtube.com/@FURIAggCS' target='_blank'>YouTube</a><br>"
                "🎮 <a href='https://www.twitch.tv/furiatv' target='_blank'>Twitch</a><br>"
                )

    # Resposta padrão caso a mensagem não seja identificada
    return resposta_padrao()
