document.addEventListener('DOMContentLoaded', function() {
    const desktopUserMenu = document.getElementById('desktopUserMenu');
    const dropdownDesktop = document.getElementById('desktopDropdown');
    const dropdownMobile = document.getElementById('mobileUserDropdown');
    const mobileAvatar = document.getElementById('mobileAvatar');

    if (desktopUserMenu) {
        desktopUserMenu.addEventListener('click', function(e) {
            e.stopPropagation();

            dropdownDesktop.classList.toggle('show');
        });
    }

    // Mobile menu toggle
    
    if (mobileAvatar && dropdownMobile) {
        mobileAvatar.addEventListener('click', function(e) {
            e.stopPropagation();

            dropdownMobile.classList.toggle('show');
            if (dropdownMobile.classList.contains('show')) {
                dropdownMobile.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    }

    // Close menus when clicking outside
    document.addEventListener('click', function() {
        if (dropdownDesktop) {
            dropdownDesktop.classList.remove('show');
        }
        
        if (dropdownMobile) {
            dropdownMobile.classList.remove('show');
        }
    });
});