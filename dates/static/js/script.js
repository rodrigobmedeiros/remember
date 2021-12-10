const month_mapper = new Map();

month_mapper.set('January', '1');
month_mapper.set('February', '2');
month_mapper.set('March', '3');
month_mapper.set('April', '4');
month_mapper.set('May', '5');
month_mapper.set('June', '6');
month_mapper.set('July', '7');
month_mapper.set('August', '8');
month_mapper.set('September', '9');
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
    myModal.show();
    
    dateField.value = completeDate;
  }
});


