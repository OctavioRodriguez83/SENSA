let currentSlide = 0;
let intervalId;
const cardsPerSlide = window.innerWidth <= 600 ? 1 : (window.innerWidth <= 900 ? 2 : 3);
const cards = document.querySelectorAll('.card-destacado');
const totalSlides = Math.ceil(cards.length / cardsPerSlide);

function mostrarSlide(slide) {
  for (let i = 0; i < cards.length; i++) {
    cards[i].style.display = 'none';
  }
  for (let i = slide * cardsPerSlide; i < (slide + 1) * cardsPerSlide && i < cards.length; i++) {
    cards[i].style.display = 'block';
  }
}
function moverCarrusel(dir) {
  currentSlide += dir;
  if (currentSlide < 0) currentSlide = totalSlides - 1;
  if (currentSlide >= totalSlides) currentSlide = 0;
  mostrarSlide(currentSlide);
  reiniciarIntervalo();
}
function avanzarAutomatico() {
  currentSlide++;
  if (currentSlide >= totalSlides) currentSlide = 0;
  mostrarSlide(currentSlide);
}
function reiniciarIntervalo() {
  clearInterval(intervalId);
  intervalId = setInterval(avanzarAutomatico, 4000); // Cambia cada 4 segundos
}
window.addEventListener('resize', () => location.reload());
document.addEventListener('DOMContentLoaded', () => {
  mostrarSlide(currentSlide);
  intervalId = setInterval(avanzarAutomatico, 4000);
});