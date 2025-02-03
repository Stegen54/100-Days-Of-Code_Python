document.querySelectorAll('.link-item').forEach(link => {
  link.addEventListener('click', function() {
    this.style.transform = 'scale(0.95)';
    setTimeout(() => {
      this.style.transform = 'scale(1)';
    }, 100);
    
    // Optional: Track clicks
    console.log(`Clicked: ${this.textContent}`);
  });
});
