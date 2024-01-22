import './auth.css'
import { Link } from 'react-router-dom'

function Reg () {
    const handleClick = (e) => {
        e.preventDefault()
    }
    return(
        <div className="wrapper">
            <h1>Cloud Storage</h1>
            <Link className='link' to={'/login'}>Вход</Link>
            <form action="" className="form-field">
                <div className="inps">
                    <input type="email" name="" id="" placeholder='Почта' />
                    <input type="password" name="" id="" placeholder='Пароль' />
                </div>
                <input type="submit" name="" id="" value="Зарегистрироваться" onClick={(e) => handleClick(e)} />
            </form>
        </div>
    )
}

export default Reg