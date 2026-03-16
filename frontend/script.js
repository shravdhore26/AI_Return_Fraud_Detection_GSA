async function predict(){

if(
num_returns.value=="" ||
refund_amount.value=="" ||
time_gap.value=="" ||
mismatch.value=="" ||
category_risk.value=="" ||
loyalty.value=="" ||
reason_pattern.value==""
){

alert("Please fill all input fields")
return

}

let data={

num_returns:Number(num_returns.value),
refund_amount:Number(refund_amount.value),
time_gap:Number(time_gap.value),
mismatch:Number(mismatch.value),
category_risk:Number(category_risk.value),
loyalty:Number(loyalty.value),
reason_pattern:Number(reason_pattern.value)

}

let res=await fetch("http://127.0.0.1:8000/predict",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)

})

let result=await res.json()

let score=Math.round(result.fraud_probability_percent)

animateScore(score)

let label=""
let color=""

/* UPDATED THRESHOLDS */

if(score < 30){

label="SAFE"
color="green"

}

else if(score < 70){

label="SUSPICIOUS"
color="orange"

}

else{

label="FRAUD"
color="red"

}

document.getElementById("label").innerText=label
document.getElementById("label").style.color=color
document.getElementById("score").style.color=color

let alertBox=document.getElementById("alertBox")

if(score >= 70){

alertBox.style.display="block"

}
else{

alertBox.style.display="none"

}

animateGauge(score,color)

let exp=await fetch("http://127.0.0.1:8000/explain",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)

})

let explanation=await exp.json()

document.getElementById("explain").innerText=explanation.explanation

}



function randomCase(){

num_returns.value=Math.floor(Math.random()*8)

refund_amount.value=Math.floor(Math.random()*5000)

time_gap.value=Math.floor(Math.random()*20)+1

mismatch.value=Math.floor(Math.random()*2)

category_risk.value=Math.floor(Math.random()*5)+1

loyalty.value=Math.floor(Math.random()*10)+1

reason_pattern.value=Math.floor(Math.random()*2)

}



function resetForm(){

num_returns.value=""
refund_amount.value=""
time_gap.value=""
mismatch.value=""
category_risk.value=""
loyalty.value=""
reason_pattern.value=""

document.getElementById("score").innerText="0%"
document.getElementById("label").innerText="Prediction"

document.getElementById("alertBox").style.display="none"

const canvas=document.getElementById("gauge")
const ctx=canvas.getContext("2d")

ctx.clearRect(0,0,320,220)

document.getElementById("explain").innerText=""

}



function animateScore(target){

let current=0

let interval=setInterval(()=>{

current++

document.getElementById("score").innerText=current+"%"

if(current>=target){

clearInterval(interval)

}

},10)

}



function animateGauge(score,color){

let progress=0

let interval=setInterval(()=>{

progress++

drawGauge(progress,color)

if(progress>=score){

clearInterval(interval)

}

},10)

}



function drawGauge(score,color){

const canvas=document.getElementById("gauge")
const ctx=canvas.getContext("2d")

ctx.clearRect(0,0,320,220)

ctx.beginPath()
ctx.arc(160,190,120,Math.PI,2*Math.PI)
ctx.strokeStyle="#ddd"
ctx.lineWidth=25
ctx.stroke()

let angle=(score/100)*Math.PI

ctx.beginPath()
ctx.arc(160,190,120,Math.PI,Math.PI+angle)
ctx.strokeStyle=color
ctx.lineWidth=25
ctx.stroke()

}