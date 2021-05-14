$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.datepicker').datepicker({
        format: "yyyy",
        yearRange: 5,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.modal').modal();
});