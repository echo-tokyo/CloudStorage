import './modal.css'
import ModalFile from './modalFile/ModalFile'

function Modal ({trashFiles, setTrashFiles, setFiles}) {
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
                    trashFiles.map(file => <ModalFile key={file.id} file={file} setTrashFiles={setTrashFiles} setFiles={setFiles}/>)
                        ) : (
                    <p>There are no files</p>
                )}
            </div>
        </div>
    )
}

export default Modal