/**
 * Created by Targon on 20.12.2015.
 */
$( document ).ready(function() {
						function getCookie(cname) {
   						var name = cname + "=";
    					var ca = document.cookie.split(';');
    					for(var i=0; i<ca.length; i++) {
        					var c = ca[i];
        					while (c.charAt(0)==' ') c = c.substring(1);
        					if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    					}
    				return "";
					}
					var csrftoken=getCookie("csrftoken");
					function csrfSafeMethod(method) {
						return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
					}
					$.ajaxSetup({
						beforeSend: function(xhr,settings) {
							if(!csrfSafeMethod(settings.type)&&!this.crossDomain) {
								xhr.setRequestHeader("X-CSRFToken",csrftoken);
							}
						}
					});
					$(".changePassword").click(function(){
						concole.log("trololo");
						var oldPassword=document.getElementById("passwordOld");
						var newPassword=document.getElementById("passwordReg");
						var newPassword2=document.getElementById("passwordRegRep");

					});
					$(".changeMail").click(function(){
						concole.log("chyba dziala");
						var newMail=document.getElementById("emailReg");
						var newMail2=document.getElementById("emailRegRep");
						var password=document.getElementById("password");
						
					});

});