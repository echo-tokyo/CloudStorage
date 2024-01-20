import './loginPage.css'

function Login () {
    return(
        <div className="wrapper">
            <h1>Cloud Storage</h1>
            <form action="" className="form-field">
                <div className="inps">
                    <input type="email" name="" id="" placeholder='Почта' />
                    <input type="password" name="" id="" placeholder='Пароль' />
                </div>
                <input type="submit" name="" id="" value="Войти" />
            </form>
        </div>
    )
}

export default Login