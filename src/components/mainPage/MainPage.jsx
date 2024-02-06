import './mainPage.css'
import Header from './header/Header'
import FileItem from './fileItem/FileItem'
import filesData from './file.data'
import {useEffect, useState } from 'react'
import Themes from './Themes'
import Modal from './modal/Modal'
import Profile from './profile/profile'
import axios from 'axios'

function MainPage(){
    const [files, setFile] = useState(filesData)
    const [profilePhoto, setProfilePhoto] = useState('')
    const [profileEmail, setProfileEmail] = useState('')

    useEffect(() => {
        const token = localStorage.getItem('token')
        axios.get('http://79.137.204.172/api/user/get-profile-info/', {headers: {'Authorization': `Bearer ${token}`}})
        .then(response => {
            setProfilePhoto(response.data.photo_url)
            setProfileEmail(response.data.email)
        })
        .catch((error) => {
            setProfilePhoto('../../../../public/i.webp')
            console.error('Произошла ошибка при получении данных профиля ', error)
        })

        axios.get('http://79.137.204.172/api/storage/get-root-dir/', {headers: {'Authorization': `Bearer ${token}`}})
        .then(response => {
            localStorage.setItem('rootDir', response.data.root_dir)
        })
        .catch(error => {
            console.error('Произошла ошибка при получении root-dir', error)
        })

        axios.get('http://79.137.204.172/api/storage/get-file-list/', {
            params: { folder_id: localStorage.getItem('rootDir') },
            headers: {'Authorization': `Bearer ${token}`}
        })
        .then(response => {
            setFile({id: response.data.id, name: response.data.name, size: response.data.size + ' байт'})
            console.log(response.data)
        })
        .catch(error => {
            console.error('Произошла ошибка при получении данных', error)
        })
    }, [])
    
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
                <Header changeTheme={changeTheme} modalOpen={modalOpen} profileClick={profileClick} profilePhoto={profilePhoto} setFile={setFile}/>
                <main>
                    {modal && <Modal />}
                    {profile && <Profile profilePhoto={profilePhoto} profileEmail={profileEmail} setProfileEmail={setProfileEmail}/>}
                    {files.length ? (
                        files.map(file => <FileItem key={file.id} file={file} setFile={setFile} />)
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