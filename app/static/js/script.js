document.addEventListener('DOMContentLoaded', function() {
    // Desktop menu toggle
    const desktopUserMenu = document.getElementById('desktopUserMenu');
    if (desktopUserMenu) {
        desktopUserMenu.addEventListener('click', function(e) {
            e.stopPropagation();
            const dropdown = document.getElementById('desktopDropdown');
            dropdown.classList.toggle('show');
        });
    }

    // Mobile menu toggle
    const mobileAvatar = document.getElementById('mobileAvatar');
    if (mobileAvatar) {
        mobileAvatar.addEventListener('click', function(e) {
            e.stopPropagation();
            const dropdown = document.getElementById('mobileUserDropdown');
            dropdown.classList.toggle('show');
            
            if (dropdown.classList.contains('show')) {
                dropdown.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    }

    // Close menus when clicking outside
    document.addEventListener('click', function() {
        const desktopDropdown = document.getElementById('desktopDropdown');
        if (desktopDropdown) {
            desktopDropdown.classList.remove('show');
        }
        
        const mobileDropdown = document.getElementById('mobileUserDropdown');
        if (mobileDropdown) {
            mobileDropdown.classList.remove('show');
        }
    });

    // Prevent dropdown close when clicking inside
    const desktopDropdown = document.getElementById('desktopDropdown');
    if (desktopDropdown) {
        desktopDropdown.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }

    const mobileDropdown = document.getElementById('mobileUserDropdown');
    if (mobileDropdown) {
        mobileDropdown.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
});