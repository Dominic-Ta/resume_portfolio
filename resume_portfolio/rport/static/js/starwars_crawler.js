// Get the board element
let boardElement = document.getElementById('board');

// Calculate the delay before applying the no-inherit class
let delay = (boardElement.style.animationDuration || 100) - 5000;

// Listen for animation end event
boardElement.addEventListener('animationend', function() {
  // Delay the application of the no-inherit class
  setTimeout(function() {
    // Add the no-inherit class to the scroll-in element
    let scrollingText = document.getElementById('scrolling-text');
    scrollingText.classList.add('no-inherit');
  }, delay);
});

function loadCharts() {
  // Load the TIMESERIES chart
  let timeseriesContainer = document.getElementById("timeseriesContainer");
  let timeseriesIframe = document.createElement("iframe");
  timeseriesIframe.src =
    "https://trends.google.com:443/trends/embed/explore/TIMESERIES?req=%7B%22comparisonItem%22%3A%5B%7B%22keyword%22%3A%22%2Fm%2F0dtfn%22%2C%22geo%22%3A%22%22%2C%22time%22%3A%222004-01-01%202023-06-15%22%7D%5D%2C%22category%22%3A0%2C%22property%22%3A%22%22%7D&tz=240&eq=date%3Dall%26q%3D%252Fm%252F0dtfn%26hl%3Den-US";
  timeseriesIframe.title = "trends-widget-timeseries";
  timeseriesIframe.loading = "lazy";
  timeseriesIframe.setAttribute("allowfullscreen", "");
  timeseriesIframe.setAttribute("sandbox", "allow-scripts allow-same-origin");
  timeseriesIframe.style.cssText = "width: 100%; height: 100%; border: none;";
  timeseriesContainer.innerHTML = ""; // Clear the container's content
  timeseriesContainer.appendChild(timeseriesIframe);

  // Load the GEO_MAP chart
  let geomapContainer = document.getElementById("geomapContainer");
  let geomapIframe = document.createElement("iframe");
  geomapIframe.src =
    "https://trends.google.com:443/trends/embed/explore/GEO_MAP?req=%7B%22comparisonItem%22%3A%5B%7B%22keyword%22%3A%22%2Fm%2F0dtfn%22%2C%22geo%22%3A%22%22%2C%22time%22%3A%222004-01-01%202023-06-15%22%7D%5D%2C%22category%22%3A0%2C%22property%22%3A%22%22%7D&tz=240&eq=date%3Dall%26q%3D%252Fm%252F0dtfn%26hl%3Den-US";
  geomapIframe.title = "trends-widget-geomap";
  geomapIframe.loading = "lazy";
  geomapIframe.setAttribute("allowfullscreen", "");
  geomapIframe.setAttribute("sandbox", "allow-scripts allow-same-origin");
  geomapIframe.style.cssText = "width: 100%; height: 100%; border: none;";
  geomapContainer.innerHTML = ""; // Clear the container's content
  geomapContainer.appendChild(geomapIframe);
}

// Call the loadCharts function to load the charts before updating the content
loadCharts();


