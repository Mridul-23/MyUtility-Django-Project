document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelector('label[for="id_username"]').textContent = 'Enter Username';
    document.querySelector('label[for="id_password1"]').textContent = 'Enter Password';
    document.querySelector('label[for="id_password2"]').textContent = 'Confirm Password';
});