import './mainPage.css'
import Header from './header/Header'
import FileItem from './fileItem/FileItem'
import {useEffect, useState } from 'react'
import Themes from './Themes'
import Modal from './modal/Modal'
import Profile from './profile/Profile'
import axios from 'axios'
import FolderItem from '../folder/folderItem/FolderItem'

function MainPage(){
    const token = localStorage.getItem('token')
    const [activeFolder, setActiveFolder] = useState(localStorage.getItem('rootDir'))
    const [files, setFiles] = useState([])
    const [folders, setFolders] = useState([])
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
            await axios.get('http://79.137.204.172/api/user/get-profile-info/', {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
            .then(response => {
                setProfilePhoto(response.data.photo_url)
                setProfileEmail(response.data.email)
            })
            .catch((error) => {
                setProfilePhoto('../../../../public/i.webp')
                console.error('Произошла ошибка при получении данных профиля ', error)
            })
    
            await axios.get('http://79.137.204.172/api/storage/get-root-dir/', {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
            .then(response => {
                localStorage.setItem('rootDir', response.data.root_dir)
            })
            .catch(error => {
                console.error('Произошла ошибка при получении root-dir', error)
            })
    
            await axios.post('http://79.137.204.172/api/storage/get-folder-content/', {folder_id: Number(localStorage.getItem('rootDir'))}, {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
            .then(response => {
                const files = response.data.files.map(file => (
                    {
                        id: file.id,
                        name: file.name,
                        size: formatFileSize(file.size)
                    }
                ))
                const folders = response.data.folders.map(folder => (
                    {
                        id: folder.id,
                        name: folder.name,
                    }
                ))
                setFolders(folders)
                setFiles(files)
            })
            .catch(error => {
                console.error('Произошла ошибка при получении данных', error)
            })
        }
        fetchData()
    }, [])

    const getFolderData = (folderId) => {
        axios.post('http://79.137.204.172/api/storage/get-folder-content/', {folder_id: folderId}, {headers: {'Authorization': `Bearer ${token}`}})
        .then(response => {
            const files = response.data.files.map(file => (
                {
                    id: file.id,
                    name: file.name,
                    size: formatFileSize(file.size)
                }
            ))
            const folders = response.data.folders.map(folder => (
                {
                    id: folder.id,
                    name: folder.name,
                }
            ))
            setFolders(folders)
            setFiles(files)
            setActiveFolder(folderId)
        })
        .catch(error => {
            console.error('Произошла ошибка при получении данных папки', error)
        })
    }
    
    const [modal, setModal] = useState(false)
    const [trashFiles, setTrashFiles] = useState([])
    const [trashFolders, setTrashFolders] = useState([])
    const modalOpen = () => {
        setModal(!modal)
        setProfile(false)
        axios.post('http://79.137.204.172/api/storage/get-trash/', null, {headers: {"Authorization": `Bearer ${token}`}})
        .then(response => {
            const files = response.data.files.map(file => (
                {
                    id: file.id,
                    name: file.name,
                    size: formatFileSize(file.size)
                }
                ))
            const folders = response.data.folders.map(file => (
                {
                    id: file.id,
                    name: file.name,
                }
                ))
            setTrashFolders(folders)
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
                <Header changeTheme={changeTheme} modalOpen={modalOpen} profileClick={profileClick} profilePhoto={profilePhoto} setFiles={setFiles} setFolders={setFolders} folders={folders} activeFolder={activeFolder} formatFileSize={formatFileSize}/>
                <main>
                    {modal && <Modal trashFiles={trashFiles} setTrashFiles={setTrashFiles} setFiles={setFiles} formatFileSize={formatFileSize} trashFolders={trashFolders} setTrashFolders={setTrashFolders} setFolders={setFolders}/>}
                    {profile && <Profile profilePhoto={profilePhoto} profileEmail={profileEmail} setProfileEmail={setProfileEmail} setProfilePhoto={setProfilePhoto}/>}
                    {files.length > 0 && (
                        files.map(file => <FileItem key={file.id} file={file} setFiles={setFiles} setTrashFiles={setTrashFiles}/>)
                    )}
                    {folders.length > 0 && (
                        folders.map(folder => <FolderItem key={folder.id} folder={folder} setFolders={setFolders} getFolderData={getFolderData} setTrashFolders={setTrashFolders}/>)
                    )}
                </main>
                </>
            )}
        </Themes>
    )
}

export default MainPage