setTimeout(function () {
  // Replace the existing div with the hidden div
  let existingDiv = document.getElementById("main_container");
  
  let hiddenDiv = document.getElementById("hiddenDiv");
// Create a style element
  let styleElement = document.createElement("style");

  // Set the CSS animation and keyframes
  existingDiv.style.cssText = '';
  styleElement.innerHTML = `
    #main_container p {
      position: relative;
      z-index: 5; /* Adjust the value as needed */
    }
    #main_container {
      position: relative; /* Change position to relative */
      font-family: Century Gothic, CenturyGothic, AppleGothic, sans-serif;
      bottom: 0;
      animation: scroll 7s linear;
      animation-delay: 0s;
    }

    @keyframes scroll {
      0% {
        transform: translateY(100%);
      }
      50% {
        transform: translateY(50%);
      }
      100% {
        transform: translateY(0%);
      }
    }
    .iframe-container {
      overflow: auto;
    }
  `;

  // Append the style element to the document head
  document.head.appendChild(styleElement);
  // Copy the content of hiddenDiv to existingDiv
  existingDiv.innerHTML = hiddenDiv.innerHTML;
  let selectElements = document.querySelectorAll('select');
  // console.log(selectElements)
  selectElements.forEach(function(selectElement) {
    selectElement.addEventListener('change', function() {
      let selectedOption = selectElement.options[selectElement.selectedIndex];
      // let selectedValue = selectedOption.value;
      let selectedId = selectedOption.id;
      // alert(`Selected Value: ${selectedValue}\nSelected ID: ${selectedId}`);
      // let doc_id = document.getElementById('meow');
      getChar(selectedId);
      // console.log(x);
    });
  });
}, 1);
// 65000
function get_url(input_url, search_crit){
  // General function mainly used for testing. No need to input specific domain names now. 
  let protocol = window.location.protocol;
  let hostname = window.location.hostname;
  let port = window.location.port ? ":" + window.location.port : ""; // Include the port if it exists
  let domain = protocol + "//" + hostname + port;
  return domain + input_url + search_crit;
}
function image_promise(data, ElId, typeVar, field, output) {
  let y = data;
  let meow_element = document.getElementById(ElId);
  let imagePromise = get_image(typeVar, field);

  imagePromise
    .then(image_output => {
      let x = image_output;

      let cardElement = meow_element.querySelector('.card');
      if (!cardElement) {
        cardElement = document.createElement('div');
        cardElement.setAttribute("id", "picture_this");
        cardElement.classList.add('card');
        // cardElement.style.width = '18rem';
        meow_element.appendChild(cardElement);
      }

      let imgElement = cardElement.querySelector('img');
      if (!imgElement) {
        imgElement = document.createElement('img');
        imgElement.classList.add('card-img-top');
        imgElement.classList.add('img-fluid');
        cardElement.appendChild(imgElement);
      }
      imgElement.src = x;
      imgElement.alt = y.character;

      let cardBody = cardElement.querySelector('.card-body');
      if (!cardBody) {
        cardBody = document.createElement('div');
        cardBody.classList.add('card-body');
        cardBody.classList.add('overflow-auto');
        cardBody.classList.add('text-center');
        cardElement.appendChild(cardBody);
      }

      let cardText = cardBody.querySelector('p');
      if (!cardText) {
        cardText = document.createElement('p');
        cardText.classList.add('card-text');
        cardText.classList.add('text-dark');
        cardBody.appendChild(cardText);
      }
      cardText.innerHTML = output;
      // Reset the animation by removing and re-adding the element with the animation class
      let clonedCardElement = cardElement.cloneNode(true);
      cardElement.parentNode.replaceChild(clonedCardElement, cardElement);

      // Add a slight delay before applying the animation class to allow time for the element to be rendered
      setTimeout(() => {
        clonedCardElement.classList.add('slideInLeft');
      }, 10);
    })
    .catch(error => {
      console.error(error);
    });
}

function get_planet(planet){
  let url = get_url('/examples/get-planet_json/', planet)
  fetch(url, {method: 'GET'})
  .then(response => {
    if (response.ok) {
      return response.json(); // or response.text() for plain text response
    } else {
      throw new Error('Error: ' + response.status);
    }})
    .then(data => {
      let y = data;
      let fields = y.fields; 
      let output = table_creation(data, 0);
      let pattern = /\d+/;
      let match = fields.url.match(pattern);
      let planetImgUrlnum=parseInt(match[0], 10)
      image_promise(data,'planet_card', 'planets', planetImgUrlnum, output)
      });
}
function table_creation(data, range){
  let y = data;
  let fields = y.fields; // Get the fields object
  let keys = Object.keys(fields);
  let output = "<table class='table table-striped table-dark table-hover'>"; // Start the table
  
  // Iterate over the fields and generate table rows
  for (let i = 0; i < keys.length - range; i++) {
    let key = keys[i];
    output += `<tr><td>${key}</td><td>${fields[key]}</td></tr>`;
  }
  
  output += "</table>";
  return output
}
function getChar(char){
  window.stop() // incase any fetch requests are waiting.
  let url = get_url('/examples/get-char/', char);


  fetch(url, {
    method: 'GET'
  })
    .then(response => {
      if (response.ok) {
        return response.json(); // or response.text() for plain text response
      } else {
        throw new Error('Error: ' + response.status);
      }
    })
    .then(data => {
      let y = data; // Store the response data in the 'y' variable
      let fields = y.fields; // Get the fields object
      let keys = Object.keys(fields);
      let output = table_creation(y, 1)
      // doc_id.innerHTML = output;
      image_promise(y, "character", "char", fields.char_num, output)
      get_planet(fields.homeworld);
    })
    .catch(error => {
      console.error(error);
    });
}
function get_image(tval, id_num) {
  let url = get_url("/examples/assets/", tval + "/" + id_num)
  return fetch(url, {
    method: 'GET'
  })
    .then(response => {
      if (response.ok) {
        return response.url
      } else {
        throw new Error('Error: ' + response.status);
      }
    });
}
