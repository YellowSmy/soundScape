document.addEventListener("DOMContentLoaded", () => {
   const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

   //Update Req
   if (document.getElementById("player").getAttribute("video-id")) {
      document.getElementById("music-player").style.display = "block";
   }

   //search
   document.getElementById('search-btn').addEventListener("click", () => {
       const query = document.getElementById("search-input").value;

       if (query.trim() == "") {
          alert("입력하세요.");
          return;
       }

       //AJAX
       fetch(`/search?query=${encodeURIComponent(query)}`, {
          method: 'GET',
          headers: {
             'X-CSRFToken': csrfToken,
          },
       })
          .then(response => response.json())
          .then(data => {
            const resultDiv = document.getElementById("youtube-result");
            if (data.error) {
               resultDiv.innerHTML = '<p> ${data.error} </p>'
            }
            else {
               resultDiv.innerHTML = `<img src="${data.thumbnail}"></img> 
                                      <button type="button" id="select-btn" 
                                              onclick = "selectVideo('${data.videoId}', '${data.thumbnail}');">Select</button>`;
            }
         })
          .catch(error => {
             console.error(error);
         });
   });


});


 function selectVideo(videoId, thumbnailURL) {
   document.getElementById("id_video_id").value = videoId;
   document.getElementById("id_thumbnail_url").value = thumbnailURL;
   alert('Select Complete.');
   loadVideo(videoId);
}

//extends from js/music/musicPlayer.js
function loadVideo(videoId) {
   const videoDiv = document.getElementById("music-player");
   const resultDiv = document.getElementById("youtube-result");
   document.getElementById('player').setAttribute("video-id", videoId);

   if (typeof player === 'undefined' || !player.loadVideoById) {
      initializePlayer(videoId);
   }
   else {
      player.loadVideoById(videoId);
   }

   resultDiv.style.display = "none";
   videoDiv.style.display = "block";

}