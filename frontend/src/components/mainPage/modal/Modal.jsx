import './modal.css'
import ModalFile from './modalFile/ModalFile'
import ModalFolder from './modalFolder/ModalFolder'

function Modal ({trashFiles, setTrashFiles, setFiles, setTrashFolders, trashFolders, setFolders}) {
    const trashRemove = () => {
        setTrashFiles('')
        setTrashFolders('')
    }
    
    return(
        <div className="modal-window">
            <div className="titles">
                <p>Корзина</p>
                <p className='subtitle' onClick={()=> trashRemove()}>Очистить</p>
            </div>
            <div className="files">
                {/* {trashFiles.length ? (
                    trashFiles.map(file => <ModalFile key={file.id} file={file} setTrashFiles={setTrashFiles} setFiles={setFiles}/>)
                        ) : (
                    <p>There are no files</p>
                )} */}
                {trashFiles.length > 0 && (
                    trashFiles.map(file => <ModalFile key={file.id} file={file} setTrashFiles={setTrashFiles} setFiles={setFiles}/>)
                )}
                {trashFolders.length > 0 && (
                    trashFolders.map(folder => <ModalFolder key={folder.id} folder={folder} setTrashFolders={setTrashFiles} setFolders={setFolders}/>)
                )}
            </div>
        </div>
    )
}

export default Modal