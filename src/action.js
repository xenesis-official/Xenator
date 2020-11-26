const clickToChangeBackground = document.querySelector('button')
const body = document.querySelector('body')

clickToChangeBackground.addEventListener("click", () => { 
    body.classList.toggle('clicked');
    clickToChangeBackground.classList.toggle('clicked-btn');
 }
);