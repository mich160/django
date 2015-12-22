/**
 * Created by Targon on 20.12.2015.
 */
$(document).ready(function () {

    setupAjax();

    $(".changePassword").click(function () {
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
                }.done( function () {
                    $(".infoPass").text("Zmiana hasła zapisana");
                    $(".infoPass").attr("class", "alert alert-success infoDiv infoPass topMargin10");
                }).fail(function (){
                    $(".infoPass").text("Błędne hasło");
                    $(".infoPass").attr("class", "alert alert-warning infoDiv infoPass topMargin10");
            })
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
            }.done(function () {
                    $(".infoMail").text("Zmiana maila zapisana");
                    $(".infoMail").attr("class", "alert alert-success infoDiv infoMail topMargin10");
                }).fail(function(){
                    $(".infoMail").text("Błędne hasło");
                    $(".infoMail").attr("class", "alert alert-warning infoDiv infoMail topMargin10");
            })
            );
        } else {
            $(".infoMail").text(validMsg);
            $(".infoMail").attr("class", "alert alert-warning infoDiv infoMail topMargin10");
        }
    });

});