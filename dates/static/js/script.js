var monthYear = document.getElementById("selected-month").textContent;
var myModal = new bootstrap.Modal("#reminderModal");

document.getElementById("calendar-days").addEventListener("click",function(e) {
  if(e.target && e.target.nodeName == "LI") {
    console.log(e.target.textContent);
    // TODO invoke the bootstrap modal
    myModal.show();
  }
});


