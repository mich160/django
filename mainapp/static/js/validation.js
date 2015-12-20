/**
 * Created by Cezary on 20.12.2015.
 */

var validateLoginForm = function() {
	var uname = $(".loginForm #username").val();
	var pswd = $(".loginForm #password").val();
	if (uname == "" || pswd == "") {
		return false;
	} else {
		return true;
	}
}

var validateLogin = function(uname) {

	var unameValidMsg = "";

	if (uname == "") {
		unameValidMsg = "Pole nie może być puste!\n";
	}
	if (!(/^[A-Z0-9_]*$/i.test(uname))) {
		unameValidMsg += "Pole może zawierać tylko łacinskie litery oraz cyfry i _ ";
	}

	return unameValidMsg;
}

var validatePassword = function(pswd) {

	var pswdValidMsg = "";
	if (pswd.length < 7) {
		pswdValidMsg += "Hasło musi zawierać conajmniej 8 znaków! ";
	}

	if (!(/[0-9]/.test(pswd))) {
		pswdValidMsg += "Hasło musi zawierać conajmniej jedną cyfrę! ";
	}

	if (!(/[A-Z]/.test(pswd))) {
		pswdValidMsg += "Hasło musi zawierać conajmniej jedną wielką literę! ";
	}

	if (!(/[a-z]/.test(pswd))) {
		pswdValidMsg += "Hasło musi zawierać conajmniej jedną małą literę! ";
	}

	if (!(/[.,-\/#!$%\^&\*;:{}=\-_`~()]/.test(pswd))) {
		pswdValidMsg += "Hasło musi zawierać conajmniej jeden znak specjalny! .,-\/#!$%\^&\*;:{}=\-_`~() ";
	}

	if (pswd == "") {
		pswdValidMsg = "Pole nie może być puste! ";
	}
	return pswdValidMsg;
}

var validateEmail = function(email) {
	var emailValidMsg = "";
	if (!(/@/.test(email))) {
		emailValidMsg = "Niepoprawny mail ";
	}

	if (email == "") {
		emailValidMsg = "Pole nie może być puste! ";
	}
	return emailValidMsg;
}

var validatePswdRep = function(pswd, pswdRep) {
	var pswdRepValidMsg = "";
	if (!(pswd === pswdRep)) {
		pswdRepValidMsg = "Źle powtórzone hasło!";
	}
	return pswdRepValidMsg;
}

var validateEmailRep = function(email, emailRep) {
	var emailRepValidMsg = "";
	if (!(email === emailRep)) {
		emailRepValidMsg = "Źle powtórzony adres e-mail!";
	}
	return emailRepValidMsg;
}

var validateRegisterForm = function() {
	var uname = $(".regForm #usernameReg").val();
	var pswd = $(".regForm #passwordReg").val();
	var pswdRep = $(".regForm #passwordRegRep").val();
	var email = $(".regForm #emailReg").val();
	var emailRep = $(".regForm #emailRegRep").val();

	$("#usernameReg").tooltip('destroy');
	$("#passwordReg").tooltip('destroy');
	$("#passwordRegRep").tooltip('destroy');
	$("#emailReg").tooltip('destroy');
	$("#emailRegRep").tooltip('destroy');

	var unameValidMsg = validateLogin(uname);
	var pswdValidMsg = validatePassword(pswd);
	var emailValidMsg = validateEmail(email);
	var pswdRepValidMsg = validatePswdRep(pswd, pswdRep);
	var emailRepValidMsg = validateEmailRep(email, emailRep);

	setTimeout(function() {
		if (unameValidMsg != "") {
			$("#usernameReg").prop("title", unameValidMsg);
			$("#usernameReg").tooltip({
				trigger : 'manual'
			})
			$("#usernameReg").tooltip('show');
		}

		if (pswdValidMsg != "") {
			$("#passwordReg").prop("title", pswdValidMsg);
			$("#passwordReg").tooltip({
				trigger : 'manual'
			})
			$("#passwordReg").tooltip('show');
		}

		if (pswdRepValidMsg != "") {
			$("#passwordRegRep").prop("title", pswdRepValidMsg);
			$("#passwordRegRep").tooltip({
				trigger : 'manual'
			})
			$("#passwordRegRep").tooltip('show');
		}

		if (emailValidMsg != "") {
			$("#emailReg").prop("title", emailValidMsg);
			$("#emailReg").tooltip({
				trigger : 'manual'
			})
			$("#emailReg").tooltip('show');
		}

		if (emailRepValidMsg != "") {
			$("#emailRegRep").prop("title", emailRepValidMsg);
			$("#emailRegRep").tooltip({
				trigger : 'manual'
			})
			$("#emailRegRep").tooltip('show');
		}
	}, 300);

	if (unameValidMsg == "" && pswdValidMsg == "" && emailValidMsg == "" && pswdRepValidMsg == "" && emailRepValidMsg == "") {
		return true;
	} else {
		return false;
	}
}

$(document).ready(function() {
	$("#usernameReg").focusout(function() {
		$("#usernameReg").tooltip('destroy');
	});
	$("#passwordReg").focusout(function() {
		$("#passwordReg").tooltip('destroy');
	});
	$("#passwordRegRep").focusout(function() {
		$("#passwordRegRep").tooltip('destroy');
	});
	$("#emailReg").focusout(function() {
		$("#emailReg").tooltip('destroy');
	});
	$("#emailRegRep").focusout(function() {
		$("#emailRegRep").tooltip('destroy');
	});
});
