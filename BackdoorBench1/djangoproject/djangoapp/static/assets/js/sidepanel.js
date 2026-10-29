// Toggle the sidebar visibility
document.addEventListener('DOMContentLoaded', function() {
    const sidepanel = document.getElementById('app-sidepanel');
    const sidepanelDrop = document.getElementById('sidepanel-drop');
    const closeBtn = document.getElementById('sidepanel-close');

    // Toggle visibility
    function toggleSidebar() {
        sidepanel.classList.toggle('sidepanel-visible');
        sidepanelDrop.classList.toggle('show');
    }

    // Close sidebar when clicking the overlay
    sidepanelDrop.addEventListener('click', toggleSidebar);

    // Close sidebar when close button is clicked
    closeBtn.addEventListener('click', function(e) {
        e.preventDefault();
        toggleSidebar();
    });
});
