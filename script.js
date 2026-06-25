const likeBtn = document.getElementById('likeBtn');
const dislikeBtn = document.getElementById('dislikeBtn');

function showBigEmoji(message) {
    const emoji = document.createElement('div');
    emoji.className = 'big-emoji';
    emoji.textContent = message;
    document.body.appendChild(emoji);

    emoji.addEventListener('animationend', () => {
        emoji.remove();
    });
}

likeBtn?.addEventListener('click', () => {
    showBigEmoji('😍');
});

dislikeBtn?.addEventListener('click', () => {
    showBigEmoji('🤬');
});
