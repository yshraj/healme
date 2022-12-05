var dateToday = new Date();
var dates = $("#date").datepicker({
    defaultDate: "+1w",
    changeMonth: true,
    numberOfMonths: 2,
    minDate: dateToday,
    maxDate: dateToday
});