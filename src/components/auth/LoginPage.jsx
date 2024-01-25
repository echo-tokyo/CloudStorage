import './auth.css'
import { Link, useNavigate } from 'react-router-dom'
import Themes from '../mainPage/Themes'

function Login () {
    const history = useNavigate()

    const handleClick = (e) => {
        e.preventDefault()
        localStorage.setItem('registered', 'yes')
        history('/')
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
            <form action="" className="form-field">
                <div className="inps">
                    <input type="email" name="" id="" placeholder='Почта' />
                    <input type="password" name="" id="" placeholder='Пароль' />
                </div>
                <input type="submit" name="" id="" value="Войти" onClick={(e) => handleClick(e)}/>
            </form>
        </div>
        </>
    )
}

export default Login