

document.getElementById("calendar-days").addEventListener("click",function(e) {
  if(e.target && e.target.nodeName == "LI") {

    var monthYear = document.getElementById("selected-month").textContent;

    console.log(e.target.textContent);
    console.log(monthYear);
    // TODO invoke the bootstrap modal
    var myModal = new bootstrap.Modal(document.getElementById('reminderModal'));
    myModal.show();
  }
});


