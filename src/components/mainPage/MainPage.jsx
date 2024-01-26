import './mainPage.css'
import Header from './header/Header'
import FileItem from './fileItem/FileItem'
import filesData from './file.data'
import { useState } from 'react'
import Themes from './Themes'
import Modal from './modal/Modal'
import Profile from './profile/profile'

function MainPage(){
    const [files, setFile] = useState(filesData)

    // функция парсинга данных с сервера, и их использование в состоянии для рендеринга (можно вынести в отдельный компонент)

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
                <Header changeTheme={changeTheme} modalOpen={modalOpen} profileClick={profileClick}/>
                <main>
                    {modal && <Modal />}
                    {profile && <Profile />}
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