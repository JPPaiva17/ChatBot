# 🐾 Chatbot FURIA | Pantera

Este é um chatbot interativo sobre a equipe de CS2 da FURIA, com respostas divertidas, emojis personalizados e interface própria. Você pode perguntar sobre a história da FURIA, seus jogadores e o próximo jogo. 🧠🎮

## 🔧 Tecnologias utilizadas

- **Python (Flask)** – para a lógica de backend  
- **HTML/CSS/JavaScript** – para a interface web  
- **Emojis** – para respostas mais expressivas e amigáveis 😄

---

## 💬 Funcionalidades

- Responde perguntas como:
  - "Quem é o coach da FURIA?"
  - "Quando o FalleN entrou?"
  - "pq a FURIA mudou a lineup?"
  - "cm a FURIA foi fundada?"
- Trata variações e abreviações comuns: `pq`, `cm`, `qnd`, `prox jogo`, etc.
- Exibe tooltip “Como posso te ajudar?” ao passar o mouse sobre o ícone do bot 🧞‍♂️

---

## 🗂 Estrutura de pastas

```
📁 projeto/
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

- Conectar com API da HLTV ou Liquipedia para dados ao vivo
- Adicionar histórico de mensagens
- Versão mobile responsiva
- Respostas com voz (text-to-speech)

---

## 🤝 Contribuindo

Sinta-se livre para enviar pull requests ou sugestões! Este projeto é uma forma divertida de aprender Flask e frontend com um tema que a gente ama: CS! 🔫

---

## 📄 Licença

MIT License © 2025 Laura Braga de Menezes
