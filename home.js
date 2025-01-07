fetch('counties.txt')
function toggleDropdown() {
    var menu = document.querySelector('.dropdown-menu');
    menu.classList.toggle('show');
}
function printCounty() {
    
}
// Filter the dropdown options based on search input
// function filterFunction() {
//     var input = document.getElementById("searchInput");
//     var filter = input.value.toLowerCase();
//     var list = document.getElementById("dropdownList");
//     var items = list.getElementsByTagName("li");

//     // Loop through all the items in the dropdown list
//     for (var i = 0; i < items.length; i++) {
//         var a = items[i].getElementsByTagName("a")[0];
//         if (a) {
//             var txtValue = a.textContent || a.innerText;
//             if (txtValue.toLowerCase().indexOf(filter) > -1) {
//                 items[i].style.display = "";
//             } else {
//                 items[i].style.display = "none";
//             }
//         }
//     }
// }

// // Close the dropdown if the user clicks outside of it
// window.onclick = function(event) {
//     if (!event.target.matches('.dropdown-btn') && !event.target.matches('.dropdown-menu, .dropdown-menu *')) {
//         var dropdowns = document.querySelectorAll('.dropdown-menu');
//         for (var i = 0; i < dropdowns.length; i++) {
//             var openDropdown = dropdowns[i];
//             openDropdown.classList.remove('show');
//         }
//     }
// }

document.getElementById('stateDropdown').addEventListener('change', function() {
    var selectedValue = this.value;
    if (selectedValue) {
      window.location.href = selectedValue; // Redirect to the map link
    }
  });