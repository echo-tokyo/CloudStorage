import './auth.css'
import { Link } from 'react-router-dom'

function Login () {
    const handleClick = (e) => {
        e.preventDefault()
        localStorage.setItem('registered', 'yes')
    }
    return(
        <div className="wrapper">
            <h1>Cloud Storage</h1>
            <Link className='link' to={'/reg'}>Регистрация</Link>    
            <form action="" className="form-field">
                <div className="inps">
                    <input type="email" name="" id="" placeholder='Почта' />
                    <input type="password" name="" id="" placeholder='Пароль' />
                </div>
                <input type="submit" name="" id="" value="Войти" onClick={(e) => handleClick(e)}/>
            </form>
        </div>
    )
}

export default Login