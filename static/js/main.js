$(document).ready(function () {
  let weatherBtn = "Sunny";
  let title = $("#song-title").text();
  likeBtnSong(title, weatherBtn);
  console.log(title);
  console.log($("#Sunny-btn").attr("value"));
});

$(function () {
  $("#Sunny-btn").click(function () {
    let title = $("#song-title").text();
    let weatherBtn = "Sunny";
    likeBtnSong(title, weatherBtn);
    console.log($("#song-title").text());
  });
});

$(function () {
  $("#Cloudy-btn").click(function () {
    let title = $("#song-title").text();
    let weatherBtn = "Cloudy";
    likeBtnSong(title, weatherBtn);
  });
});

$(function () {
  $("#Rainy-btn").click(function () {
    let title = $("#song-title").text();
    let weatherBtn = "Rainy";
    likeBtnSong(title, weatherBtn);
  });
});

$(function () {
  $("#Snowy-btn").click(function () {
    let title = $("#song-title").text();
    let weatherBtn = "Snowy";
    likeBtnSong(title, weatherBtn);
  });
});

function likeBtnSong(title, weatherBtn) {
  $.ajax({
    type: "POST",
    url: "/api/likeBtn",
    data: { title_give: title, weatherBtn_give: weatherBtn },
    success: function (response) {
      alert(response["msg"]);
    },
  });
}

console.log($("#song-title").text());
