async function get_data_character(url, _type, charName){
    let full_url = url+charaName;
    let response = await fetch(full_url).json();
    console.log(response);
}
// function getChar(char){
//     window.stop() // incase any fetch requests are waiting.
//     let character = char;
//     let domain = window.location.hostname;
//     let url = domain + "/examples/get-char/" + character;
//     // url = "http://127.0.0.1:8000/examples/get-char/Luke%20Skywalker";

//     fetch(url, {
//       method: 'GET',
//     })
//       .then(response => {
//         if (response.ok) {
//           return response.json(); // or response.text() for plain text response
//         } else {
//           throw new Error('Error: ' + response.status);
//         }
//       })
//       .then(data => {
//         y = data; // Store the response data in the 'y' variable
//         console.log(y);
//       })
//       .catch(error => {
//         console.error('Error:', error);
//       });
// }
