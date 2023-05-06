const inputs = document.querySelectorAll("input");
const sparkles = document.querySelectorAll(".sparkle");
const wheelOne = document.querySelector(".wheel-one");
const wheelTwo = document.querySelector(".wheel-two");
const wheelThree = document.querySelector(".wheel-three");
const wheels = document.querySelectorAll(".wheel");
const letters = document.querySelectorAll(".letters");
const letterbT = document.querySelector(".letter-b-T");
const letterbO = document.querySelector(".letter-b-O");
const letterbO2 = document.querySelector(".letter-b-O2");
const letterbL = document.querySelector(".letter-b-L");
const letterbS = document.querySelector(".letter-b-S");
const lettersB = document.querySelectorAll(".letters-b");
const jumpingLetters = document.querySelectorAll(".let");
const form = document.querySelector("form");
const error = document.querySelector(".error");
let isBroken = false;
let animationInMotion = false;


const jumpingAnimation = () => {
    for (let i = 0; i < jumpingLetters.length; i++) {
        setTimeout(() => {
            if(isBroken) return;
            jumpingLetters[i].classList.add("jump");
        }, i * 100);
    }
    jumpingLetters.forEach(letter => {
        letter.classList.remove("jump");
    })
}

const jumpingAnimationReverse = () => {
    for (let i = jumpingLetters.length - 1; i + 1 > 0; i--) {
        setTimeout(() => {
            if(isBroken) return;
            jumpingLetters[i].classList.add("jump");
        }, (jumpingLetters.length - i) * 100);
    }
    jumpingLetters.forEach(letter => {
        letter.classList.remove("jump");
    })
}

const toolJump = () => {
    lettersB.forEach(letter => {
        letter.classList.add("jump");
    })
    setTimeout(() => {
        lettersB.forEach(letter => {
            letter.classList.remove("jump");
        })
    }, 200);

}

const fallingLetters = () => {
    letterbT.classList.remove("back-Tb");
    letterbO.classList.remove("back-Ob");
    letterbO2.classList.remove("back-Ob2");
    letterbL.classList.remove("back-Lb");
    letterbS.classList.remove("back-Sb");

    letterbT.classList.add("falling-tools");
    letterbO.classList.add("falling-tools");
    letterbO2.classList.add("falling-tools");
    letterbL.classList.add("falling-tools");        
    letterbS.classList.add("falling-S-b");
    
    sparkles.forEach(sparkle => {
        sparkle.classList.add("display-block");
    })

    letters.forEach(letter => {
        letter.classList.remove("letters-shadow");
    })

    setTimeout(() => {
        letterbT.classList.remove("falling-tools");
        letterbO.classList.remove("falling-tools");
        letterbO2.classList.remove("falling-tools");
        letterbL.classList.remove("falling-tools");

        
        letterbT.classList.add("falling-T-b");
        letterbO.classList.add("falling-O-b");
        letterbO2.classList.add("falling-O-b2");
        letterbL.classList.add("falling-L-b");
        
        setTimeout(() => {
            animationInMotion = false;
        }, 1500);
    }, 300);
}

const backLetters = () => {
    letterbT.classList.remove("falling-T-b");
    letterbO.classList.remove("falling-O-b");
    letterbO2.classList.remove("falling-O-b2");
    letterbL.classList.remove("falling-L-b");
    letterbS.classList.remove("falling-S-b");

    letterbT.classList.add("back-Tb");
    letterbO.classList.add("back-Ob");
    letterbO2.classList.add("back-Ob2");
    letterbL.classList.add("back-Lb");
    letterbS.classList.add("back-Sb");

    sparkles.forEach(sparkle => {
        sparkle.classList.remove("display-block");
    })

    letters.forEach(letter => {
        letter.classList.add("letters-shadow");
    })

    setTimeout(() => {
        letterbT.classList.remove("back-Tb");
        letterbO.classList.remove("back-Ob");
        letterbO2.classList.remove("back-Ob2");
        letterbL.classList.remove("back-Lb");
        letterbS.classList.remove("back-Sb");
        isBroken = false;
    }, 1000);
}

const backAnimation = () => {
    if(animationInMotion) return;
    backLetters();
}

const brokenAnimation = () => {
    isBroken = true;
    animationInMotion = true;
    jumpingLetters.forEach(letter => {
        letter.classList.remove("jump");
    })
    fallingLetters();
}

const inputAnimation = (input) => {
    const top = input.nextElementSibling;
    const side = top.nextElementSibling
    const bottomOne = side.nextElementSibling;
    const bottomTwo = bottomOne.nextElementSibling;
    const label = input.previousElementSibling;
    const icon = label.previousElementSibling;

    label.classList.remove("white");
    side.classList.remove('white-bgc');
    top.classList.remove('white-bgc');
    bottomTwo.classList.remove('white-bgc');

    icon.style.borderRight = "none";
    label.classList.add("active-label");
    top.style.width = "10%";
    side.classList.remove('white-bgc');
    bottomOne.classList.add("bottom-active");
    bottomTwo.classList.add("bottom-active");
}

const clearInputAnimation = (input) => {
    const top = input.nextElementSibling;
    const side = top.nextElementSibling
    const bottomOne = side.nextElementSibling;
    const bottomTwo = bottomOne.nextElementSibling;
    const label = input.previousElementSibling;
    const icon = label.previousElementSibling;

    if(input.value === "") {
        setTimeout(() => {
            side.classList.add('white-bgc');
        }, 220);
        icon.style.borderRight = "1px solid white";
        label.classList.remove("active-label");
        top.style.width = "0%";
        bottomOne.classList.remove("bottom-active");
        bottomTwo.classList.remove("bottom-active");
    } else {
        label.classList.add("white");
        side.classList.add('white-bgc');
        top.classList.add('white-bgc');
        bottomTwo.classList.add('white-bgc');
    }
}   

setInterval(() => {
    wheelOne.classList.toggle("reverse-animation");
    wheelTwo.classList.toggle("reverse-animation");
    wheelThree.classList.toggle("reverse-animation");
}, 10000);

setTimeout(() => {
    jumpingAnimation();
    setInterval(() => {
        if(!isBroken && wheelOne.classList.contains("reverse-animation")) {
            jumpingAnimationReverse();
        } else if(!isBroken && !wheelOne.classList.contains("reverse-animation")) {
            jumpingAnimation();
        }
    }, 5000);
}, 2500);

inputs.forEach(input => {
    input.addEventListener("focus", () => {
        inputAnimation(input);
    })
    input.addEventListener("blur", () => {
        clearInputAnimation(input);
    })
})

lettersB.forEach(letter => {
    letter.addEventListener("click", () => {
        brokenAnimation();
    })
})

wheels.forEach(wheel => {
    wheel.addEventListener("click", () => {
        if(isBroken){
            backAnimation();
        } else {
            toolJump();
        }
    })   
})

if(inputs[1].value !== "") {
    inputAnimation(inputs[1]);
    clearInputAnimation(inputs[1]);
}

if(error.textContent.trim() !== "") {
    brokenAnimation();
}