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
						console.log("trololo");
						var oldPassword=document.getElementById("passwordOld").value;
						var newPassword=document.getElementById("passwordReg").value;
						var newPassword2=document.getElementById("passwordRegRep").value;
						console.log(newPassword);
						if (oldPassword=="test"){
							if(newPassword!="" && newPassword2!="") {
								if (newPassword == newPassword2) {
									$(".infoPass").text("Hasło zmienione");
									$(".infoPass").attr("class", "alert alert-success infoDiv infoPass topMargin10");
								} else {
									$(".infoPass").text("Hasła nie są zgodne");
									$(".infoPass").attr("class", "alert alert-warning infoDiv infoPass topMargin10");
								}
							}else{
								$(".infoPass").text("Wpisz hasło");
								$(".infoPass").attr("class", "alert alert-warning infoDiv infoPass topMargin10");
							}
						}else{
							$(".infoPass").text("Błędne hasło");
							$(".infoPass").attr("class","alert alert-warning infoDiv infoPass topMargin10");
						}
					});
					$(".changeMail").click(function(){
						console.log("chyba dziala");
						var newMail=document.getElementById("emailReg").value;
						var newMail2=document.getElementById("emailRegRep").value;
						var password=document.getElementById("password").value;
						if (password=="test"){
							if(newMail!="" && newMail2!="") {
								if (newMail == newMail2) {
									$(".infoMail").text("Adres mailowy został zmieniony");
									$(".infoMail").attr("class", "alert alert-success infoDiv infoMail topMargin10");
								} else {
									$(".infoMail").text("Adresy mailowe nie są zgodne");
									$(".infoMail").attr("class", "alert alert-warning infoDiv infoMail topMargin10");
								}
							}else{
								$(".infoMail").text("Wpisz maila");
								$(".infoMail").attr("class", "alert alert-warning infoDiv infoMail topMargin10");
							}
						}else{
							$(".infoMail").text("Błędne hasło");
							$(".infoMail").attr("class","alert alert-warning infoDiv infoMail topMargin10");
						}
					});

});