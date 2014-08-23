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

    init();

})