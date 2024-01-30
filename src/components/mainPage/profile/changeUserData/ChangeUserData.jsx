function ChangeUserData({sendProfileData, setPassChange}) {
    return(
        <form action="" className='modal-form' onSubmit={(e) => sendProfileData(e)}>
            <p className="pLink" onClick={() => setPassChange(true)}>Сменить пароль</p>
            <input name='email' type="email" placeholder="example@gmail.com"/>
            <input className='send' type="submit" value="Сохранить"/>
    </form>
    )
}
export default ChangeUserData