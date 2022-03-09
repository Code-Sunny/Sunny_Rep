/* 종아요 API 함수 실행 순서 : POST -> GET이어야 한다 */
/* POST로 DB에 좋아요 수 +1로 업데이트 후 GET으로 화면에 보여주기*/

/* 좋아요 API (POST) 클라이언트 */

// 각 버튼이 클릭되었을 때
// 팝업창의 노래 제목 태그의 text 불러오기 = 곡 제목
// 버튼 id에 적힌 날씨 = 그 날씨 버튼을 클릭함
// 두 개의 정보를 매개변수로 likeBtnSong 함수를 호출하여
// ajax를 사용해서 서버측으로 전송
$(function () {
  $("#Sunny-btn").click(function () {
    let title = $("#song-title").text();
    let artist = $(".music-box-artist").text();
    let weatherBtn = "Sunny";
    likeBtnSong(title, artist, weatherBtn);
    showLike(title, artist);
    console.log(artist);
  });
});

$(function () {
  $("#Cloudy-btn").click(function () {
    let title = $("#song-title").text();
    let artist = $(".music-box-artist").text();
    let weatherBtn = "Cloudy";
    likeBtnSong(title, artist, weatherBtn);
    showLike(title, artist);
  });
});

$(function () {
  $("#Rainy-btn").click(function () {
    let title = $("#song-title").text();
    let artist = $(".music-box-artist").text();
    let weatherBtn = "Rainy";
    likeBtnSong(title, artist, weatherBtn);
    showLike(title, artist);
  });
});

$(function () {
  $("#Snowy-btn").click(function () {
    let title = $("#song-title").text();
    let artist = $(".music-box-artist").text();
    let weatherBtn = "Snowy";
    likeBtnSong(title, artist, weatherBtn);
    showLike(title, artist);
  });
});

function likeBtnSong(title, artist, weatherBtn) {
  $.ajax({
    type: "POST",
    url: "/api/likeBtn",
    data: {
      title_give: title,
      artist_give: artist,
      weatherBtn_give: weatherBtn,
    },
    success: function (response) {
      alert(response["msg"]);
    },
  });
}

/* 좋아요 API (GET) 클라이언트 */

function showLike(title, artist) {
  $.ajax({
    type: "GET",
    url: "/api/showLike",
    data: { title_give: title, artist_give: artist },
    success: function (response) {
      // 서버 DB로부터 받은 그 곡의 데이터(곡 정보, 날씨 좋아요 수)
      let song = response["target_song"];
      console.log(song);

      // 곡 제목 -> 필요 X
      // let title = song[0]["title"]

      // 각 날씨별 반영된 좋아요 수
      let sunnyLike = song["Sunny"];
      let cloudyLike = song["Cloudy"];
      let rainyLike = song["Rainy"];
      let snowyLike = song["Snowy"];

      // 날씨별 버튼의 좋아요 수를 나타내는 태그를 jQuery로 잡아서 text를 바꾸면 될 듯?
      // ex) 날씨별 버튼의 좋아요 수를 나타내는 태그의 id = 날씨likeCount라고 하면,
      $(".Sunny-btn__like").text(sunnyLike);
      $(".Cloudy-btn__like").text(cloudyLike);
      $(".Rainy-btn__like").text(rainyLike);
      $(".Snowy-btn__like").text(snowyLike);
    },
  });
}