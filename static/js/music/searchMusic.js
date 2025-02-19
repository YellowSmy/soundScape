document.addEventListener("DOMContentLoaded", () => {
   const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

   //Update Req
   if (document.getElementById("player").getAttribute("video-id")) {
      document.getElementById("music-player").style.display = "block";
   }

   //search
   document.getElementById('search-btn').addEventListener("click", (event) => {
       const query = document.getElementById("search-input").value;

       if (query.trim() == "") {
          alert("필수 입력 사항입니다."); 
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
            //reset
            resultDiv.style.display = "flex"; 
            resultDiv.innerHTML = "";

            if (data.error) {
               resultDiv.innerHTML = `<p>${data.error}</p>`
            }

            else {
               data.results.forEach(video => {
                  const musicDiv = document.createElement("div");
                  musicDiv.className = "music-div";
                  musicDiv.innerHTML = `<img class="thumbnail" src="${video.thumbnail}" alt="${video.title}"></img> 
                                        <p class="title">${video.title}</p>
                                        <button type="button" class="select-btn" style="display:none" 
                                                onclick="selectVideo('${video.videoId}','${video.thumbnail}'); selectMusicInfo('${data.info.music_title}','${data.info.artist}')">
                                        Select</button>`
                  musicDiv.addEventListener("click", showBtn);

                  resultDiv.appendChild(musicDiv);
               });
            }
         })
          .catch(error => {
             console.error(error);
         });
   });
});

// hidden input 
 function selectVideo(videoId, thumbnailURL) {
   // video info. 
   document.getElementById("id_video_id").value = videoId;
   document.getElementById("id_thumbnail_url").value = thumbnailURL;
   
   loadVideo(videoId);
}

function selectMusicInfo(musicTitle, artist) {
   document.getElementById("id_music_title").value = musicTitle;
   document.getElementById("id_artist").value = artist;
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
      player.cueVideoById(videoId);
   }

   resultDiv.style.display = "none";
   videoDiv.style.display = "block";

}


//show select Btn
function showBtn(event) {
   const item = event.currentTarget;
   const items = document.querySelectorAll('.music-div');
   const button = item.querySelector('.select-btn');

   items.forEach(otherItem => {
      if(otherItem != item) {
         otherItem.querySelector('.select-btn').style.display = 'none';
      }
   });

   if (button.style.display === 'none' || button.style.display === '') {
      button.style.display = 'block';
   }
   else {
      button.style.display = 'none';
   }
}


//temp-save validation
document.addEventListener("DOMContentLoaded", () => {
   document.getElementById('content-form').addEventListener('submit', function (event) {
      const searchInput = document.getElementById('search-input');
      if (!searchInput.value.trim()) {
         event.preventDefault(); // 폼 제출 방지
         alert('검색 입력은 필수입니다!');
      }
   });
});
