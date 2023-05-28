function playPause() {
    var mediaPlayer = document.getElementById("fish_noises");
    if (mediaPlayer.paused) {
        mediaPlayer.play(); 
        $('#pause-btn').show();
        $('#play-btn').hide();
        console.log("played")
    } else {
        mediaPlayer.pause(); 
        $('#play-btn').show();
        $('#pause-btn').hide();
        console.log("paused")
    }
}