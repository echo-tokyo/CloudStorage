import './auth.css'
import { Link, useNavigate } from 'react-router-dom'
import Themes from '../mainPage/Themes'

function Login () {
    const history = useNavigate()

    const handleClick = (e) => {
        e.preventDefault()
        localStorage.setItem('registered', 'yes')

        const formData = {
            email: e.target.email.value,
            password: e.target.password.value
        }

        fetch('http://79.137.204.172/api/user/login/', {
            method: 'POST',
            body: JSON.stringify(formData)
        })

        .then(response => {
            if (response.ok) {
              return response.json();
            }
            throw new Error('Network response was not ok.');
        })

        .then(data => {
            const token = data.token;
            localStorage.setItem('token', token);
            history('/');
        })
        
        .catch(error => {
            console.error('Произошла ошибка при отправке запроса', error);
        });
    }

    return(
        <>
        <div className="wrapper">
            <h1>Cloud Storage</h1>
            <Themes defaultTheme={false}>
                {() => (
                    <Link className='link' to={'/reg'}>Регистрация</Link>
                )}
            </Themes>
            <form action="" className="form-field" onSubmit={(e) => handleClick(e)}>
                <div className="inps">
                    <input type="email" name='email' placeholder='Почта' />
                    <input type="password" name='password' placeholder='Пароль' />
                </div>
                <input type="submit" value="Войти"/>
            </form>
        </div>
        </>
    )
}

export default Login