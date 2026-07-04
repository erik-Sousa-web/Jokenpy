async function jogar(escolha) {

    const resposta = await fetch("/jogar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            jogada: escolha
        })
    });

    const dados = await resposta.json();

    document.getElementById("resultado").innerHTML =
        `
        Você escolheu: <strong>${escolha}</strong><br><br>
        Computador escolheu: <strong>${dados.computador}</strong><br><br>
        <strong>${dados.resultado}</strong>
        `;
}