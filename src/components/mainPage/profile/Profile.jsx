import './profile.css'

function Profile () {    
    return(
        <div className="modal-profile">
            <div className="modal-item">
                <p>Профиль</p>
                <div className="avatar"></div>
                <input type="file" id="file-upload"/>
                <label htmlFor="file-upload" className='download'>Загрузить фото</label>
                <p className='subtitle'>JPG или PNG, мин 100 х 100 пикс, до 5 Mb</p>
            </div>
            <form action="" className='modal-form'>
                <input type="text" value="ChelovekPayk"/>
                <input type="email" value="example@gmail.com"/>
                <input type="password" value="*********"/>
                <input type="submit" placeholder="Сохранить"/>
            </form>
        </div>
    )
}

export default Profile