import './auth.css'
import { Link } from 'react-router-dom'
import Themes from '../mainPage/Themes'
import axios from 'axios'

function Reg () {
    const handleClick = (e) => {
        e.preventDefault()

        const formData = {
            email: e.target.email.value,
            password: e.target.password.value
        }

        console.log(formData)
        console.log(JSON.stringify(formData))

        axios.post('http://79.137.204.172/api/user/reg/', formData, {headers: {'Content-Type': 'application/json'}})

        .then(response => {
            console.log(response.data)
        })

        .catch(error => {
            console.error('произошла ошибка при отправке запроса, ', error.response.data)
        })
    }
    return(
        <div className="wrapper">
            <h1>Cloud Storage</h1>
            <Themes defaultTheme={false}>
                {() => (
                    <Link className='link' to={'/login'}>Вход</Link>
                )}
            </Themes>
            <form className="form-field" onSubmit={(e) => handleClick(e)}>
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