import './auth.css'
import { Link, useNavigate } from 'react-router-dom'
import Themes from '../mainPage/Themes'
import axios from 'axios'
import { useState } from 'react'

function Reg () {
    const navigate = useNavigate()
    const [dataCorrect, setDataCorrect] = useState(undefined)

    const handleClick = (e) => {
        e.preventDefault()
        const formData = {
            email: e.target.email.value,
            password: e.target.password.value
        }

        axios.post('http://79.137.204.172/api/user/reg/', formData, {headers: {'Content-Type': 'application/json'}})
        .then(response => {
            localStorage.setItem('token', response.data.token)
            navigate('/')
        })
        .catch(error => {
            console.error('Произошла ошибка при регистрации, ', error)
            setDataCorrect(false)
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
                {dataCorrect == false &&(
                    <p className="dataNotCorrect">Неверные введенные данные</p>
                )}
                <div className="inps">
                    <input type="email" name="email" placeholder='Почта' required/>
                    <input id='pass' type="password" name="password" placeholder='Пароль' required/>
                </div>
                <input type="submit" value="Зарегистрироваться" />
            </form>
        </div>
    )
}

export default Reg