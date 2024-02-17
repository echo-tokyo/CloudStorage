import './modal.css'
import FileItem from '../fileItem/FileItem'

function Modal ({trashFiles, setTrashFiles}) {
    const trashRemove = () => {
        setTrashFiles('')
    }
    
    return(
        <div className="modal-window">
            <div className="titles">
                <p>Корзина</p>
                <p className='subtitle' onClick={()=> trashRemove()}>Очистить</p>
            </div>
            <div className="files">
                {trashFiles.length ? (
                    trashFiles.map(file => <FileItem key={file.id} file={file} setFile={setTrashFiles}/>)
                        ) : (
                    <p>There are no files</p>
                )}
            </div>
        </div>
    )
}

export default Modal