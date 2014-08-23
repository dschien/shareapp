/**
 * Created by schien on 23/08/2014.
 */



function init() {
    var template = _.template(
        $("script.listitem_template").html()
    );

    $.ajax({url: "/apibrowse/items" }).done(function (data) {
        console.log(data)
        var div = $('<div></div>');

        _.each(data, function (it) {
            div.append(template(it))
        });

        $("#first_list").append(div)
    })
}

$(document).ready(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }})


    $("#button").click(function () {
        t = setTimeout("removeDisplayMessage()", 2000);
    });

    $("#submit_item").bind('tap', function (event) {
        event.preventDefault();
        //showNotification({
        //	message: "This is a sample Success notification",
        //	type: "success"
        //});


        $("#add_form").empty();
        $('#add_form').append('<p><b>Item added!</b> <img src="../static/res/icons/agt_action_success.png" alt="Smiley face" height="42" width="42"></p>  ');
        t = setTimeout("removeDisplayMessage()", 1000);
    });


    init();

});

function removeDisplayMessage() {
    $("#add_form").hide();
}




