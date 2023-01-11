const STRIPE_PUBLIC_KEY='pk_test_51MObzkBYbqa2B3argHpjQOqAhndSEvm1ppOU22HN9YPIJiJlYGOvtKMjo0PiIFbX1SbPzci4hwxaKJg8v1hmdgQw00EemmEz46'
const STRIPE_PRIVATE_KEY='sk_test_51MObzkBYbqa2B3arq3ZkDHrxRXitxVzyeNMGE7zsEz4qaEb6gSFD4fUB9BibemudPJVSCmAMZh3W8DhY8J8rekAh00CKzcArQR'

const $d = document;
const $arepas = $d.getElementById("arepas");
const $template = $d.getElementById("arepa-template").content;
const $fragment = $d.createDocumentFragment();
const options = { headers: {Authorization: `Bearer ${STRIPE_PRIVATE_KEY}`}}
const FormatoDeMoneda = num => `$${num.slice(0, -2)}.${num.slice(-2)}`;

let products, prices;

Promise.all([
    fetch("https://api.stripe.com/v1/products", options),
    fetch("https://api.stripe.com/v1/prices", options)
])
.then(responses => Promise.all(responses.map(res => res.json())))
.then(json => {
    products = json[0].data;
    prices = json[1].data;
    prices.forEach(el => {
        let productData = products.filter(product => product.id === el.product);
        
        $template.querySelector(".arepa").setAttribute("data-price", el.id);
        $template.querySelector("img").src = productData[0].images[0];
        $template.querySelector("img").alt = productData[0].name;
        $template.querySelector("figcaption").innerHTML = `${productData[0].name} ${FormatoDeMoneda(el.unit_amount_decimal)} ${(el.currency).toUpperCase()}`;

        let $clone = $d.importNode($template, true);

        $fragment.appendChild($clone);
    });

    $arepas.appendChild($fragment);
})
.catch(error => {
    let message = error.statuText || "Ocurrió un error en la petición";

    $arepas.innerHTML = `Error: ${error.status}: ${message}`;
})

$d.addEventListener("click", e => {
    if (e.target.matches(".arepas *")) {
        let priceId = e.target.parentElement.getAttribute("data-price");

        Stripe(STRIPE_PUBLIC_KEY).redirectToCheckout({
            lineItems: [{
                price: priceId,
                quantity: 1
            }],
            mode: "payment",
            successUrl:"http://127.0.01:5500/pago/success",
            cancelUrl:"http://127.0.0.1:5500/pago/fail"
        })
        .then(res => {
            if (res.error){
                $arepas.insertAdjacentElement("afterend", res.error.message)
            }
        })
    }
})