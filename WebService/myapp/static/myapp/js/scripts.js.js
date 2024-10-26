document.getElementById('show-register').addEventListener('click', function() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register').style.display = 'block';
});

document.getElementById('show-login').addEventListener('click', function() {
    document.getElementById('register').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
});