# 🐾 Chatbot FURIA | Pantera

Este é um chatbot interativo sobre a equipe de CS2 da FURIA, com respostas divertidas, emojis personalizados e interface própria. Você pode perguntar sobre a história da FURIA, seus jogadores e o próximo jogo. 🧠🎮

## 🔧 Tecnologias utilizadas

- **Python (Flask)** – para a lógica de backend  
- **HTML/CSS/JavaScript** – para a interface web 

---

## 💬 Funcionalidades

- Responde perguntas como:
  - "Quem é o coach da FURIA?"
  - "Quando o FalleN entrou?"
  - "pq a FURIA mudou a lineup?"
  - "cm a FURIA foi fundada?"
- Trata variações e abreviações comuns: `pq`, `cm`, `qnd`, `prox jogo`, etc.
- Exibe tooltip “Como posso te ajudar?” ao passar o mouse sobre o ícone do bot 🧞‍♂️
- Obtém:
  - ✅ **Próximo jogo da FURIA** diretamente da [HLTV.org](https://www.hltv.org/) com `BeautifulSoup`
  - ✅ **Últimos 5 resultados da FURIA**, também via scraping
  - ✅ **Status ao vivo** de partidas da FURIA em andamento

---

## 🗂 Estrutura de pastas

```
📁 ChatBotFuria/
├── app.py                # Backend Flask
├── chatbot.py            # Lógica e respostas do bot
├── pagina/
│   ├── index.html        # Interface principal
│   ├── style.css         # Estilo da interface
│   ├── script.js         # Lógica do chat
│   └── imagens/
│       └── pantera.png   # Avatar do bot
```

---

## ▶️ Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/chatbot-furia.git
   cd chatbot-furia
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install flask
   ```

3. Rode a aplicação:
   ```bash
   python app.py
   ```

4. Acesse pelo navegador:
   ```
   http://localhost:5000
   ```

---

## 📦 Futuras melhorias

- Versão mobile responsiva
- Respostas com voz (text-to-speech)

---


## 🖼️ Fotos do ChatBot

<p align="left">
  Abaixo está a imagem utilizada como avatar do Pantera, o bot oficial da FURIA:
</p>

<img src="https://github.com/user-attachments/assets/d6e8e019-ece9-4058-a607-d7ade830efcb" alt="Pantera" width="250"/>

<br><br>

<p align="left">
  Aqui estão algumas fotos da interface de funcionamento:
</p>

<img src="https://github.com/user-attachments/assets/b3d06aa2-665b-484e-93f0-4e5c7b98145a" alt="Interface 1" width="500"/>
<br><br>
<img src="https://github.com/user-attachments/assets/ac952458-0837-4eb3-8ae8-337853211595" alt="Interface 2" width="500"/>
<br><br>
<img src="https://github.com/user-attachments/assets/85665065-4a68-4cca-9242-b72aea5450df" alt="Interface 3" width="500"/>


## 📄 Licença

MIT License © 2025 João Pedro Paiva
