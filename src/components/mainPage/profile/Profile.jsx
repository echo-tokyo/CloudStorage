import './profile.css'
import axios from 'axios'

function Profile () { 
    const sendProfileData = (e) => {
        e.preventDefault()
        const token = localStorage.getItem('token')

        const profileData = {
            email: e.target.email.value,
            name: e.target.name.value
        }
        
        console.log(profileData)
        axios.patch('http://79.137.204.172/api/user/edit/', profileData, {headers:{'Content-Type': 'application/json', "Authorization": `Bearer ${token}`}})
        .then((response) => {
            document.querySelector('.send').style = `border: 2px solid lightgreen`
            console.log(response.data)
        })
        .catch((error) => {
            document.querySelector('.send').style = `border: 2px solid red`
            console.error('ошибка епта', error) 
        })
    }   

    return(
        <div className="modal-profile">
            <div className="modal-item">
                <p>Профиль</p>
                <div className="avatar"></div>
                <input type="file" id="file-upload"/>
                <label htmlFor="file-upload" className='download'>Загрузить фото</label>
                <p className='subtitle'>JPG или PNG, мин 100 х 100 пикс, до 5 Mb</p>
            </div>
            <form action="" className='modal-form' onSubmit={(e) => sendProfileData(e)}>
                <input name='name' type="text" placeholder="ChelovekPayk"/>
                <input name='email' type="email" placeholder="example@gmail.com"/>
                <input name='password' type="password" placeholder="*********"/>
                <input className='send' type="submit" value="Сохранить"/>
            </form>
        </div>
    )
}

export default Profile