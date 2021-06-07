// Получение переменной cookie по имени
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Настройка AJAX
$(function () {
  $.ajaxSetup({
    headers: { "X-CSRFToken": getCookie("csrftoken") }
  });
});



function like() {

  var article = $(this).parent().parent().parent().attr('id');
  $("#debug_msg").html('Msg: like pressed on ' + article);
  var likesCounter = $(this).parent().parent().children().first()  
  $.ajax({
    url: '/like/' + article,
    success: function (json) {
      likesCounter.html(json.likes);
    }
  });
}

$(function () {
  $('.like').click(like);
});
