document.addEventListener('DOMContentLoaded', function() {
    // This code targets both login and register password fields
    const togglePassword = document.querySelector('.toggle-password');
    // Using a more general selector to work on both pages
    const passwordInput = document.querySelector('#id_password, #id_password1'); 

    if (togglePassword && passwordInput) {
        togglePassword.addEventListener('click', function () {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            
            this.classList.toggle('fa-eye');
            this.classList.toggle('fa-eye-slash');
        });
    }
    
});