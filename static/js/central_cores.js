const inputPesquisa = document.querySelector(".input_busca");
const cards = document.querySelectorAll(".card_cor");
const card_notificacao = document.querySelector(".notificacao_cores");

//Aqui eu estou escondendo o card de notifição, e vou mostrado somente se a cor procurada não for encontrada
card_notificacao.style.display = "none";

inputPesquisa.addEventListener("input", function () {
    const termo = inputPesquisa.value.toLowerCase();
    let verifica_encontrou_cor = false;

    cards.forEach(card => {
        const nome = card.querySelector(".nome_cor").textContent.toLowerCase();
        const codigo = card.querySelector(".codigo_cor").textContent.toLowerCase();

        if (nome.includes(termo) || codigo.includes(termo)) {
            card.style.display = "flex";
            verifica_encontrou_cor = true;
        } else {
            card.style.display = "none";
        }
    });
    if (!verifica_encontrou_cor && termo !== "") {
        //se encontrou a cor ele oculta o card_notificação, se não ele mostra o card_notificação
        card_notificacao.style.display = "block";
    } else {
        card_notificacao.style.display = "none";
    }
});