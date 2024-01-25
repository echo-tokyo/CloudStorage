import './mainPage.css'
import Header from './header/Header'
import FileItem from './fileItem/FileItem'
import filesData from './file.data'
import { useState } from 'react'
import Themes from './Themes'
import Modal from './modal/Modal'

function MainPage(){
    const [files, setFile] = useState(filesData)

    const [modal, setModal] = useState(false)
    const modalOpen = () => {
        setModal(!modal)
    }
    
    return(
        <Themes defaultTheme={false}>
            {(changeTheme) => (
                <>
                <Header changeTheme={changeTheme} modalOpen={modalOpen}/>
                <main>
                    {modal && <Modal/>}
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