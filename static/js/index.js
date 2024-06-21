const texts = [
    "РАЗРАБОТКА ТЕХНОЛОГИЧНЫХ САЙТОВ",
    "МОБИЛЬНЫХ ПРИЛОЖЕНИЙ",
    "ДИЗАЙН ПРОЕКТОВ"
];
const speed = 50; // Скорость печатания в миллисекундах

function typeText(text, element) {
    let i = 0;
    function typing() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, speed);
        }
    }
    typing();
}

document.addEventListener("DOMContentLoaded", function() {
    const firstWord = document.querySelector('.first_word');
    const secondWord = document.querySelector('.second_word');
    const thirdWord = document.querySelector('.theard_word');

    typeText(texts[0], firstWord);
    setTimeout(() => typeText(texts[1], secondWord), texts[0].length * speed);
    setTimeout(() => typeText(texts[2], thirdWord), (texts[0].length + texts[1].length) * speed);
});
