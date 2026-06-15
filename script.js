// White mouse cursor and heart counter

const whiteCursor = document.createElement('div');
whiteCursor.id = 'white-cursor';
whiteCursor.style.cssText = `
  position: fixed;
  width: 24px;
  height: 24px;
  border: 2px solid white;
  border-radius: 50%;
  pointer-events: none;
  z-index: 10000;
  box-shadow: 0 0 8px rgba(255, 255, 255, 0.6);
`;
document.body.appendChild(whiteCursor);

document.addEventListener('mousemove', (e) => {
  whiteCursor.style.left = (e.clientX - 12) + 'px';
  whiteCursor.style.top = (e.clientY - 12) + 'px';
});

document.addEventListener('mouseover', (e) => {
  if (['INPUT', 'TEXTAREA', 'SELECT', 'BUTTON'].includes(e.target.tagName)) {
    whiteCursor.style.opacity = '0';
  }
});

document.addEventListener('mouseout', (e) => {
  if (['INPUT', 'TEXTAREA', 'SELECT', 'BUTTON'].includes(e.target.tagName)) {
    whiteCursor.style.opacity = '1';
  }
});

let heartCount = 0;

function createStaticHearts(e) {
  const centerX = e.pageX || window.innerWidth / 2;
  const centerY = e.pageY || window.innerHeight / 2;
  const radius = 80;

  for (let i = 0; i < 8; i++) {
    const heart = document.createElement('div');
    heart.className = 'flying-heart';
    heart.textContent = '❤️';
    
    const angle = (i / 8) * Math.PI * 2;
    const x = centerX + Math.cos(angle) * radius;
    const y = centerY + Math.sin(angle) * radius;
    
    heart.style.left = x + 'px';
    heart.style.top = y + 'px';
    
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 1000);
  }

  // Increment counter
  heartCount++;
  document.getElementById('count').textContent = heartCount;
}

// Attach hearts to all buttons
document.addEventListener('click', (e) => {
  const btn = e.target.closest('.action-btn');
  if (btn) {
    createStaticHearts(e);
  }
});

console.log('%c⚽ Bienvenue au stade !', 'color: #ffd700; font-size: 16px; font-weight: bold;');
