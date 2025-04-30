// Efecto de animación para cuando se hace scroll
document.addEventListener('scroll', () => {
    let scrollPosition = window.scrollY;
    
    if (scrollPosition > 200) {
      document.querySelector('.hero-section').classList.add('scrolled');
    } else {
      document.querySelector('.hero-section').classList.remove('scrolled');
    }
  });
  