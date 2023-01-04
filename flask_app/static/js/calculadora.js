let currentNum = "";
let provider = "calculadora";
const currentDisplayNumber = document.querySelector(".currentNumber");
const numberButtons = document.querySelectorAll(".number");
const decimal = document.querySelector(".decimal");
decimal.addEventListener("click", () => {
  addDecimal();
});
const sendData = document.querySelector(".sendData");
sendData.addEventListener("click", () =>{

})

console.log("INGRESÓ")
numberButtons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      handleNumber(e.target.textContent);
    });
});

function handleNumber(number) {
    if ((currentNum == "" || currentNum.includes(".")) && currentNum.length <3 ) {
      currentNum += number;
      currentDisplayNumber.textContent = currentNum;
    }else{
        sendDataToFlask(provider, currentNum)
    }
}

function addDecimal() {
    if (!currentNum.includes(".")) {
      currentNum += ".";
      currentDisplayNumber.textContent = currentNum;
    }
}

function sendDataToFlask(provider,currentNum){
    console.log("send data to python")
    const dict_values = {provider, currentNum}
    const s = JSON.stringify(dict_values);
    window.alert(s)
    $.ajax({
        url:"/retiro-monto",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)
    });
}
