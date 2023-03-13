const plusBtn = document.querySelector('.plus');
const minusBtn = document.querySelector('.minus');
const copyBtn = document.querySelector('.copy-btn');
const generateBtn = document.querySelector('generate-btn');
let lengthInput = document.querySelector('.range-slider');
let length = document.querySelector('.choosed-length');
let password = document.querySelector('.password-text');
var messageElement = document.getElementById('myMessage');
const passwordStrengthElement = document.querySelector('.password');
//QUESTIONS
const questionBtns = document.querySelectorAll('.accordion-btn');
const questionTexts = document.querySelectorAll('.accordion-text');

//FUNKCJA BUTTONA OD ZWIEKSZANIA DLUGOSCI HASLA
function add() {
	lengthInput.stepUp(1);
	length.textContent = lengthInput.value;
	passwordStrength();
}
//FUNKCJA BUTTONA OD ZMNIEJSZANIA DLUGOSCI HASLA
function subtraction() {
	lengthInput.stepDown(1);
	length.textContent = lengthInput.value;
	passwordStrength();
}
//FUNKCJA SILY HASLA
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
//FUNCKJA KOPIOWANIA
function passwordCopyMessage() {
	messageElement.innerHTML = 'Skopiowano hasło do schowka';
	messageElement.classList.remove('dnone');

	setTimeout(function () {
		messageElement.classList.add('dnone');
	}, 1500);
}

//QUESTIONS SECTION FUNCTIONS
function removeQuestionsClass() {
	this.nextElementSibling.classList.toggle('accordion-text-d-none');
}
function addQuestionsTitleColor() {
	this.classList.toggle('probe');
}

//WYWOLYWANIE FUNKCJI

plusBtn.addEventListener('click', add);
minusBtn.addEventListener('click', subtraction);
lengthInput.addEventListener('input', passwordStrength);
copyBtn.addEventListener('click', passwordCopyMessage);


for (let i = 0; i < questionBtns.length; i++) {
	questionBtns[i].addEventListener('click', removeQuestionsClass);
}
for (let i = 0; i < questionBtns.length; i++) {
	questionBtns[i].addEventListener('click', addQuestionsTitleColor);
}
