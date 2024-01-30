import './mainPage.css'
import Header from './header/Header'
import FileItem from './fileItem/FileItem'
import filesData from './file.data'
import { useEffect, useState } from 'react'
import Themes from './Themes'
import Modal from './modal/Modal'
import Profile from './profile/profile'
import axios from 'axios'

function MainPage(){
    const [profilePhoto, setProfilePhoto] = useState('')
    useEffect(() => {
        const token = localStorage.getItem('token')
        axios.get('http://79.137.204.172/api/user-profile/get/', {headers: {Authorization: `Bearer ${token}`}})
        .then(response => {
            setProfilePhoto(response.data.photo_url)
        })
        .catch((error) => {
            setProfilePhoto('../../../../public/i.webp')
            console.error('Произошла ошибка при получении аватарки ', error)
        })
    }, [])
    
    const [files, setFile] = useState(filesData)

    const [modal, setModal] = useState(false)
    const modalOpen = () => {
        setModal(!modal)
        setProfile(false)
    }

    const [profile, setProfile] = useState(false)
    const profileClick = () => {
        setProfile(!profile)
        setModal(false)
    }
    return(
        <Themes defaultTheme={false}>
            {(changeTheme) => (
                <>
                <Header changeTheme={changeTheme} modalOpen={modalOpen} profileClick={profileClick} profilePhoto={profilePhoto} />
                <main>
                    {modal && <Modal />}
                    {profile && <Profile profilePhoto={profilePhoto}/>}
                    {files.length ? (
                        files.map(file => <FileItem key={file.id} file={file} setFile={setFile}/>)
                    ) : (
                        <p>There are no files</p>
                    )}
                </main>
                </>
            )}
        </Themes>
    )
}

export default MainPage 