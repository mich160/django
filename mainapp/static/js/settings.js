/**
 * Created by Targon on 20.12.2015.
 */
$(document).ready(function () {
    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') c = c.substring(1);
            if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
        }
        return "";
    }

    var csrftoken = getCookie("csrftoken");

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $(".changePassword").click(function () {
        console.log("trololo");
        var oldPassword = document.getElementById("passwordOld").value;
        var newPassword = document.getElementById("passwordReg").value;
        var newPassword2 = document.getElementById("passwordRegRep").value;
        var validMsg = validatePassword(newPassword);
        validMsg += validatePswdRep(newPassword, newPassword2);
        console.log(validMsg)
        if (validMsg == "") {
            $.post("changePassword", {
                    oldPswd: oldPassword,
                    newPswd: newPassword
                }, function () {
                    $(".infoPass").text("Zmiana hasła zapisana");
                    $(".infoPass").attr("class", "alert alert-success infoDiv infoPass topMargin10");
                }
            );
        } else {
            $(".infoPass").text(validMsg);
            $(".infoPass").attr("class", "alert alert-warning infoDiv infoPass topMargin10");
        }
    });
    $(".changeMail").click(function () {
        console.log("chyba dziala");
        var newMail = document.getElementById("emailReg").value;
        var newMail2 = document.getElementById("emailRegRep").value;
        var password = document.getElementById("password").value;
        var validMsg = validateEmail(newMail);
        validMsg += validateEmailRep(newMail, newMail2);
        if (validMsg == "") {
            $.post("changeMail", {
                    pswd: password,
                    mail: newMail
                }, function () {
                    $(".infoMail").text("Zmiana maila zapisana");
                    $(".infoMail").attr("class", "alert alert-success infoDiv infoMail topMargin10");
                }
            );
        } else {
            $(".infoMail").text(validMsg);
            $(".infoMail").attr("class", "alert alert-warning infoDiv infoMail topMargin10");
        }
    });

});