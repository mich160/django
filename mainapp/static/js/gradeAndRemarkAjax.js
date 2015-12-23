/**
 * Created by Targon on 15.12.2015.
 */
$(document).ready(function () {

    setupAjax();

    $(".classSelection").change(function () {
        managePeopleSelector();
    });

    var managePeopleSelector = function () {
        var classSelected = $(".classSelection").val().trim();

        $.post("fetchPeopleFromClass", {classSelected: classSelected}, function (data) {
            var interestingData = data.studentsList;
            var selectionElem = $(".peopleSelection");
            for (c in interestingData) {
                var newOption = $("<option>");
                newOption.attr('value', interestingData[c]);
                newOption.text(interestingData[c]);
                selectionElem.append(newOption);
            }

        });

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
        });

    };

    $(".saveGrade").click(function () {  // teacherGrades.html
        var selectedStudents = $(".peopleSelection").val();
        if (selectedStudents != null) {
            var forWhat = $(".forWhat").val().trim();
            var classSelected = $(".classSelection").text().trim();
            var subjectSelected = $(".subjectList").val().trim();
            var gradeSelection = $('.gradeSelection').val().trim();
            var sign = $('.markSign').val().trim();

            $.post("saveGrade", {
                forWhat: forWhat,
                clazz: classSelected,
                subjectSelected : subjectSelected,
                students: selectedStudents,
                grade: gradeSelection,
                modifier: sign
            }, function () {
                $(".infoDiv").text("Ocena zapisana");
                $(".infoDiv").attr("class", "alert alert-success infoDiv topMargin10");
            })

        } else {
            $(".infoDiv").text("Nie wybrano ucznia");
            $(".infoDiv").attr("class", "alert alert-warning infoDiv topMargin10");
        }
    });

    $(".saveRemark").click(function () { // teacherRemark.html
        var selectedStudents = $(".peopleSelection").val();
        if (selectedStudents != null) {
            var remarkText = $(".remarkText").val().trim();
            var classSelected = $(".classSelection").text().trim();

            $.post("saveRemark", {
                remarkText: remarkText,
                students: selectedStudents
            }, function () {
                $(".infoDiv").text("Uwaga zapisana");
                $(".infoDiv").attr("class", "alert alert-success infoDiv topMargin10");
            })

        } else {
            $(".infoDiv").text("Nie wybrano ucznia");
            $(".infoDiv").attr("class", "alert alert-warning infoDiv topMargin10");
        }
    });

    managePeopleSelector();
    $("textarea").text($("textarea").text().trim())
});