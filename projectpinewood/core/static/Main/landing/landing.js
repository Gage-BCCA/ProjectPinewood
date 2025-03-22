document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.carousel-track');
    if (!track) return;
    const slides = Array.from(track.children);
    const nextButton = document.querySelector('.btn-right');
    const prevButton = document.querySelector('.btn-left');
    const slideWidth = slides[0].getBoundingClientRect().width;
    
    slides.forEach((slide, index) => {
      slide.style.left = `${slideWidth * index}px`;
    });
    // lord help me
    const moveSlide = (current, target) => {
      track.style.transform = `translateX(-${target.style.left})`;
      current.classList.remove('current-slide');
      target.classList.add('current-slide');
    };
    
    nextButton.addEventListener('click', () => {
      const current = track.querySelector('.current-slide');
      let next = current.nextElementSibling || slides[0];
      moveSlide(current, next);
    });
    
    prevButton.addEventListener('click', () => {
      const current = track.querySelector('.current-slide');
      let prev = current.previousElementSibling || slides[slides.length - 1];
      moveSlide(current, prev);
    });
  });
  