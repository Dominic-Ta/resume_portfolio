let playButton = document.getElementById('play_btn');
let volumeButton = document.getElementById('muteButton');
playButton.addEventListener('click', function() {
  console.log(playButton.classList);
  if (playButton.classList.contains('bi-play')) {
    playButton.classList.remove('bi-play');
    playButton.classList.add('bi-pause');
  } else {
    playButton.classList.remove('bi-pause');
    playButton.classList.add('bi-play');
  }
});
volumeButton.addEventListener('click', function() {
  if (volumeButton.classList.contains('bi-volume-up')) {
    volumeButton.classList.remove('bi-volume-up');
    volumeButton.classList.add('bi-volume-mute');
  } else {
    volumeButton.classList.remove('bi-volume-mute');
    volumeButton.classList.add('bi-volume-up');
  }
});
// window.addEventListener('resize', function() {
//     var button = document.getElementById('myButton');
//     var buttonFontSize = parseFloat(window.getComputedStyle(button).getPropertyValue('font-size'));
//     var zoomRatio = buttonFontSize / 16; // Adjust the initial font size used for calculation
  
//     // Update the font size of all related elements
//     var elements = document.getElementsByClassName('btn_mute');
//     for (var i = 0; i < elements.length; i++) {
//       var element = elements[i];
//       element.style.fontSize = zoomRatio * 16 + 'px'; // Adjust the base font size as needed
//     }
//   });
