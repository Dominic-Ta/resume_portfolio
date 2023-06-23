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
// Function to be executed after 1 minute
// Wait for 1 minute (60000 milliseconds)
// setTimeout(function() {
//   // Show the hidden div
//   let hiddenDiv = document.getElementById("hiddenDiv");
//   hiddenDiv.style.display = "block";

//   // Apply custom CSS animation
//   hiddenDiv.style.animation = "fadeIn 3s";

//   // Define a CSS animation keyframe
//   let styleSheet = document.createElement("style");
//   styleSheet.innerHTML = `

//     @keyframes fadeIn {
//       from { opacity: 0; }
//       to { opacity: 1; }
//     }
//   `;
//   document.head.appendChild(styleSheet);
// }, 1000);

// // Run the function after 1 minute (60,000 milliseconds)
// setTimeout(myFunction, 60000);
// Wait for 1 minute (60000 milliseconds)
// Wait for 1 minute (60000 milliseconds)

// setTimeout(function() {
//   // Replace the existing div with the hidden div
//   let existingDiv = document.getElementById("main_container");
//   let hiddenDiv = document.getElementById("hiddenDiv");

//   // Copy the content of hiddenDiv to existingDiv
//   existingDiv.innerHTML = hiddenDiv.innerHTML;

//   // Remove the display none property
//   existingDiv.style.display = "";

//   // Define a CSS animation keyframe
//   let styleSheet = document.createElement("style");
//   styleSheet.innerHTML = `
//   #main_container {
//     z-index: 5;
//     font-family: Century Gothic, CenturyGothic, AppleGothic, sans-serif;
//     bottom: 0;
//     animation: scroll 5s linear ;
//     animation-delay: 0s;
//   }

//   @keyframes scroll {
//     0% {
//       transform: translateY(100%);
//     }
//     75% {
//       transform: translateY(75%);
//     }
//     100% {
//       transform: translateY(75%);
//     }
//   }

// `;
// console.log(existingDiv);
//   document.head.appendChild(styleSheet);
//   existingDiv.style.display = "";
// }, 1);
// // 65000
// Create a function to load the charts
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
}, 1);
// 65000