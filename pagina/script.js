function enviarMensagem() {
    let mensagem = document.getElementById("input-message").value;
    if (mensagem.trim() === "") return;

    // Adiciona a mensagem do usuário na interface
    adicionarMensagem(mensagem, 'usuario');

    // Limpa o campo de entrada
    document.getElementById("input-message").value = '';

    // Envia a mensagem para o backend (Flask)
    fetch('/mensagem', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'mensagem=' + encodeURIComponent(mensagem)
    })
    .then(response => response.json())
    .then(data => {
        // Adiciona a resposta do chatbot na interface
        adicionarMensagem(data.resposta, 'chatbot');
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function adicionarMensagem(mensagem, autor) {
    const chatBox = document.getElementById('chat-box');
    const novaMensagem = document.createElement('div');
    novaMensagem.classList.add(autor); // Adiciona a classe 'usuario' ou 'chatbot'
    novaMensagem.textContent = mensagem;
    chatBox.appendChild(novaMensagem);

    // Rolagem automática para o final
    chatBox.scrollTop = chatBox.scrollHeight;
}
