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
const quoteResult = document.getElementById("quoteResult");

//Obtener la lista de los artistas
async function getDataArtist() {
  //let url = "http://18.231.188.212/api/v1/artists";
  try {
    const respuesta = await fetch("../front/artist.json");
    console.log(respuesta.status);
    if (respuesta.status === 200) {
      listArtist = await respuesta.json();
      renderArtist();
    }
  } catch (error) {
    console.log(error);
  }
}

// seleccionar  y renderizar la informacion del artista
function renderArtist() {
  artist = listArtist.find((element) => element.name === "Vanessa");
  const artistInfo = `
  <div class="row">
    <div class="col-12 col-md-6 mb-1">
      <label for="artistname" class="pb-0">Name</label>
      <input type="text" id="artistname" class="form-control form-control-sm" value=${artist.name} placeholder="First name" aria-label="First name" readonly />
    </div>
    <div class="col-12 col-md-6 mb-1">
      <label for="whatsapp" class="pb-0">WhatsApp</label>
      <input type="text" id="whatsapp" class="form-control form-control-sm" value=${artist.phone} placeholder="Last name" aria-label="Last name" readonly />
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

  const artistBody = artist.body
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
    artist_id: artist.id,
    data: {
      user: {
        name: userName.value,
        mail: userMail.value,
        phone: userPhone.value,
      },
      quotation: {
        style: selectStyle.value,
        body: selectBody.value,
        size: selectSize.value,
        image: quotationImage.value,
        description: quotationDescription.value,
      },
    },
  };
  const url = "http://18.231.188.212api/v1/quotation/create";
  let response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataQuotation),
  })
    .then((response) => response.json()) // respuesta no se puede leer, se tranforma en json
    .then((respuestaJson) => {
      console.log("respuesta", respuestaJson);
      renderQuotation();
    })
    .catch((razon) => {
      console.log("enviar datos fallo, razon:", razon);
    });
  console.log(dataQuotation);
}

function renderQuotation() {
  const responseQuotation = {
    time: "2:00h",
    price: "350.000",
  };
  const quotationInfo = `
  <div class="row py-3">
  <div class="col-12 col-md-6 mb-1">
    <label for="estimatedTime" class="pb-0 fs-4">Estimated time</label>
    <input type="text" id="estimatedTime" class="form-control form-control-sm fs-5" value=${responseQuotation.time} placeholder="Estimated time" aria-label="Estimated time" readonly />
  </div>
  <div class="col-12 col-md-6 mb-1">
    <label for="estimatedPrice" class="pb-0 fs-4">Estimated price</label>
    <input type="text" id="estimatedPrice" class="form-control form-control-sm fs-5" value=${responseQuotation.price} placeholder="Estimated price" aria-label="Estimated price" readonly />
  </div>
</div>`;
  quoteResult.innerHTML = quotationInfo;
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
