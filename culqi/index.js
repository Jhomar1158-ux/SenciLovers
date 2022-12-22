Culqi.publicKey = ''; //Agregar llave pública

Culqi.settings({
    title: 'Senci Device',
    currency: 'PEN',
    description: 'Transacción SenciLover',
    amount: 3500,
    order: 'ord_live_0CjjdWhFpEAZlxlz'
 });

 Culqi.options({
  lang: "auto",
  installments: false, // Habilitar o deshabilitar el campo de cuotas
  paymentMethods: {
    tarjeta: true,
    yape: false, 
    bancaMovil: false,
    agente: false,
    billetera: false,
    cuotealo: false,
  },
  style: {
      logo: 'https://culqi.com/LogoCulqi.png',
      maincolor: '#0ec1c1',
      buttontext: '#ffffff',
      maintext: '#4A4A4A',
      desctext: '#4A4A4A'
    }
});

const btn_pagar = document.getElementById('btn_pagar');
btn_pagar.addEventListener('click', function (e) {
    // Abre el formulario con la configuración en Culqi.settings y CulqiOptions
    console.log("Hola Senci!")
    Culqi.open();
    e.preventDefault();
})
function culqi() {
    if (Culqi.token) {  // ¡Objeto Token creado exitosamente!
      const token = Culqi.token;
      console.log(`Se ha creado el objeto Token: ${token}.`);
      //En esta linea de codigo debemos enviar el "Culqi.token.id"
      //hacia tu servidor con Ajax
    } else if (Culqi.order) {  // ¡Objeto Order creado exitosamente!
      const order = Culqi.order;
      console.log(`Se ha creado el objeto Order: ${order}. para PagoEfectivo`);
      
    } else {
      // Mostramos JSON de objeto error en consola
      console.log(`Error : ${Culqi.error.merchant_message}.`);
    }
  };