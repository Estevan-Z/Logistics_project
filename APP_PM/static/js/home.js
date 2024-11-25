document.getElementById('theme-toggle').addEventListener('click', function() {
    document.body.classList.toggle('light-theme');
    const icon = this.querySelector('i');
    if (document.body.classList.contains('light-theme')) {
        icon.classList.replace('ri-sun-line', 'ri-moon-line');
    } else {
        icon.classList.replace('ri-moon-line', 'ri-sun-line');
    }
});

// Sidebar collapse toggle
document.getElementById('toggle-sidebar').addEventListener('click', function() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('collapsed');
    const icon = this.querySelector('i');
    if (sidebar.classList.contains('collapsed')) {
        icon.classList.replace('ri-menu-fold-line', 'ri-menu-unfold-line');
    } else {
        icon.classList.replace('ri-menu-unfold-line', 'ri-menu-fold-line');
    }
});