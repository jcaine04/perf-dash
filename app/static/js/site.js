/**
 * Created by jcaine on 5/5/14.
 */

$(document).ready(function () {

    // select all checkboxes when the select all checkbox is checked
    $("#select-all").click(function () {
        $(".instances").prop('checked', $(this).prop('checked'));
    });

    // date picker
    $(function() {
        $(".datepicker").datepicker();
    });

    // time picker
    $(function() {
        $(".timepicker").timepicker();
    });

    // disable end date and time if live checkbox is checked
    $("#live").click(function () {
        if($("#live").is(":checked")){
            $("#end-date").val('');
            $("#end-time").val('');
            $("#end-date").prop("disabled", true);
            $("#end-time").prop("disabled", true);
        } else {
            $("#end-date").prop("disabled", false);
            $("#end-time").prop("disabled", false);
        }
    });
});