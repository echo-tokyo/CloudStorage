import './auth.css'
import { Link, useNavigate } from 'react-router-dom'
import Themes from '../mainPage/Themes'
import axios from 'axios'
import { useState } from 'react'

function Login () {
    const navigate = useNavigate()
    const [dataCorrect, setDataCorrect] = useState(true)

    const handleClick = (e) => {
        e.preventDefault()
        const formData = {
            email: e.target.email.value,
            password: e.target.password.value
        }

        axios.post('http://79.137.204.172/api/user/login/', formData, {headers:{'Content-Type': 'application/json'}})
        .then(response => {
            localStorage.setItem('token', response.data.token)
            navigate('/')
        })
        .catch(error => {
            console.error('Произошла ошибка при входе ', error.response.data)
            setDataCorrect(false)
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
                {dataCorrect == false && (
                    <p className='dataNotCorrect'>Неверные введенные данные</p>
                )}
                <div className="inps">
                    <input type="email" name='email' placeholder='Почта' required/>
                    <input type="password" name='password' placeholder='Пароль' required/>
                </div>
                <input type="submit" value="Войти"/>
            </form>
        </div>
        </>
    )
}

export default Login