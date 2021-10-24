let listArtist = [];
let artistInformation = document.getElementById("artistInformation");
let userName = document.getElementById("userName");
let userMail = document.getElementById("userMail");
let userPhone = document.getElementById("userPhone");
let artist = {};
let selectStyle = document.getElementById("selectStyle");
let selectBody = document.getElementById("selectBody");
let selectSize = document.getElementById("selectSize");
let quotationImage = document.getElementById("quotationImage");
let quotationDescription = document.getElementById("quotationDescription");
const makeQuote = document.getElementById("makeQuote");
const secctionQuoteResult = document.getElementById("secctionQuoteResult");

//Obtener la lista de los artistas
async function getDataArtist() {
  let url = "http://54.233.163.4/api/v1/artists/"
  try {
    const respuesta = await fetch(url);
    console.log(respuesta.status);
    if (respuesta.status === 200) {
      listArtist = await respuesta.json();
      console.log(listArtist);
      renderArtist();
    }
  } catch (error) {
    console.log(error);
  }
}

// seleccionar  y renderizar la informacion del artista
async function renderArtist() {
  let url = `http://54.233.163.4/api/v1/artists/${listArtist[0].id}`;
  try {
    let response = await fetch(url);
    if (response.status === 200) {
      artist = await response.json();
      console.log(artist);
    }
  } catch (error) {
    console.log(error);
  }
  console.log('El artista es: ', artist)
  const artistInfo = `
  <div class="row">
    <div class="col-12 col-md-6 mb-1">
      <label for="artistname" class="pb-0">Name</label>
      <input type="text" id="artistname" class="form-control form-control-sm" value="${artist.name}" placeholder="First name" aria-label="First name" readonly />
    </div>
    <div class="col-12 col-md-6 mb-1">
      <label for="whatsapp" class="pb-0">WhatsApp</label>
      <input type="text" id="whatsapp" class="form-control form-control-sm" value="${artist.phone}" placeholder="Last name" aria-label="Last name" readonly />
    </div>
  </div>
  <div class="row">
    <div class="col mb-3">
      <label for="address" class="pb-0">Address</label>
      <input type="text" class="form-control form-control-sm" id="address"
      value="${artist.address}" placeholder="Address" aria-label="Address" readonly />
    </div>
  </div>
  `;

  const artistStyles = artist.styles
    .map((style, indice) => `<option value="${style}">${style}</option>`)
    .join("");
  artistRenderStyles = `<option disable hidden value="">Styles</option>`.concat(
    "",
    artistStyles
  );

  const artistBody = artist.body_part
    .map(
      (bodyPart, indice) => `<option value="${bodyPart}">${bodyPart}</option>`
    )
    .join("");
  artistRenderBody =
    `<option disable hidden value="">Body part</option>`.concat("", artistBody);

  /*Insert info */
  artistInformation.innerHTML = artistInfo;
  selectStyle.innerHTML = artistRenderStyles;
  selectBody.innerHTML = artistRenderBody;
}

async function sendDataQuotation(event) {
  event.preventDefault();
  const dataQuotation = {
    "artist_id": {
      "id": artist.id
    },
    "user": {
      "name": userName.value,
      "mail": userMail.value,
      "phone": userPhone.value
    },
    "quotation": {
      "style": selectStyle.value,
      "body_part": selectBody.value,
      "size": selectSize.value,
      "description": quotationDescription.value
    }
  }

  const url = "http://54.233.163.4/api/v1/quotation/create";
  let response = await fetch(url, {
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "body": JSON.stringify(dataQuotation)
  })
    .then((response) => response.text()) // respuesta no se puede leer, se tranforma en json
    .then((respuestaJson) => {
      console.log("respuesta", respuestaJson);
      renderQuotation(respuestaJson);
    })
    .catch((razon) => {
      console.log("enviar datos fallo, razon:", razon);
    });
  console.log(dataQuotation);
}

function renderQuotation(dataQuotation) {
  let responseQuotation = JSON.parse(dataQuotation);
  const quotationInfo = `
  <h6 class="mb-4 text-center fs-1">Quote Result</h6>
  <div class="mb-3 px-3" id="quoteResult">
    <div class="row py-3">
      <div class="col-12 col-md-6 mb-1">
        <label for="estimatedTime" class="pb-0 fs-4">Estimated time</label>
        <input type="text" id="estimatedTime" class="form-control form-control-sm fs-5" value="${responseQuotation.time}" placeholder="Estimated time" aria-label="Estimated time" readonly />
      </div>
      <div class="col-12 col-md-6 mb-1">
        <label for="estimatedPrice" class="pb-0 fs-4">Estimated price</label>
        <input type="text" id="estimatedPrice" class="form-control form-control-sm fs-5" value="${responseQuotation.price}" placeholder="Estimated price" aria-label="Estimated price" readonly />
      </div>
      <small id="emailHelp" class="form-text text-muted ">This is a price and an approximate time of the session of your tattoo, the artist will decide the final price, which can vary between <spam class="fw-bold">+50,000 COP and -50,000 COP</spam></small>
    </div>
  </div>`;
  secctionQuoteResult.innerHTML = quotationInfo;
}

getDataArtist();
makeQuote.onclick = sendDataQuotation;
/*
[x] Obtener la lista de los artistas
[x] seleccionar  y renderizar la informacion del artista
[x] Obtener los datos del usuario y de la cotizacion desde el formulario
[x] enviar la informacion
[] mostrar el resultado de la cotizacion


*/
