//Iframe Player Asynchronized load.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);


var player;
function initializePlayer(videoId) {
    player = new YT.Player('player', {
        height: '360',  //변경가능-영상 높이
        width: '640',  //변경가능-영상 너비
        videoId: videoId,  //변경-영상ID


        playerVars: {
            'rel': 0,    //연관동영상 표시여부(0:표시안함)
            'controls': 1,    //플레이어 컨트롤러 표시여부(0:표시안함)
            'autoplay': 0,   //자동재생 여부(1:자동재생 함, mute와 함께 설정)
            'mute': 0,   //음소거여부(1:음소거 함)
            'loop': 1,    //반복재생여부(1:반복재생 함)
            'playsinline': 1,   //iOS환경에서 전체화면으로 재생하지 않게
        },
        events: {
            'onReady': onPlayerReady, //onReady 상태일 때 작동하는 function이름
            'onStateChange': onPlayerStateChange,
        }
    });
}

function onYouTubeIframeAPIReady() {
    youtube_video_id = document.getElementById('player').getAttribute("video-id");

    if (youtube_video_id) {
        initializePlayer(youtube_video_id);
    }
}

function onPlayerReady(event) {
    musicControl()
}

function onPlayerStateChange(event) {
    musicControl()
}

function loadNewVideo(videoId){
    player.destroy();
    playerParams.videoId = vidID;
    player = new YT.Player('player', playerParams);

}


//music control tool
function musicControl() {
    //Play & Pause
    var playBtn = document.getElementById("playBtn");
    playBtn.addEventListener("click", () => { 
        var playerState =player.getPlayerState()
        if(playerState == 1) {
            player.pauseVideo()
            playBtn.innerText = ">>";
        } 
        else {
            player.playVideo();
            playBtn.innerText = "||";
        }
    });

    //Audio
    // volume
    var slider = document.getElementById("volume");
    slider.value = 50;
    slider.addEventListener('mousemove', () => { player.setVolume(slider.value); })

    // mute
    var mute = document.getElementById("mute");
    mute.addEventListener("click", () => {
        if (player.isMuted()) {
            player.unMute();
            mute.innerText = "음소거";
        }
        else {
            player.mute();
            mute.innerText = "켜기";
        }
    });


    //Play Bar
    var seeker = document.getElementById("seeker");
    var playerclick = false;

    var checkDuration = setInterval(() => {
        if (player.getDuration) {
            seeker.max = player.getDuration();
            clearInterval(checkDuration);
        }
    }, 250);

    seeker.value = 0;

    seeker.addEventListener('mousemove', () => {
        if (playerclick) {
            player.seekTo(seeker.value, false);
        }
    });

    seeker.addEventListener('mousedown', () => { playerclick = true; });
    seeker.addEventListener('mouseup', () => {
        playerclick = false;
        player.seekTo(seeker.value, true)
    });

    setInterval(updatePlayer, 250);

    function updatePlayer() {
        if (player && player.getDuration) {
            if (!playerclick) {
                seeker.value = player.getCurrentTime();
            }
        }
    }
}

