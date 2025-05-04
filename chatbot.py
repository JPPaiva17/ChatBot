# Decidi criar o chatbot do zero sem auxilio de inteligencia artificial

def responder(mensagem):
    mensagem = mensagem.lower()

    # Perguntas do Tipo QUEM

    if "quem" in mensagem and ("fallen" in mensagem or "gabriel" in mensagem or "toledo" in mensagem):
        return "FalleN, nome verdadeiro Gabriel Toledo, é um dos maiores ícones do CS brasileiro. Bicampeão mundial com a SK Gaming, atualmente é o capitão da FURIA, conhecido por sua liderança, AWP precisa e papel fundamental no crescimento do CS no Brasil."


    if "quem" in mensagem and ("kscerato" in mensagem or "kaike" in mensagem or "cerato" in mensagem):
        return "KSCERATO, nome verdadeiro Kaike Cerato, é um dos riflers mais consistentes do mundo e está na FURIA desde 2018. Ele é um jogador crucial para a equipe, com sua habilidade precisa e leitura de jogo."


    if "quem" in mensagem and ("yuurih" in mensagem or "yuri" in mensagem or "santos" in mensagem):
        return "Yuurih, nome verdadeiro Yuri Santos, é conhecido por sua agressividade controlada e está na FURIA desde 2018. Ele é uma peça-chave no time, sempre trazendo grande impacto nas partidas."


    if "quem" in mensagem and ("molodoy" in mensagem or "Danil" in mensagem or "Golubenko" in mensagem):
        return ("Molodoy, nome verdadeiro Danil Golubenko, é um jovem awper cazaque que se juntou à FURIA em 2025. "
            "Ele é conhecido por sua habilidade com a AWP e por trazer uma nova energia ao time. "
            "Antes de ingressar na FURIA, Molodoy era membro da Amkal, uma equipe cazaque de destaque.")


    if "quem" in mensagem and ("yekindar" in mensagem or "mareks" in mensagem or "galinskis" in mensagem):
        return ("YEKINDAR, nome verdadeiro Mareks Gaļinskis, é um jogador letão conhecido por sua agressividade e estilo explosivo. "
            "Ele se destacou na Virtus.pro e Team Liquid antes de se juntar à FURIA em 2025. "
            "Ele foi eleito o 8º melhor jogador do mundo em 2021 e é reconhecido por sua habilidade de entrada e clutchs decisivos.")


    if "quem" in mensagem and "fundou" in mensagem:
        return "A FURIA foi fundada por Jaime 'raizen' Pádua e André Akkari em 2017."

    if "quem" in mensagem and ("coach" in mensagem or "sidde" in mensagem or "sid" in mensagem):
        return (
        "Sid 'sidde' Macedo é o atual treinador principal da FURIA no Counter-Strike 2. "
        "Ele assumiu o cargo em julho de 2024, após a saída de Nicholas 'guerri' Nogueira, "
        "que agora ocupa a função de Head de Esports da organização. "
        "Sidde, que anteriormente atuava como assistente técnico, foi promovido ao cargo de head coach "
        "e trouxe uma nova dinâmica à equipe, com foco em estratégias inovadoras e liderança jovem. "
        "Ele conta com o apoio dos assistentes internacionais Hunter 'Lucid' Tucker e Viacheslav 'innersh1ne' Britvin. "
        "Sidde tem uma trajetória sólida no cenário brasileiro, com passagens por equipes como Redemption POA, Liberty e ODDIK."
    )

    # Perguntas do tipo QUANDO

    if "quando" in mensagem and "criada" in mensagem:
        return "A FURIA foi criada em 2017."

    if "quando" in mensagem and "fallen" in mensagem and "entrou" in mensagem:
        return "FalleN entrou na FURIA em julho de 2023."

    if "quando" in mensagem and "próximo jogo" in mensagem:
        return "O próximo jogo da FURIA é amanhã às 18h contra a NAVI."

    if "quando" in mensagem and "major" in mensagem:
        return "A FURIA jogou seu primeiro Major no IEM Katowice 2019."

    if "quando" in mensagem and "yekindar" in mensagem and "entrou" in mensagem:
        return "Yekindar entrou na FURIA em fevereiro de 2025."

    # Perguntas do tipo PORQUE

    if "por que" in mensagem and "fallen" in mensagem and "furia" in mensagem:
        return "FalleN entrou na FURIA em 2023 para trazer experiência, liderança e tática ao time."

    if "por que" in mensagem and "yekindar" in mensagem:
        return "Yekindar saiu da Liquid buscando um novo desafio e alinhamento com seu estilo de jogo."

    if "por que" in mensagem and "mudou" in mensagem and "line" in mensagem:
        return "A FURIA mudou sua line para renovar o elenco e buscar melhores resultados internacionais."

    if "por que" in mensagem and "furia" in mensagem and "agressiva" in mensagem:
        return "A agressividade é marca registrada da FURIA desde o início, sufocando os adversários."
    
    # Perguntas do tipo QUAL

    if "qual" in mensagem and "line"  in mensagem:
        return "Line-up 2025: FalleN, Yuurih, KSCERATO, Yekindar e Molodoy."

    if "qual" in mensagem and "função" in mensagem and "fallen" in mensagem:
        return "FalleN é IGL  e suporte da FURIA."

    if "qual" in mensagem and "estilo" in mensagem and "yekindar" in mensagem:
        return "Yekindar é um entry fragger agressivo, famoso por abrir espaços com confiança."

    if "qual" in mensagem and "ranking" in mensagem:
        return "A FURIA está atualmente no top 15 do ranking HLTV (dados de 2025)."

    if "qual" in mensagem and "origem" in mensagem:
        return "O nome FURIA representa intensidade e garra, pilares da mentalidade competitiva do time."

    # perguntas do tipo COMO

    if "como" in mensagem and "começou" in mensagem and "furia" in mensagem:
        return "A FURIA nasceu em 2017 com a missão de revolucionar os esports no Brasil."

    if "como" in mensagem and "jogar" in mensagem and "furia" in mensagem:
        return "Para jogar na FURIA, você precisa se destacar no cenário competitivo e ter mentalidade alinhada ao time."

    if "como" in mensagem and "estreia" in mensagem:
        return "A estreia da FURIA em grandes torneios internacionais foi em 2019, no Major de Katowice."

    if "como" in mensagem and "treina" in mensagem:
        return "A FURIA treina com uma rotina intensa de táticos, deathmatch e análise de partidas."

    if "como" in mensagem and "estilo" in mensagem:
        return "A FURIA é conhecida por seu estilo agressivo e jogadas explosivas lideradas por arT."



print(responder(pergunta))