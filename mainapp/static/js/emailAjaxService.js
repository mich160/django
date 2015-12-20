/**
 * Created by Cezary on 20.12.2015.
 */
$(document).ready(function () {

    setupAjax();

    $(".sendMail").click(function () {
        var to = $(".parentSelect").val();
        var subj = $(".mailSubject").val();
        var msg = $(".mailBody").val();

        if (to != '' && subj != '' && msg != '') {
            $.post("sendMailServ", {
                toWho: to,
                mailSubject: subj,
                mailBody: msg
            }, function () {
                $(".infoDiv").text("Wiadomość wysłana");
                $(".infoDiv").attr("class", "alert alert-success infoDiv topMargin10");
            })

        } else {
            $(".infoDiv").text("Źle wypełniony formularz");
            $(".infoDiv").attr("class", "alert alert-warning infoDiv topMargin10");
        }

    });

});