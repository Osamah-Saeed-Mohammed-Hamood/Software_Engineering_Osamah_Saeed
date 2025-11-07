document.addEventListener('DOMContentLoaded', function() {
    const notifBtn = document.querySelector('.notification-dropdown .icon-btn');
    const dropdown = document.querySelector('.notification-dropdown .dropdown-content');

    if (!notifBtn || !dropdown) return;

    // فتح وإغلاق القائمة عند الضغط
    notifBtn.addEventListener('click', function(e) {
        e.stopPropagation(); // لمنع إغلاق القائمة فورًا
        dropdown.classList.toggle('show');
    });

    // إغلاق القائمة عند الضغط خارجها
    document.addEventListener('click', function() {
        dropdown.classList.remove('show');
    });
});
