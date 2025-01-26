       // Validação de login
       const usuarios = [
        { login: 'admin', pass: 'admin' },
        { login: 'lucas', pass: 'lucas' },
        { login: 'mislene', pass: 'mislene' },
        { login: '1234', pass: '1234' }
    ];

    document.getElementById('btnLogar').addEventListener('click', function () {
        const usuario = document.getElementById('usuario').value.trim();
        const senha = document.getElementById('senha').value.trim();
        let valido = false;

        for (let i = 0; i < usuarios.length; i++) {
            if (usuario === usuarios[i].login && senha === usuarios[i].pass) {
                valido = true;
                break;
            }
        }

        if (valido) {
            alert('Login realizado com sucesso!');
            window.location.href = 'home.html';
        } else {
            alert('Usuário ou senha incorretos!');
        }
    });