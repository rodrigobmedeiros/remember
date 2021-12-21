const month_mapper = new Map();

month_mapper.set('January', '01');
month_mapper.set('February', '02');
month_mapper.set('March', '03');
month_mapper.set('April', '04');
month_mapper.set('May', '05');
month_mapper.set('June', '06');
month_mapper.set('July', '07');
month_mapper.set('August', '08');
month_mapper.set('September', '09');
month_mapper.set('October', '10');
month_mapper.set('November', '11');
month_mapper.set('December', '12');


document.getElementById("calendar-days").addEventListener("click",function(e) {
  if(e.target && e.target.nodeName == "LI") {

    var day = e.target.textContent;
    var monthYear = document.getElementById("selected-month").textContent.split(' ')
    var month = month_mapper.get(monthYear[0]);
    var year = monthYear[1];

    if (day.length == 1) {
      day = '0' + day
    }

    var completeDate = year + '-' + month + '-' + day

    // TODO invoke the bootstrap modal
    var myModal = new bootstrap.Modal(document.getElementById('reminderModal'));
    var dateField = document.getElementById("id_date");


    if (e.target.className != "calendar-day calendar-day--not-current"){
      myModal.show();
      dateField.value = completeDate;
    }
  }
});


function getMonthYear(){
  return document.getElementById("selected-month").innerText;
}
