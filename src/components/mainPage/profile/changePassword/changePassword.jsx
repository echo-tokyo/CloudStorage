function ChangePassword({setPassChange, sendNewPassword}) {
    return(
        <form action="" className='modal-form' onSubmit={(e) => sendNewPassword(e)}>
            <p className="pLink"  onClick={() => setPassChange(false)}>Назад</p>
            <input name='oldPassword' type="password" placeholder="Старый пароль"/>
            <input name='newPassword' type="password" placeholder="Новый пароль"/>
            <input className='send' type="submit" value="Сохранить"/>
        </form>
    )
}
export default ChangePassword
