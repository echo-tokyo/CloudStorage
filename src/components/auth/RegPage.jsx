import './auth.css'
import { Link } from 'react-router-dom'
import Themes from '../mainPage/Themes'

function Reg () {
    const handleClick = (e) => {
        e.preventDefault()

        const formData = {
            email: e.target.email.value,
            password: e.target.password.value
        }

        fetch('http://79.137.204.172/api/user/reg/', {
            method: 'POST',
            body: JSON.stringify(formData)
        })

        .then(response => {
            if(response.ok) {
              return response.json();
            }
            throw new Error('Network response was not ok.');
        })

        .then(data => {
            console.log('Успешный ответ от сервера', data);
        })

        .catch(error => {
            console.error('Произошла ошибка при отправке запроса', error);
        });
    }
    return(
        <div className="wrapper">
            <h1>Cloud Storage</h1>
            <Themes defaultTheme={false}>
                {() => (
                    <Link className='link' to={'/login'}>Вход</Link>
                )}
            </Themes>
            <form action="" className="form-field" onSubmit={(e) => handleClick(e)}>
                <div className="inps">
                    <input type="email" name="email" placeholder='Почта' />
                    <input type="password" name="password" placeholder='Пароль' />
                </div>
                <input type="submit" value="Зарегистрироваться" />
            </form>
        </div>
    )
}

export default Reg