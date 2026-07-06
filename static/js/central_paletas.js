const inputPesquisa = document.querySelector(".input_busca");
const cards = document.querySelectorAll(".card_polaroid");
const card_notificacao = document.querySelector(".notificacao_paletas");

card_notificacao.style.display = "none";

inputPesquisa.addEventListener("input", function () {
    const termo = inputPesquisa.value.toLowerCase();
    let verifica_encontrou_paleta = false;

    cards.forEach(card => {
        const nome = card.querySelector(".nome_paleta").textContent.toLowerCase();
        const codigo = card.querySelector(".codigo_cor").textContent.toLowerCase();

        if (nome.includes(termo) || codigo.includes(termo)) {
            card.style.display = "flex";
            verifica_encontrou_paleta = true
        } else {
            card.style.display = "none";
        }
    });
    if (!verifica_encontrou_paleta && termo !== "") {
        //se encontrou a paleta ele oculta o card_notificação, se não ele mostra o card_notificação
        card_notificacao.style.display = "block";
    } else {
        card_notificacao.style.display = "none";
    }
});