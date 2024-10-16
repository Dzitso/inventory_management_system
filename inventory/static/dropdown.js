// Get all dropdown toggles
const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

// Add click event listener to each dropdown toggle
dropdownToggles.forEach(toggle => {
  toggle.addEventListener('click', function() {
    const dropdownMenu = this.nextElementSibling;
    dropdownMenu.classList.toggle('show');
  });
});

// Close dropdowns when clicking outside
window.addEventListener('click', function(event) {
  const dropdowns = document.querySelectorAll('.dropdown-menu.show');
  dropdowns.forEach(dropdown => {
    if (!dropdown.contains(event.target) && !dropdown.previousElementSibling.contains(event.target)) {
      dropdown.classList.remove('show');
    }
  });
});