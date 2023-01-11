let provider = "retiroSimple";
const sendData20 = document.querySelector(".sendData20");
const sendData15 = document.querySelector(".sendData15");
const sendData10 = document.querySelector(".sendData10");
const sendData5 = document.querySelector(".sendData5");
const sendData2 = document.querySelector(".sendData2");

console.log("INGRESÓ")
sendData20.addEventListener("click", () =>{ 
    console.log(sendData20.firstElementChild.innerHTML)
    let numberButton = sendData20.firstElementChild.innerHTML;
    sendDataToFlask(provider, numberButton.split("s/").join(''))
})

sendData15.addEventListener("click", () =>{ 
    console.log(sendData15.firstElementChild.innerHTML)
    let numberButton = sendData15.firstElementChild.innerHTML;
    sendDataToFlask(provider, numberButton.split("s/").join(''))
})
sendData10.addEventListener("click", () =>{ 
    console.log(sendData10.firstElementChild.innerHTML)
    let numberButton = sendData10.firstElementChild.innerHTML;
    sendDataToFlask(provider, numberButton.split("s/").join(''))
})
sendData5.addEventListener("click", () =>{ 
    console.log(sendData5.firstElementChild.innerHTML)
    let numberButton = sendData5.firstElementChild.innerHTML;
    sendDataToFlask(provider, numberButton.split("s/").join(''))
})
sendData2.addEventListener("click", () =>{ 
    console.log(sendData2.firstElementChild.innerHTML)
    let numberButton = sendData2.firstElementChild.innerHTML;
    sendDataToFlask(provider, numberButton.split("s/").join(''))
})


function sendDataToFlask(provider,monto){
    console.log("send data to python")
    const dict_values = {provider, monto}
    const s = JSON.stringify(dict_values);
    $.ajax({
        url:"/retiro-monto",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)
    });
    window.location.href = "http://127.0.0.1:5000/loader";
}
