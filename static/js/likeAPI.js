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
    let weatherBtn = "Sunny";
    console.log($("#Sunny-btn").css("font-size"));
    if ($("#Sunny-btn").css("font-size") == "16px") {
      is_weatherLike = false;
    } else {
      is_weatherLike = true;
    }
    console.log(is_weatherLike);
    likeBtnSong(weatherBtn, is_weatherLike);
    setTimeout(showLike, 100);
  });
});

$(function () {
  $("#Cloudy-btn").click(function () {
    let weatherBtn = "Cloudy";

    if ($("#Cloudy-btn").css("background-color") == "blue") {
      is_weatherLike = true;
    } else {
      is_weatherLike = false;
    }

    likeBtnSong(weatherBtn, is_weatherLike);
    setTimeout(showLike, 100);
  });
});

$(function () {
  $("#Rainy-btn").click(function () {
    let weatherBtn = "Rainy";

    if ($("#Rainy-btn").css("background-color") == "blue") {
      is_weatherLike = true;
    } else {
      is_weatherLike = false;
    }

    likeBtnSong(weatherBtn, is_weatherLike);
    setTimeout(showLike, 100);
  });
});

$(function () {
  $("#Snowy-btn").click(function () {
    let weatherBtn = "Snowy";

    if ($("#Snowy-btn").css("background-color") == "blue") {
      is_weatherLike = true;
    } else {
      is_weatherLike = false;
    }

    likeBtnSong(weatherBtn, is_weatherLike);
    setTimeout(showLike, 100);
  });
});

function likeBtnSong(weatherBtn, is_weatherLike) {
  let title = $("#song-title").text();
  let artist = $(".music-box-artist").text();
  let username = $(".username").text();

  $.ajax({
    type: "POST",
    url: "/api/like-btn",
    data: {
      title_give: title,
      artist_give: artist,
      weatherBtn_give: weatherBtn,
      username_give: username,
      is_weatherLike_give: is_weatherLike,
    },
    success: function (response) {
      console.log(response);
      if (response["msg"] == "로그인을 해주세요!") {
        alert(response["msg"]);
        let redirect_url = response["redirect_url"];
        window.location.replace(redirect_url);
      }
    },
  });
}

/* 좋아요 API (GET) 클라이언트 */

function showLike() {
  let title = $("#song-title").text();
  let artist = $(".music-box-artist").text();
  let username = $(".username").text();

  $.ajax({
    type: "GET",
    url: "/api/show-like",
    data: { title_give: title, artist_give: artist, username_give: username },
    success: function (response) {
      console.log(response);
      // 서버 DB로부터 받은 그 곡의 데이터(곡 정보, 날씨 좋아요 수)
      let song = response["target_song"];

      let btn_like = response["target_btn_like"];
      console.log(song);
      console.log(btn_like);

      // 각 날씨별 사용자가 버튼 눌렀는지(true) / 안 눌렀는지 (false)
      let is_SunnyLike = btn_like["Sunny"];
      let is_CloudyLike = btn_like["Cloudy"];
      let is_RainyLike = btn_like["Rainy"];
      let is_SnowyLike = btn_like["Snowy"];

      // 곡 제목 -> 필요 X
      // let title = song[0]["title"]

      // 각 날씨별 반영된 좋아요 수
      let SunnyLike = song["Sunny"];
      let CloudyLike = song["Cloudy"];
      let RainyLike = song["Rainy"];
      let SnowyLike = song["Snowy"];

      // 현재 좋아요를 누른 상태인지, 아닌지 확인 (True : 좋아요를 누른 상태 / False : 좋아요를 취소한 상태)
      // let is_Like =

      // 날씨별 버튼의 좋아요 수를 나타내는 태그를 jQuery로 잡아서 text를 바꾸면 될 듯?
      // ex) 날씨별 버튼의 좋아요 수를 나타내는 태그의 id = 날씨likeCount라고 하면,
      $(".Sunny-btn__like").text(SunnyLike);
      $(".Cloudy-btn__like").text(CloudyLike);
      $(".Rainy-btn__like").text(RainyLike);
      $(".Snowy-btn__like").text(SnowyLike);

      // 날씨별 사용자가 버튼 눌렀는지, 안 눌렀는지에 따라 html,css 다르게
      if (is_SunnyLike == true) {
        // 맑음 버튼 사용자가 누른 상태일 때 디자인
        $("#Sunny-btn").css({ "font-size": "40px" });
      } else {
        // 맑음 버튼 사용자가 안 누른? 상태일 때 디자인 (원래 디자인)
        $("#Sunny-btn").css({ "font-size": "16px" });
      }
      // 이렇게 4개 버튼 디자인

      // 예시 : 사용자가 누른 상태일 때 background : blue / 원래 디자인 : orange
      if (is_CloudyLike == true) {
        $("#Cloudy-btn").css({ "background-color": "blue" });
      } else {
        $("#Cloudy-btn").css({ "background-color": "orange" });
      }

      if (is_RainyLike == true) {
        $("#Rainy-btn").css({ "background-color": "blue" });
      } else {
        $("#Rainy-btn").css({ "background-color": "orange" });
      }

      if (is_SnowyLike == true) {
        $("#Snowy-btn").css({ "background-color": "blue" });
      } else {
        $("#Snowy-btn").css({ "background-color": "orange" });
      }
    },
  });
}
