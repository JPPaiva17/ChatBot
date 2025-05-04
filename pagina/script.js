// Função para exibir as mensagens no chat
function exibirMensagem(mensagem, autor) {
    const chatBox = document.getElementById("chat-box");
    const mensagemElement = document.createElement("div");

    if (autor === "bot") {
        // Mensagem do bot
        const botElement = document.createElement("div");
        botElement.classList.add("bot");

        const imgElement = document.createElement("img");
        const botImageURL = document.getElementById("bot-image-url").dataset.url;
        imgElement.src = botImageURL;
        imgElement.alt = "Pantera";

        const mensagemTextElement = document.createElement("div");
        mensagemTextElement.classList.add("mensagem");
        mensagemTextElement.innerText = mensagem;

        botElement.appendChild(imgElement);
        botElement.appendChild(mensagemTextElement);
        mensagemElement.appendChild(botElement);
    } else {
        // Mensagem do usuário
        const userElement = document.createElement("div");
        userElement.classList.add("user");

        const userTextElement = document.createElement("div");
        userTextElement.classList.add("mensagem");
        userTextElement.innerText = mensagem;

        userElement.appendChild(userTextElement);
        mensagemElement.appendChild(userElement);
    }

    chatBox.appendChild(mensagemElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Função para enviar mensagem do usuário
function enviarMensagem() {
    const inputMessage = document.getElementById("input-message").value;
    if (inputMessage.trim() === "") return;

    exibirMensagem(inputMessage, "user");
    document.getElementById("input-message").value = "";

    fetch('/mensagem', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'mensagem=' + encodeURIComponent(inputMessage)
    })
    .then(response => response.json())
    .then(data => {
        exibirMensagem(data.resposta, "bot");
    });
}

// Mensagem inicial do bot
function mensagemInicial() {
    const mensagem = "Olá! Eu sou o Pantera, seu assistente de CS. Estou aqui para responder suas perguntas sobre a FURIA. Como posso te ajudar?";
    exibirMensagem(mensagem, "bot");
}

// Mostrar a mensagem inicial
window.onload = function() {
    mensagemInicial();
};
