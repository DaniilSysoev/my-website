const buttons = document.querySelectorAll('.base-button')

for (let index = 0; index < buttons.length; index++) {
    const button = buttons[index];
    button.addEventListener('mouseover', shake);
    button.addEventListener('mouseout', stopshake);

    function shake(event){
        button.classList.add('animate__animated', 'animate__headShake')
    }
    
    function stopshake(event){
        button.classList.remove('animate__animated', 'animate__headShake')
    }
}

const logo = document.querySelector('.logo')
logo.addEventListener('mousemove', startrotate)
logo.addEventListener('mouseout', stoprotate)

function startrotate(event){
    const logoItem = this.querySelector('.logo-item');
    const halfHeight = logoItem.offsetHeight / 2;
    logoItem.style.transform = 'rotateX(' + -(event.offsetY - halfHeight) + 'deg) rotateY(' + (event.offsetX - halfHeight) + 'deg)';
}

function stoprotate(event){
    const logoItem = this.querySelector('.logo-item');
    logoItem.style.transform = "rotate(0)";
}
