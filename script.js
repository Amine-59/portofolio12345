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

document.addEventListener('click', (e) => {
  const btn = e.target.closest('.action-btn');
  if (btn) {
    heartCount += 1;
    document.getElementById('count').textContent = heartCount;
  }
});

console.log('%c⚽ Bienvenue au stade !', 'color: #ffd700; font-size: 16px; font-weight: bold;');
