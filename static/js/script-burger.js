const button = document.querySelector(".burger-btn");
const nav = document.querySelector(".nav-burger");
let allNavItems = document.querySelectorAll(".dropdown-item");
let itemButton = document.querySelectorAll(".button-burger");
let menuItem = document.querySelectorAll(".burger-item");
let dropdown = document.querySelectorAll(".dropdown");
// let dropdown = document.querySelectorAll('.dropdown-burger')

const navTransform = () => {
	nav.classList.toggle("nav--active");

	if (nav.classList.contains("nav--active")) {
		burgerRemoveFocus();
		button.classList.add("burger-btn-click");
	} else {
		button.classList.remove("burger-btn-click");
	}

	navAnimation();
};

const navAnimation = () => {
	let delayTime = 0;

	menuItem.forEach((navItem) => {
		navItem.classList.toggle("nav-animation");
		navItem.style.animationDelay = "." + delayTime + "s";
		delayTime++;
	});
};

const burgerButtons = function () {
	const dropdown = this.nextElementSibling;

	if (!dropdown.classList.contains("dropdown-focused")) {
		burgerRemoveFocus();
		dropdown.classList.add("dropdown-focused");
	} else {
		dropdown.classList.remove("dropdown-focused");
	}
};

const burgerRemoveFocus = () => {
	dropdown.forEach((animation) => {
		console.log("2");
		animation.classList.remove("dropdown-focused");
	});
};

const removeAll = () => {
	burgerRemoveFocus();
	button.classList.remove("burger-btn-click");
	nav.classList.remove("nav--active");
};

button.addEventListener("click", () => {
	navTransform();
});

itemButton.forEach((burger) => {
	burger.addEventListener("click", burgerButtons);
});

// document.addEventListener("click", function (event) {
//   if(!event.target.closest(".nav-burger")) {
//     removeAll();
//   }
// });
