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
let responseQuotation = {}
const makeQuote = document.getElementById("makeQuote");
const secctionQuoteResult = document.getElementById("secctionQuoteResult");
const checkAvailability = document.getElementById("checkAvailability")
let hourDate = ""

const ipServer = "https://api2.rescot.systems"

//Obtener la lista de los artistas
async function getDataArtist() {
  let url = `${ipServer}/api/v1/artists/`
  try {
    const respuesta = await fetch(url);
    if (respuesta.status === 200) {
      listArtist = await respuesta.json();
      renderArtist();
    }
  } catch (error) {
    console.log(error);
  }
}

// seleccionar  y renderizar la informacion del artista
async function renderArtist() {
  let url = `${ipServer}/api/v1/artists/${listArtist[0].id}`;
  try {
    let response = await fetch(url);
    if (response.status === 200) {
      artist = await response.json();
    }
  } catch (error) {
    console.log(error);
  }
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

  const url = `${ipServer}/api/v1/quotation/create`;
  let response = await fetch(url, {
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "body": JSON.stringify(dataQuotation)
  })
    .then((response) => response.json()) // respuesta no se puede leer, se tranforma en json
    .then((respuestaJson) => {
      responseQuotation = respuestaJson;
      renderQuotation(respuestaJson);
    })
    .catch((razon) => {
      console.log("enviar datos fallo, razon:", razon);
    });
}

function renderQuotation(dataQuotation) {
  //let responseQuotation = JSON.parse(dataQuotation);
  const quotationInfo = `
  <h1 class="mb-4 text-center fs-1 first-text" focus>Quote Result</h1>
  <div class="mb-3 px-3" id="quoteResult">
    <div class="row py-3">
      <div class="col-12 col-md-6 mb-1">
        <label for="estimatedTime" class="pb-0 fs-6 fw-bold">Estimated time</label>
        <input type="text" id="estimatedTime" class="form-control form-control-sm fs-6" value="${responseQuotation.time}" placeholder="Estimated time" aria-label="Estimated time" readonly />
      </div>
      <div class="col-12 col-md-6 mb-1">
        <label for="estimatedPrice" class="pb-0 fs-6 fw-bold">Estimated price</label>
        <input type="text" id="estimatedPrice" class="form-control form-control-sm fs-6" value="${responseQuotation.price}" placeholder="Estimated price" aria-label="Estimated price" readonly />
      </div>
      <small id="emailHelp" class="form-text text-muted ">This is a price and an approximate time of the session of your tattoo, the artist will decide the final price, which can vary between <spam class="fw-bold">+50,000 COP and -50,000 COP</spam></small>
    </div>
  </div>`;
  secctionQuoteResult.innerHTML = quotationInfo;
  renderAgenda();
  window.scrollTo(0, document.body.scrollHeight);
}

/*Agenda */
function renderAgenda() {
  const agendaInfo = `
  <h1 class="mb-4 text-center fs-1 first-text">Agenda</h1>
  <div class="mb-3 px-3">
    <div class="row" >
      <div class="col mb-2">
        <label for="chooseDate" class="pb-0">Select a date</label>
        <input type="date" class="form-control" id="chooseDate" required>
      </div>
      <div class="col mb-2 d-grid gap-1 pb-3 pt-3">
        <button type="submit" onclick="sendDateAgenda()" class="btn btn-lg btn-rescot" id="checkAvailability">Check Availability</button>
      </div>
    <div class="row">
      <div class="col-12 col-sm-8 offset-sm-2 mb-2 d-grid gap-2" id="availability">
        <!-- availability  -->
      </div>
    </div>
    </div>
  `;
  const secctionAgenda = document.getElementById("secctionAgenda");
  secctionAgenda.innerHTML = agendaInfo;

}

async function sendDateAgenda(event) {
  //event.preventDefault();
  let [year, month, day] = getDateAgenda();
  const urlAvailability = `${ipServer}/api/v1/calendar/availability`
  const dataAvailability = {
    "year": year,
    "month": month,
    "day": day,
    "total_time": responseQuotation.max_time,
    "quotation_id": responseQuotation.id_quotation
  }
  const responseAvailability = await fetch(urlAvailability, {
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "body": JSON.stringify(dataAvailability)
  })
    .then((response) => response.json())
    .catch((razon) => {
      console.log("enviar datos 'dataAvailability' fallo, razon:", razon);
    });
  renderAvailability(responseAvailability);
}

function getDateAgenda() {
  let date = document.getElementById("chooseDate")
  return date.value.split("-")
}

function renderAvailability(obj) {
  let availabilityInfo = obj.map((hour, indice) => `
  <button type="button" class="p-1 btn btn-lg btn-rescot2 m-2 hour-cls"
  value=${hour} data-bs-toggle="modal" data-bs-target="#exampleModal">
    ${hour}</button>
`).join("");
  const availability = document.getElementById("availability");
  availability.innerHTML = availabilityInfo;
  const hours = document.querySelectorAll(".hour-cls");
  hours.forEach(boton => {
    boton.addEventListener("click", confirmDateHour)
  })

}

function confirmDateHour(event) {
  event.preventDefault();
  let [year, month, day] = getDateAgenda();
  const confirmModal = `
  <p id="contentModal">
  Your appointment with <span class="fw-bold fs-5">${artist.name}</span> will
  be scheduled on the <span class="fw-bold fs-5">${day}th</span> day of the
  <span class="fw-bold fs-">${month}th</span> month of the year
  <span class="fw-bold fs-5">${year}</span> at <span class="fw-bold fs-5">${this.value}.</span>
  <br>
  Remember that the session will last approximately <span class="fw-bold fs-5">${responseQuotation.time}</span>
  <br>
  To confirm click on schedule.
  </p>`;
  let modalBody = document.getElementById("modalBody")
  modalBody.innerHTML = confirmModal;
  let modalSchedule = document.getElementById("modalSchedule")
  modalSchedule.addEventListener("click", createDate)
  hourDate = checkHour(this.value);
}

function checkHour(obj) {
  let hour = obj.split(":")
  let fixHour = "";
  if (hour[0].length < 2) {
    fixHour = "0".concat("", hour[0])
    hour[0] = fixHour;
  }
  return hour.join(":")
}

async function createDate(event) {
  event.preventDefault();
  let [year, month, day] = getDateAgenda();
  const urlCreateDate = `${ipServer}/api/v1/calendar/creation`
  const dataCreateDate = {
    "year": year,
    "month": month,
    "day": day,
    "total_time": responseQuotation.max_time,
    "quotation_id": responseQuotation.id_quotation,
    "time_event": hourDate,
  }
  console.log(dataCreateDate)
  const responseCreateDate = await fetch(urlCreateDate, {
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
    },
    "body": JSON.stringify(dataCreateDate)
  })
    .then((response) => response.json())
    .catch((razon) => {
      console.log("enviar datos 'dataCreateDate' fallo, razon:", razon);
    });
  renderCreateDate(responseCreateDate)
}

function renderCreateDate(obj) {
  const availability = document.getElementById("availability");
  const responseCreateDate = `
  <p id="emailHelp">
  <h1 class="fw-bold text-center first-text">${obj.message}!</h1><br>
  Remember that in your email and your calendar you will find all the information of the appointment.
  </p>
  `
  availability.innerHTML = responseCreateDate;
}

getDataArtist();
makeQuote.onclick = sendDataQuotation;
