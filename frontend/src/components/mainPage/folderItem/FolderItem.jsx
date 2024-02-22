import axios from 'axios'
import './folderItem.css'
import { useState } from 'react'

const FolderItem = ({folder, getFolderData, setFolders, setTrashFolders, setIdStorage}) => {
	const [isFolderRenaming, setIsFolderRenaming] = useState(false)
	const handleRemove = (event) => {
		event.stopPropagation()
		setFolders(prev => prev.filter((el) => el.id !== folder.id))
        const token = localStorage.getItem('token')
        axios.put('http://79.137.204.172/api/storage/move-folder-to-trash/', {"id": folder.id}, {headers: {"Authorization": `Bearer ${token}`}})
        .then(() => {
            const newFolder = {id: folder.id, name: folder.name}
            setTrashFolders(prevFolders => [...prevFolders, newFolder])
        })
        .catch(error => {
            console.error('Произошла ошибка при удалении файла ', error)
        })
	}

	const folderRename = (event) => {
		event.stopPropagation()
		setIsFolderRenaming(!isFolderRenaming)
		if(isFolderRenaming == false){
			setTimeout(() => {
				document.querySelector('.folderRename').focus()
			}, 0)
		}
	}

	const sendFolderNewName = (e) => {
		const newName = document.querySelector('.folderRename').value
		e.stopPropagation()
		setIsFolderRenaming(false)
		if(newName.length > 0 && newName !== '/'){
			axios.put('http://79.137.204.172/api/storage/rename-folder/', {id: folder.id, name: newName}, {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
			.then(response => {
				setFolders(prev => {
					const thisFolder = prev.find(el => el.id === folder.id)
					thisFolder.name = response.data.name
					return [...prev]
				})
			})
			.catch(error => {
				console.error('Произошла ошибка при переименовании ', error)
			})
		} else{
			alert('Некорректное название папки')
		}
	}

	const getFolderData2 = (folderId) => {
		setIdStorage(prev => [...prev, folderId])
		getFolderData(folderId)
	}

	return (
		<div className="file-item" style={{cursor:'pointer'}} onClick={() => getFolderData2(folder.id)}>
			{isFolderRenaming ? (
				<input onKeyDown={e => e.key === 'Enter' && sendFolderNewName(e)} className='folderRename' name='rename' type="text" placeholder='Введите имя папки...' onClick={e => e.stopPropagation()}/>
			) : (
				<p>{folder.name}</p>
			)}
			<div className="file-item_item">
				<div className="file-item_item2">
					{isFolderRenaming && (
						<svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" onClick={(e)=> sendFolderNewName(e)}>
							<g clipPath="url(#clip0_20_6)"><path d="M8.44127 14.8012C8.2218 14.556 7.91445 14.4071 7.58593 14.3871C7.25741 14.367 6.93423 14.4773 6.68654 14.694C6.43885 14.9108 6.28664 15.2165 6.26296 15.5448C6.23927 15.873 6.34601 16.1974 6.56002 16.4475L10.935 21.4475C11.0497 21.5786 11.1906 21.6843 11.3485 21.7579C11.5065 21.8314 11.6781 21.871 11.8523 21.8743C12.0265 21.8776 12.1994 21.8445 12.3601 21.777C12.5207 21.7095 12.6654 21.6092 12.785 21.4825L23.41 10.2325C23.6376 9.9913 23.7601 9.66959 23.7505 9.33812C23.7408 9.00665 23.5999 8.69257 23.3588 8.46499C23.1176 8.2374 22.7959 8.11494 22.4644 8.12455C22.1329 8.13416 21.8189 8.27505 21.5913 8.51624L11.91 18.7662L8.44127 14.8012Z" fill="white"/></g><defs><clipPath id="clip0_20_6"><rect width="30" height="30" fill="white"/></clipPath></defs>
						</svg>
					)}
					<svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" onClick={(event) => folderRename(event)}>
						<path fillRule="evenodd" clipRule="evenodd" d="M20.7179 5.59477L23.0519 7.49437C23.2773 7.71395 23.4037 8.01578 23.4017 8.33041C23.3999 8.64505 23.2702 8.94539 23.0423 9.16237L21.2687 11.3224L15.2327 18.6868C15.1282 18.8099 14.9876 18.8968 14.8307 18.9352L11.7012 19.6552C11.2859 19.6723 10.9278 19.3661 10.8804 18.9532L11.0268 15.8656C11.0376 15.7079 11.1 15.5582 11.2044 15.4396L16.9799 8.40157L19.0139 5.91997C19.4091 5.38205 20.1525 5.2402 20.7179 5.59477Z" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
						<path d="M6.59995 22.4896C6.1029 22.4896 5.69995 22.8925 5.69995 23.3896C5.69995 23.8867 6.1029 24.2896 6.59995 24.2896V22.4896ZM23.04 24.2896C23.537 24.2896 23.94 23.8867 23.94 23.3896C23.94 22.8925 23.537 22.4896 23.04 22.4896V24.2896ZM17.8146 8.06475C17.6284 7.60383 17.104 7.38099 16.6431 7.56703C16.1822 7.75308 15.9594 8.27755 16.1454 8.73847L17.8146 8.06475ZM21.4671 12.2039C21.9519 12.0944 22.2561 11.6125 22.1467 11.1277C22.0371 10.6428 21.5553 10.3386 21.0704 10.4481L21.4671 12.2039ZM6.59995 24.2896H23.04V22.4896H6.59995V24.2896ZM16.1454 8.73847C16.4246 9.43012 16.998 10.4161 17.8518 11.1754C18.7213 11.9486 19.9596 12.5445 21.4671 12.2039L21.0704 10.4481C20.2992 10.6224 19.633 10.3506 19.0479 9.83027C18.447 9.29587 18.0153 8.56231 17.8146 8.06475L16.1454 8.73847Z" fill="white"/>
					</svg>
					<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none" onClick={(event) => handleRemove(event)}>
						<path className='theme4' d="M23.4986 21.5431C23.7839 21.8517 23.9386 22.2586 23.9305 22.6787C23.9223 23.0988 23.7518 23.4995 23.4548 23.7967C23.1578 24.0939 22.7573 24.2646 22.3372 24.2731C21.9171 24.2816 21.51 24.1271 21.2013 23.8421L14.9992 17.64L8.79706 23.8421C8.64841 24.0029 8.46881 24.132 8.26904 24.2217C8.06926 24.3114 7.85343 24.3598 7.63449 24.3641C7.41554 24.3683 7.198 24.3283 6.99489 24.2465C6.79178 24.1646 6.6073 24.0425 6.4525 23.8876C6.29771 23.7327 6.1758 23.5482 6.09407 23.345C6.01234 23.1418 5.97248 22.9243 5.97689 22.7053C5.9813 22.4864 6.02988 22.2706 6.11971 22.0709C6.20955 21.8712 6.33879 21.6917 6.4997 21.5431L12.7018 15.341L6.4997 9.14206C6.33879 8.99351 6.20955 8.814 6.11971 8.61429C6.02988 8.41458 5.9813 8.19879 5.97689 7.97984C5.97248 7.7609 6.01234 7.54333 6.09407 7.34016C6.1758 7.137 6.29771 6.95243 6.4525 6.79753C6.6073 6.64263 6.79178 6.52059 6.99489 6.43872C7.198 6.35686 7.41554 6.31685 7.63449 6.32111C7.85343 6.32536 8.06926 6.37379 8.26904 6.46349C8.46881 6.55319 8.64841 6.68231 8.79706 6.84311L14.9992 13.0436L21.2013 6.84153C21.51 6.55651 21.9171 6.40204 22.3372 6.41049C22.7573 6.41895 23.1578 6.58967 23.4548 6.88689C23.7518 7.18411 23.9223 7.58476 23.9305 8.00487C23.9386 8.42498 23.7839 8.83194 23.4986 9.14048L17.2965 15.341L23.4986 21.5431Z" fill="black"/>
					</svg>
				</div>
			</div>
		</div>
	)
}

export default FolderItem