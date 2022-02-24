document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".sidenav");
  var instances = M.Sidenav.init(elems);
});

$(document).ready(function () {
  $("#example").DataTable();
  // $("input#Vehicle_Name").characterCounter();

   function getCookie(name) {
     let cookieValue = null;
     if (document.cookie && document.cookie !== "") {
       const cookies = document.cookie.split(";");
       for (let i = 0; i < cookies.length; i++) {
         const cookie = cookies[i].trim();
         // Does this cookie string begin with the name we want?
         if (cookie.substring(0, name.length + 1) === name + "=") {
           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
           break;
         }
       }
     }
     return cookieValue;
   }
   const csrftoken = getCookie("csrftoken");


  $(".onoff_btn").on('click',function(){
    $(this).siblings().removeClass('active');
    $(this).addClass('active');

    value=$(this).attr("data-value");
    id=$(this).attr("data-id");

    onoff_data = {'value':value,'id':id}

    $.ajax({
      data: onoff_data,
      headers: { "X-CSRFToken": csrftoken },
      type: "POST",
      url: "/update/",
      success: function (response) {
        // if (response.status == "Success") {
        //   alert("Status changed");
        // } else {
        //   alert("can't chaange status");
        // }
      },
    });



     

  })



});

    
    
