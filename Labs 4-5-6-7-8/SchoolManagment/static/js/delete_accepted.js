document.addEventListener('click', function (e) {
    const btn = e.target.closest('.js-delete');
    if (!btn) return;

    e.preventDefault();
    const name = btn.dataset.name || '';
    const url  = btn.dataset.url;
    const type = btn.dataset.type || 'العنصر'; // النوع (طالب، معلم ...)

    if (!url) return;

    const ok = confirm(`هل أنت متأكد أنك تريد حذف ${type}: ${name}؟`);
    if (ok) {
        window.location.href = url;
    }
});
