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

                var studentName = $("<td>");
                studentName.text(c);
                var presentPlaceholder = $("<td>");
                var absentPlaceholder = $("<td>");

                var inputPresent = $("<input type='radio' name='" + c + "'>");
                var inputAbsent = $("<input type='radio' name='" + c + "'>");

                if (interestingData[c] === false) {
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
                var absMap = {};
                $.each(rows, function(index, item){
                    


                })













            })





        });
    };

    $(".classSelection").change(function () {
        manageSubjectSelector();
    });


    manageSubjectSelector();

});