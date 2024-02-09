function ChangeUserData({sendProfileData, setPassChange, profileEmail}) {
    return(
        <form className='modal-form' onSubmit={(e) => sendProfileData(e)}>
            <p className="pLink" onClick={() => setPassChange(true)}>Сменить пароль</p>
            <input name='email' type="email" placeholder={profileEmail}/>
            <input className='send' type="submit" value="Сохранить"/>
        </form>
    )
}
export default ChangeUserData