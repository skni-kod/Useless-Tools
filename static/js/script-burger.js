const button = document.querySelector('.burger-btn');
const nav = document.querySelector('.nav-burger');
let allNavItems = document.querySelectorAll('.dropdown-item');
let itemButton = document.querySelectorAll('.button-burger');
let menuItem = document.querySelectorAll('.burger-item');

const navTransform = () => {
  nav.classList.toggle('nav--active');
  
  if(nav.classList.contains('nav--active')){
    button.classList.add('burger-btn-click')
  } else {
    button.classList.remove('burger-btn-click')
  }

  navAnimation();
};

const navAnimation = () => {
  let delayTime = 0;

  menuItem.forEach(navItem => {
    navItem.classList.toggle('nav-animation')
    navItem.style.animationDelay = '.' + delayTime + 's';
    delayTime++;
  })
}

button.addEventListener('click', () => {
  navTransform();
});

