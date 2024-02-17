import './mainPage.css'
import Header from './header/Header'
import FileItem from './fileItem/FileItem'
import {useEffect, useState } from 'react'
import Themes from './Themes'
import Modal from './modal/Modal'
import Profile from './profile/Profile'
import axios from 'axios'

function MainPage(){
    const token = localStorage.getItem('token')
    const [files, setFiles] = useState([])
    const [profilePhoto, setProfilePhoto] = useState('')
    const [profileEmail, setProfileEmail] = useState('')
    
    const formatFileSize = (sizeInBytes) => {
        let suffix = 'байт';

        switch (true) {
            case sizeInBytes < 1024:
                suffix = 'байт';
                break;
            case sizeInBytes < 1024 * 1024:
                sizeInBytes = (sizeInBytes / 1024).toFixed(1);
                suffix = 'КБ';
                break;
            case sizeInBytes < 1024 * 1024 * 1024:
                sizeInBytes = (sizeInBytes / (1024 * 1024)).toFixed(1);
                suffix = 'МБ';
                break;
            default:
                sizeInBytes = (sizeInBytes / (1024 * 1024 * 1024)).toFixed(1);
                suffix = 'ГБ';
        }

        return sizeInBytes + ' ' + suffix;
    };

    useEffect( () => {
        const fetchData = async () => {
            await axios.get('http://79.137.204.172/api/user/get-profile-info/', {headers: {'Authorization': `Bearer ${token}`}})
            .then(response => {
                setProfilePhoto(response.data.photo_url)
                setProfileEmail(response.data.email)
            })
            .catch((error) => {
                setProfilePhoto('../../../../public/i.webp')
                console.error('Произошла ошибка при получении данных профиля ', error)
            })
    
            await axios.get('http://79.137.204.172/api/storage/get-root-dir/', {headers: {'Authorization': `Bearer ${token}`}})
            .then(response => {
                localStorage.setItem('rootDir', response.data.root_dir)
            })
            .catch(error => {
                console.error('Произошла ошибка при получении root-dir', error)
            })
    
            await axios.post('http://79.137.204.172/api/storage/get-file-list/', {folder_id: Number(localStorage.getItem('rootDir'))}, {headers: {'Authorization': `Bearer ${token}`}})
            .then(response => {
                const files = response.data.map(file => (
                    {
                        id: file.id,
                        name: file.name,
                        size: formatFileSize(file.size)
                    }
                    ))
                setFiles(files)
            })
            .catch(error => {
                console.error('Произошла ошибка при получении данных', error)
            })
        }
        fetchData()
    }, [])
    
    const [modal, setModal] = useState(false)
    const [trashFiles, setTrashFiles] = useState([])
    const modalOpen = () => {
        setModal(!modal)
        setProfile(false)
        axios.post('http://79.137.204.172/api/storage/get-trash/', null, {headers: {"Authorization": `Bearer ${token}`}})
        .then(response => {
            const files = response.data.map(file => (
                {
                    id: file.id,
                    name: file.name,
                    size: formatFileSize(file.size)
                }
                ))
            setTrashFiles(files)
        })
        .catch(error => {
            console.error('Произошла ошибка при получении удаленных файлов ', error)
        })
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
                <Header changeTheme={changeTheme} modalOpen={modalOpen} profileClick={profileClick} profilePhoto={profilePhoto} setFile={setFiles} />
                <main>
                    {modal && <Modal trashFiles={trashFiles} setTrashFiles={setTrashFiles} setFiles={setFiles} formatFileSize={formatFileSize}/>}
                    {profile && <Profile profilePhoto={profilePhoto} profileEmail={profileEmail} setProfileEmail={setProfileEmail} setProfilePhoto={setProfilePhoto}/>}
                    {files.length ? (
                        files.map(file => <FileItem key={file.id} file={file} setFiles={setFiles} setTrashFiles={setTrashFiles}/>)
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