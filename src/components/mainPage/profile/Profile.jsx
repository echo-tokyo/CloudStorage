import './profile.css'
import axios from 'axios'
import { useState } from 'react'
import ChangePassword from './changePassword/changePassword'
import ChangeUserData from './changeUserData/ChangeUserData'

function Profile ({profilePhoto, profileEmail, setProfileEmail, setProfilePhoto}) { 
    const [passChange, setPassChange] = useState(false)

    const sendProfileData = (e) => {
        e.preventDefault()
        setProfileEmail(e.target.email.value)
        const token = localStorage.getItem('token')
        const profileData = {
            email: e.target.email.value,
        }
        
        axios.put('http://79.137.204.172/api/user/edit-email/', profileData, {headers:{'Content-Type': 'application/json', "Authorization": `Bearer ${token}`}})
        .then(() => {
            document.querySelector('.send').style = `border: 2px solid lightgreen`
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
        .then(() => {
            document.querySelector('.send').style = `border: 2px solid lightgreen`
        })
        .catch((error) => {
            document.querySelector('.send').style = `border: 2px solid red`
            console.error('Произошла ошибка при смене пароля ', error) 
        })
    }   

    const photoUpload = (e) => {
        const token = localStorage.getItem('token')
        const file = e.target.files[0]
        const formData = new FormData()
        formData.append('photo', file)
        axios.put('http://79.137.204.172/api/user/edit-profile-photo/', formData, {headers: {'Authorization': `Bearer ${token}`}})
        .then(response => {
            setProfilePhoto(response.data.photo_url)
        })
        .catch(error => {
            console.error('Произошла ошибка при обновлении аватарки', error)
        })
    }
    return(
        <div className="modal-profile">
            <div className="modal-item">
                <p>Профиль</p>
                <div className="avatar" style={{backgroundImage: `url('${profilePhoto}')`}}></div>
                <form onChange={(e) => photoUpload(e)}>  
                    <input type="file" id="photo-upload"/>
                    <label htmlFor="photo-upload" className='download'>Загрузить фото</label>
                </form>
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