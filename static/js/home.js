const slides = document.querySelector('.slides');
const imagens = document.querySelectorAll('.imagem_carrossel');

let index = 0;

function mostrarSlide() {
    slides.style.transform = `translateX(-${index * 100}%)`;

}

setInterval(() => {

    index++;

    if (index >= imagens.length){
        index = 0;

    }

    mostrarSlide();

}, 5000)