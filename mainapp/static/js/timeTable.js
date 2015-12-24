/**
 * Created by Cezary on 24.12.2015.
 */


$(document).ready(function () {
    setupAjax();
    $('table').addClass('table table-striped');
    $('th:not(.lessonTimeHeader)').addClass('dayHeader')
    tables = $('table');

    var classNameArr = ['classTDBlue', 'classTDRed', 'classTDGreen', 'classTDOrange', 'classTDLightBlue', 'classTDLightGreen', 'classTDLightOrange'];
    tables.each(function (index, item) {

        var items = $(item).find('td:not(:empty):not(.lessonTime)');
        var itemGroup = {};

        items.each(function (index, item) {
            text = $(item).text();
            if (itemGroup[text] === undefined) {
                itemGroup[text] = [];
            }
            itemGroup[text].push(item);
        });

        var i = 0;
        for (key in itemGroup) {


            var className = classNameArr[i];
            i += 1;


            $(itemGroup[key]).each(function (index, item) {
                $(item).addClass('classTD dayHeader ' + className)
            })

        }


    });


    $('.savePDF').click(function () {

        var table = $($(this).closest('ul').siblings('table')[0]).html();

        console.log(table);

        $.post("getTimeTablePDF", {
            tbl:table
        }, function () {
            console.log("im back");
        })

    })


});