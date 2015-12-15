/**
 * Created by Targon on 15.12.2015.
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

					$(".classSelection").change(function() {
					managePeopleSelector();
					});
					var managePeopleSelector= function() {
					var classSelected=$(".classSelection").val().trim();


					$.post("fetchPeopleFromClass", {classSelected: classSelected}, function(data) {
						var interestingData = data.studentsList;
						var selectionElem =	$(".peopleSelection");
						for(c in interestingData) {
							var newOption = $("<option>");
							newOption.attr('value', interestingData[c]);
							newOption.text(interestingData[c]);
							selectionElem.append(newOption);
						}

						});
					};

					$(".saveRemark").click(function() {
						var selectedStudents=$(".peopleSelection").val();
						if(selectedStudents != null) {
						var remarkText = $(".remarkText").val().trim();
						var classSelected=$(".classSelection").text().trim();

						console.log(selectedStudents);

						$.post("saveRemark", {remarkText: remarkText, clazz: classSelected, students: selectedStudents}, function() {
							$(".infoDiv").text("Uwaga zapisana");
							$(".infoDiv").attr("class", "alert alert-success");
						})

						}else{
							$(".infoDiv").text("Nie wybrano ucznia");
							$(".infoDiv").attr("class", "alert alert-warning");
						}
					});
						managePeopleSelector();
						$("textarea").text($("textarea").text().trim())
					});