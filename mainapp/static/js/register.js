/**
 * Created by Cezary on 20.12.2015.
 */

$(document).ready(function() {
    $('.cancelRegistration').click(function() {
        $('.regForm input[type="text"]').val('');
        $('.regForm input[type="password"]').val('');
        $('.regForm input').tooltip('destroy');
    })
});
