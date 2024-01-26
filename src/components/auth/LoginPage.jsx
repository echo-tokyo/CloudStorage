import './auth.css'
import { Link, useNavigate } from 'react-router-dom'
import Themes from '../mainPage/Themes'
import axios from 'axios'

function Login () {
    const navigate = useNavigate()

    const handleClick = (e) => {
        e.preventDefault()
        localStorage.setItem('registered', 'yes')

        const formData = {
            email: e.target.email.value,
            password: e.target.password.value
        }

        axios.post('http://79.137.204.172/api/user/login/', formData, {headers: {'Content-Type': 'application/json'}})

        .then(response => {
            const token = response.data.token
            localStorage.setItem('token', token)
            navigate('/')
        })

        .catch(error => {
            console.error('произошла ошибка при отправке запроса ', error.response.data)
        })
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