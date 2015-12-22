/**
 * Created by Cezary on 22.12.2015.
 */


$(document).ready(function () {

    setupAjax();

    var manageSubjectSelector = function () {
        var classSelected = $(".classSelection").val().trim();

        $.post("fetchClassSubject", {classSelected: classSelected}, function (data) {
            var interestingData = data.subjectList;
            var selectionElem = $(".subjectList");
            selectionElem.empty();
            for (var c in interestingData) {
                var newOption = $("<option>");
                newOption.attr('value', interestingData[c]);
                newOption.text(interestingData[c]);
                selectionElem.append(newOption);
            }
            $(".subjectList").change(function () {
                manageLessonsSelector();
            });
            manageLessonsSelector();

        });

    };

    var manageLessonsSelector = function () {

        var subjectSelected = $(".subjectList").val().trim();

        $.post("fetchClassesLessons", {
            subjectSelected: subjectSelected
        }, function (data) {
            var interestingData = data.lessonList;
            var selectionElem = $(".lessonList");
            selectionElem.empty();
            for (var c in interestingData) {
                var newOption = $("<option>");
                newOption.attr('value', interestingData[c]);
                newOption.text(interestingData[c]);
                selectionElem.append(newOption);
            }
            fetchAbsenceManager();
        });
    };

    var fetchAbsenceManager = function () {

        var classSelected = $(".classSelection").val().trim();
        var subjectSelected = $(".subjectList").val().trim();
        var lessonSelected = $(".lessonList").val().trim();
        var lessonDate = lessonSelected.split(" ");
        lessonDate = lessonDate[1] + " " + lessonDate[2];

        $.post("fetchLessonAbsence", {
            classSelected: classSelected,
            subjectSelected: subjectSelected,
            lessonDate: lessonDate
        }, function (data) {
            console.log(data.absList);
            var interestingData = JSON.parse(data);
            console.log(interestingData);


            var absDiv = $(".absDisplay");
            absDiv.empty();
            var head = $("<thead><th class='studentName'>Student</th><th class='present'>Obecny</th><th class='absent'>Nieobecny</th></thead>");
            var body = $("<tbody></tbody>");

            absDiv.append(head);
            absDiv.append(body);


            // var selectionElem = $(".lessonList");
            for (var c in interestingData) {

                var row = $("<tr class='studentRow'>");

                var studentName = $("<td class='studentName'>");
                studentName.text(c);
                var presentPlaceholder = $("<td class='presentPh'>");
                var absentPlaceholder = $("<td class='absentPh'>");

                var inputPresent = $("<input type='radio' name='" + c + "' value='false'>");
                var inputAbsent = $("<input type='radio' name='" + c + "' value='true'>");

                if (interestingData[c] === true) {
                    inputAbsent.attr("checked", "checked");
                } else {
                    inputPresent.attr("checked", "checked");
                }

                presentPlaceholder.append(inputPresent);
                absentPlaceholder.append(inputAbsent);

                row.append(studentName);
                row.append(presentPlaceholder);
                row.append(absentPlaceholder);

                body.append(row);
            }

            var lastRow = $("<tr><td colspan='3'><button class='btn btn-default sendAbs'>Zapisz</button></td></tr>");
            absDiv.append(lastRow);

            $(".sendAbs").click(function () {
                var rows = $(".absDisplay .studentRow");

                var classSelected = $(".classSelection").val().trim();
                var subjectSelected = $(".subjectList").val().trim();
                var lessonSelected = $(".lessonList").val().trim();
                var lessonDate = lessonSelected.split(" ");
                lessonDate = lessonDate[1] + " " + lessonDate[2];


                var absMap = {};
                $.each(rows, function (index, item) {

                    var studentName = $(item).find(".studentName").text();
                    var present = $(item).find("input:checked").val();

                    absMap[studentName] = present;

                })

                $(this).addClass("disabled");
                var that = this;

                $.post("submitAbsences", {
                    absMap: JSON.stringify(absMap),
                    subjectSelected: subjectSelected,
                    lessonDate: lessonDate,
                    classSelected: classSelected
                }, function () {
                    $(that).removeClass("disabled");
                });


            })


        });
    };

    $(".classSelection").change(function () {
        manageSubjectSelector();
    });


    manageSubjectSelector();

});