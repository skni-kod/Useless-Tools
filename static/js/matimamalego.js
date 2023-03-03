// password
const plusBtn = document.querySelector('.plus');
const minusBtn = document.querySelector('.minus');
const copyBtn = document.querySelector('.copy-btn');
let lengthInput = document.querySelector('.range-slider');
let length = document.querySelector('.choosed-length');
let password = document.querySelector('.password-text');

var messageElement = document.getElementById('myMessage');

const passwordStrengthElement = document.querySelector('.password');

//clipboard
const textItem = new ClipboardItem({
	'text/plain': new Blob([password.textContent], { type: 'text/plain' }),
});

function add() {
	lengthInput.stepUp(1);
	console.log('pawel');
	length.textContent = lengthInput.value;
	passwordStrength();
}
function subtraction() {
	lengthInput.stepDown(1);
	console.log('pawel');
	length.textContent = lengthInput.value;
	passwordStrength();
}
function copyPassword() {
	navigator.clipboard.write([textItem]);
	messageElement.innerHTML = 'Skopiowano hasło do schowka';
	messageElement.classList.remove('dnone');

	setTimeout(function () {
		messageElement.classList.add('dnone');
	}, 1500);
}
function passwordStrength() {
	if (lengthInput.value < 7) {
		passwordStrengthElement.classList.remove('yellow');
		passwordStrengthElement.classList.add('red');
		passwordStrengthElement.classList.remove('green');
	} else if (lengthInput.value >= 7 && lengthInput.value < 12) {
		passwordStrengthElement.classList.add('yellow');
		passwordStrengthElement.classList.remove('red');
		passwordStrengthElement.classList.remove('green');
	} else if (lengthInput.value >= 12) {
		passwordStrengthElement.classList.remove('yellow');
		passwordStrengthElement.classList.remove('red');
		passwordStrengthElement.classList.add('green');
	}
}

plusBtn.addEventListener('click', add);
minusBtn.addEventListener('click', subtraction);
copyBtn.addEventListener('click', copyPassword);

lengthInput.addEventListener('input', passwordStrength);
