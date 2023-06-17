function sha1(text) {
  function rotateLeft(n, s) {
    return (n << s) | (n >>> (32 - s));
  }

  function toHex(value) {
    var hex = "";
    for (var i = 7; i >= 0; i--) {
      hex += ((value >> (i * 4)) & 0xf).toString(16);
    }
    return hex;
  }

  function preprocess(text) {
    var utf8Text = unescape(encodeURIComponent(text));
    var data = new Uint8Array(utf8Text.length);
    for (var i = 0; i < utf8Text.length; i++) {
      data[i] = utf8Text.charCodeAt(i);
    }
    return data;
  }

  function hash(data) {
    var h0 = 0x67452301;
    var h1 = 0xefcdab89;
    var h2 = 0x98badcfe;
    var h3 = 0x10325476;
    var h4 = 0xc3d2e1f0;

    var paddingSize = ((data.length + 8) >>> 6) + 1;
    var paddedData = new Uint8Array(paddingSize * 64);
    paddedData.set(data);

    paddedData[data.length] = 0x80;

    var messageLength = data.length * 8;
    paddedData[paddedData.length - 4] = (messageLength >>> 24) & 0xff;
    paddedData[paddedData.length - 3] = (messageLength >>> 16) & 0xff;
    paddedData[paddedData.length - 2] = (messageLength >>> 8) & 0xff;
    paddedData[paddedData.length - 1] = messageLength & 0xff;

    for (var i = 0; i < paddedData.length; i += 64) {
      var w = new Uint32Array(80);
      for (var j = 0; j < 16; j++) {
        w[j] =
          (paddedData[i + j * 4] << 24) |
          (paddedData[i + j * 4 + 1] << 16) |
          (paddedData[i + j * 4 + 2] << 8) |
          (paddedData[i + j * 4 + 3] << 0);
      }
      for (var j = 16; j < 80; j++) {
        w[j] = rotateLeft(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1);
      }

      var a = h0;
      var b = h1;
      var c = h2;
      var d = h3;
      var e = h4;

      for (var j = 0; j < 80; j++) {
        var f, k;
        if (j < 20) {
          f = (b & c) | (~b & d);
          k = 0x5a827999;
        } else if (j < 40) {
          f = b ^ c ^ d;
          k = 0x6ed9eba1;
        } else if (j < 60) {
          f = (b & c) | (b & d) | (c & d);
          k = 0x8f1bbcdc;
        } else {
          f = b ^ c ^ d;
          k = 0xca62c1d6;
        }

        var temp = rotateLeft(a, 5) + f + e + k + w[j];
        e = d;
        d = c;
        c = rotateLeft(b, 30);
        b = a;
        a = temp;
      }

      h0 += a;
      h1 += b;
      h2 += c;
      h3 += d;
      h4 += e;
    }

    return toHex(h0) + toHex(h1) + toHex(h2) + toHex(h3) + toHex(h4);
  }

  var data = preprocess(text);
  return hash(data);
}


function auth(){
    //Login
    var login = "2d9eaf1e662518756a3d78806543af5b"
    console.log("Paso login")

    var uuidv4 = function() {
      var result = '';
      var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
      var charactersLength = characters.length;
      for (var i = 0; i < 32; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
      }
      return result;
    };
    
    // Uso de uuidv4 para generar un UUID
    var nonce = uuidv4();
    console.log(nonce);

    //Creamos la variable 'nonce'
    console.log("paso uuid")

    // Uso de uuidv4
    //var { v4: uuidv4 } = require('uuid');

    //Con el unique id nos aseguramos de tener una cadena unica
    let nonceB64 = btoa(nonce.toString());
    console.log(nonceB64)
    console.log("Creo nonceb64")
    
    //Creamos la variable 'seed'
    var seed = new Date().toISOString();
    console.log(seed)
    console.log("paso seed")

    //Creamos la variable 'secretkey'
    var secretkey = "3YC5brb5eAR4xBGQ"
    console.log("paso secretkey")

    //Creamos la 'trankey'
    trankey_woc = nonce + seed + secretkey //woc = with out codify

    //Codificamos primero a SHA1 y luego a encriptamos en Base64
    var hash = sha1(trankey_woc);
    console.log(hash);
    var base64 = btoa(hash.toString());
    console.log(base64);
    console.log("paso crypto")

    //Importamos la libreria para poder calcular días futuros
    var currentDate = new Date();

// Agregar 3 días a la fecha actual
var futureDate = new Date(currentDate.getTime() + (3 * 24 * 60 * 60 * 1000));

// Obtener los componentes de la fecha futura
var year = futureDate.getFullYear();
var month = String(futureDate.getMonth() + 1).padStart(2, '0');
var day = String(futureDate.getDate()).padStart(2, '0');
var hours = String(futureDate.getHours()).padStart(2, '0');
var minutes = String(futureDate.getMinutes()).padStart(2, '0');
var seconds = String(futureDate.getSeconds()).padStart(2, '0');
var timezoneOffset = futureDate.getTimezoneOffset();
var timezoneOffsetHours = Math.abs(Math.floor(timezoneOffset / 60)).toString().padStart(2, '0');
var timezoneOffsetMinutes = (Math.abs(timezoneOffset) % 60).toString().padStart(2, '0');
var timezoneSign = timezoneOffset < 0 ? '+' : '-';

// Construir la cadena de fecha y hora en el formato deseado
var formattedDateTime = `${year}-${month}-${day}T${hours}:${minutes}:${seconds}${timezoneSign}${timezoneOffsetHours}:${timezoneOffsetMinutes}`+'Z';

console.log(formattedDateTime);
    console.log("paso fecha")


    const requestData = {
        locale: "es_CO",
        auth: {
          login: login,
          tranKey: base64,
          nonce: nonceB64,
          seed: seed
        },
        payer: {
          document: "1122334455",
          documentType: "CC",
          name: "Brayan",
          surname: "Luján",
          company: "Evertec",
          email: "test_mail@app.com",
          mobile: "+573111111111",
          address: {
            street: "Calle falsa 123",
            city: "Medellín",
            state: "Poblado",
            postalCode: "55555",
            country: "Colombia",
            phone: "+573111111111"
          }
        },
        payment: {
          reference: "1122334455",
          description: "Prueba",
          amount: {
            currency: "COP",
            total: 10000
          }
        },
        expiration: formattedDateTime,
        returnUrl: "https://commerce.test/return",
        ipAddress: "127.0.0.1",
        userAgent: "PlacetoPay Sandbox"
      };
      
      // Utiliza el objeto requestData según tus necesidades
      return requestData
}

function request(){
    console.log("gays")
    data = auth()
    console.log("gays2")

    const url = 'https://checkout-test.placetopay.com/api/session/2345275';

    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(result => {
        console.log("gays3")
        console.log(result);
      })
    .catch(error => {
      console.log("gays4")
      console.error('Error:', error);
    });
}

