const earth = document.getElementById("earth")
const dateButton = document.getElementById("id_birth_date")
const datePicker = document.getElementById("datePicker")
const ellipse = document.getElementById("ellipse")
const card = document.querySelector(".data-card")
const showDate = document.querySelector(".show-date")
const dateConfirm = document.querySelector(".confirm")

let isPressing = false

const earthSize = 40
const horizontalRadius = 150
const verticalRadius = 73
const horizontalMargin = 25
const verticalMargin = 10

const activeData = () =>{
  card.classList.toggle("data-active");
}

const mousedown = () =>{
  isPressing = true
}

const mouseup = () => {
  isPressing = false
}

const dateFromDay = day => {
  let date = new Date(year, 0)
  return new Date(date.setDate(day))
}

const addZero = num =>{
  return num<10?"0"+num:num
}

const isLeapyear = () => {
  return (year % 100 === 0) ? (year % 400 === 0) : (year % 4 === 0)
}

const mousemove = e => {
  if(!isPressing)
    return
  
  const { clientX, clientY } = e.touches != null ? e.touches[0] : e
  
  const rect = ellipse.getBoundingClientRect()
  const ellipseCenterX = rect.x + rect.width/2 + horizontalMargin
  const ellipseCenterY = rect.y + rect.height/2 + verticalMargin
  angle = Math.atan2(ellipseCenterY - clientY, clientX - ellipseCenterX)

  let x = horizontalRadius*Math.cos(angle)
  let y = verticalRadius*Math.sin(angle)

  earth.setAttribute("x", horizontalRadius + x - earthSize/2 + horizontalMargin)
  earth.setAttribute("y", verticalRadius - y - earthSize/2 + verticalMargin)

  let oldDate = date

  let dayNumber = ((182.5 + (isLeapyear()?0.5:0))*(Math.sin((angle)/2) + 1) + 1)

  date = dateFromDay(dayNumber)

  if(oldDate.getDate() == 1 && oldDate.getMonth() == 0 && date.getDate() == 31 && date.getMonth() == 11){
    year--
  }else if(oldDate.getDate() == 31 && oldDate.getMonth() == 11 && date.getDate() == 1 && date.getMonth() == 0){
    year++
  }
  
  dayNumber = ((182.5 + (isLeapyear()?0.5:0))*(Math.sin((angle)/2)+1)+1)
  date = dateFromDay(dayNumber)

  if(date.getTime() > today.getTime()){
    showDate.textContent = "Jesteś z przyszłości?" 
  }else{
    showDate.textContent = addZero(date.getDate()) + "-" + addZero(date.getMonth() + 1) + "-" + date.getFullYear()
    dateButton.value = showDate.textContent
  }
}

const dataPicker = () => {
    let today = new Date()
    let year = today.getFullYear()
    let start = new Date(today.getFullYear(), 0, 0)
    let diff = today - start
    const oneDay = 1000 * 60 * 60 * 24
    let dayNumber = Math.floor(diff / oneDay)
    let date = dateFromDay(dayNumber)

    let angle = 2*Math.asin(((dayNumber-1)/(182.5 + (isLeapyear()?0.5:0)))-1)
    let x = horizontalRadius*Math.cos(angle)
    let y = verticalRadius*Math.sin(angle)

    earth.setAttribute("x",horizontalRadius + x - earthSize/2 + horizontalMargin)
    earth.setAttribute("y",verticalRadius - y - earthSize/2 + verticalMargin)

    showDate.textContent = addZero(date.getDate()) + "-" + addZero(date.getMonth()+1) + "-" + date.getFullYear()

    earth.addEventListener("mousedown", mousedown)
    earth.addEventListener("touchstart", mousedown)

    document.addEventListener("mousemove", mousemove)
    document.addEventListener("touchmove", mousemove)

    document.addEventListener("mouseup", mouseup)
    document.addEventListener("touchend", mouseup)

    dateButton.addEventListener("click", activeData)
    dateConfirm.addEventListener("click", () => {
      activeData()
      checkInputs()
    })
}

document.addEventListener("DOMContentLoaded", dataPicker)