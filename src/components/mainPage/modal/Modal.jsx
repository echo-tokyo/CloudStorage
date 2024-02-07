import './modal.css'
import FileItem from '../fileItem/FileItem'
import { useState } from 'react'

function Modal () {
    const [files, setFile] = useState([])
    const trashRemove = () => {
        setFile('')
    }
    
    return(
        <div className="modal-window">
            <div className="titles">
                <p>Корзина</p>
                <p className='subtitle' onClick={()=> trashRemove()}>Очистить</p>
            </div>
            <div className="files">
                {files.length ? (
                    files.map(file => <FileItem key={file.id} file={file} setFile={setFile}/>)
                        ) : (
                    <p>There are no files</p>
                )}
            </div>
        </div>
    )
}

export default Modal