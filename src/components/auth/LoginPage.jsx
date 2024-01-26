import './auth.css'
import { Link, useNavigate } from 'react-router-dom'
import Themes from '../mainPage/Themes'
import axios from 'axios'

function Login () {
    const history = useNavigate()

    const handleClick = (e) => {
        e.preventDefault()
        localStorage.setItem('registered', 'yes')

        const formData = {
            email: e.target.email.value,
            password: e.target.password.value
        }

        axios.post('http://79.137.204.172/api/user/login/', JSON.stringify(formData))

        .then(response => {
            if (response.status == 200){
                const token = response.data.token
                localStorage.setItem('token', token)
                history('/')
            } else{
                throw new Error('network response not ok.')
            }
        })

        .then(data => {
            console.log('успешный ответ от сервера ', data)
        })
        
        .catch(error => {
            console.error('произошла ошибка при отправке запроса ', error)
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