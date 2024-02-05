import './profile.css'
import axios from 'axios'
import { useState } from 'react'
import ChangePassword from './changePassword/changePassword'
import ChangeUserData from './changeUserData/ChangeUserData'

function Profile ({profilePhoto, profileEmail, setProfileEmail}) { 
    const [passChange, setPassChange] = useState(false)

    const sendProfileData = (e) => {
        e.preventDefault()

        setProfileEmail(e.target.email.value)

        const token = localStorage.getItem('token')

        const profileData = {
            email: e.target.email.value,
        }
        
        axios.put('http://79.137.204.172/api/user/edit-email/', profileData, {headers:{'Content-Type': 'application/json', "Authorization": `Bearer ${token}`}})

        .then((response) => {
            document.querySelector('.send').style = `border: 2px solid lightgreen`
            console.log(response.data)
        })

        .catch((error) => {
            document.querySelector('.send').style = `border: 2px solid red`
            console.error('Произошла ошибка при смене почты ', error) 
        })
    }

    const sendNewPassword = (e) => {
        e.preventDefault()
        const token = localStorage.getItem('token')

        const newPasswrodData = {
            old_password: e.target.oldPassword.value,
            new_password: e.target.newPassword.value
        }

        axios.put('http://79.137.204.172/api/user/change-password/', newPasswrodData, {headers:{'Content-Type': 'application/json', "Authorization": `Bearer ${token}`}})

        .then((response) => {
            document.querySelector('.send').style = `border: 2px solid lightgreen`
            console.log(response.data)
        })

        .catch((error) => {
            document.querySelector('.send').style = `border: 2px solid red`
            console.error('Произошла ошибка при смене пароля ', error) 
        })
    }   

    return(
        <div className="modal-profile">
            <div className="modal-item">
                <p>Профиль</p>
                <div className="avatar" style={{backgroundImage: `url('${profilePhoto}')`}}></div>
                <input type="file" id="file-upload"/>
                <label htmlFor="file-upload" className='download'>Загрузить фото</label>
                <p className='subtitle'>JPG или PNG, мин 100 х 100 пикс, до 5 Mb</p>
            </div>
            {passChange == false ? (
                <ChangeUserData setPassChange={setPassChange} sendProfileData={sendProfileData} profileEmail={profileEmail} />
                ) : (
                <ChangePassword setPassChange={setPassChange} sendNewPassword={sendNewPassword} />
            )}
        </div>
    )
}

export default Profile