var url ="https://docs.google.com/spreadsheets/d/15s0iFAmgE3yegdEB9XL7Er3F06AU3ZvqFKVIbj0pWUs/edit?usp=sharing";
function doPost(e){
   Logger.log("Funcion doPost Ingreso : la fecha y hora: " + new Date());
   var operacion = JSON.parse(e.postData.contents)
   var respuesta = "";
    var jo = {};
    if (operacion.op == "listar"){
      var result={};
      var ss=SpreadsheetApp.openByUrl(url);
      var sheet =ss.getSheetByName("Mensajes");
      var jo = {};
      var dataArray = [];
      var rows = sheet.getRange(2,1,sheet.getLastRow()-1, sheet.getLastColumn()).getValues();
      for(var i = rows.length-1; i >= 0 ; i--){
        var dataRow = rows[i];
        var record = {};
        record['fecha'] = dataRow[0];
        record['mensaje'] = dataRow[1];
        record['persona'] = dataRow[2];
        record['monto'] = dataRow[3];
        dataArray.push(record);    
    }
    jo.status = '0';
    jo.message = 'Exito';
    jo.content = dataArray;
    }
 return ContentService.createTextOutput(JSON.stringify(jo)).setMimeType(ContentService.MimeType.JSON);
  
}

function doGet(e){

  var callback = e.parameter.callback;
  var operacion = e.parameter.op;
  var respuesta = "";
  if (operacion == "listenersms"){
        
        var mensaje_yape = e.parameter.mensaje;
        var jo = {};
        
        if(mensaje_yape.includes("Yape")){
          jo.status = '0';
          jo.message ="Se registro la listener";  
          var persona = e.parameter.mensaje.split("te")[0].trim().replace("Yape! ","");
          var monto_array = e.parameter.mensaje.split(" ");
          var monto = monto_array[monto_array.length-1];
          let ans = {
            "Fecha":new Date(),
            "mensaje_yape":mensaje_yape,
            "persona":persona,
            "monto":monto,
          };
          const s = JSON.stringify(ans);
          $.ajax({
            url:"http://127.0.0.1:5000/userInfo",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(s)
         });
         }else{
          jo.status = '1';
          jo.message ="no es mensaje valido";
         }
        respuesta = JSON.stringify(jo);
  }
  return ContentService.createTextOutput(callback+'('+ JSON.stringify(respuesta)+')').setMimeType(ContentService.MimeType.JAVASCRIPT);
}