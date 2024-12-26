const form = document.getElementById('userForm');
const formTitle = document.getElementById('formTitle');
const toggleForm = document.getElementById('toggleForm');
const emailField = document.getElementById('emailField');

let isLogin = true;

toggleForm.addEventListener('click', () => {
    isLogin = !isLogin;
    formTitle.innerText = isLogin ? 'Login' : 'Register';
    emailField.style.display = isLogin ? 'none' : 'block';
    toggleForm.innerHTML = isLogin
        ? "Don't have an account? <span class='text-highlight' style='cursor: pointer;'>Register</span>"
        : "Already have an account? <span class='text-highlight' style='cursor: pointer;'>Login</span>";
});

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const user = {
        username: document.getElementById('username').value,
        email: document.getElementById('email')?.value || '',
        password: document.getElementById('password').value,
    };

    const endpoint = isLogin ? '/login' : '/register';
    const response = await fetch(`http://127.0.0.1:5000${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(user),
    });

    const result = await response.json();
    alert(result.message || result.error);
});
