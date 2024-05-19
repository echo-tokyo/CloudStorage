import axios from 'axios'
import '../modalFile/modalFile.css'

function ModalFolder({folder, setFolders, setTrashFolders}) {
    const token = localStorage.getItem('token')
    const folderRemove = () => {
        setTrashFolders(prev => prev.filter((el) => el.id !== folder.id))
        axios.delete('https://best-edu-server.ru/api/storage/delete-folder/', {
            data: {id: folder.id},
            headers: {"Authorization": `Bearer ${token}`}
        })
        .catch(error => {
            console.error('Произошла ошибка при удалении файла ', error);
        });
    }
    
    const restoreFolder = () => {
        axios.put('https://best-edu-server.ru/api/storage/move-folder-from-trash/', {"id": folder.id}, {headers: {"Authorization": `Bearer ${token}`}})
        .then(() => {
            setTrashFolders(prev => prev.filter((el) => el.id !== folder.id))
            const newFolder = {id: folder.id, name: folder.name}
            setFolders(prevFolders => [...prevFolders, newFolder])
        })
        .catch(error => {
            console.error('Произошла ошибка при восстановлении файла ', error)
        })
    }
    
    return(
        <div className="file-item">
            <p>{folder.name}</p>
            <div className="file-item_item">
                <div className="file-item_item2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 30 30" fill="none" onClick={() => folderRemove()}>
                        <path className='theme4' d="M23.4986 21.5431C23.7839 21.8517 23.9386 22.2586 23.9305 22.6787C23.9223 23.0988 23.7518 23.4995 23.4548 23.7967C23.1578 24.0939 22.7573 24.2646 22.3372 24.2731C21.9171 24.2816 21.51 24.1271 21.2013 23.8421L14.9992 17.64L8.79706 23.8421C8.64841 24.0029 8.46881 24.132 8.26904 24.2217C8.06926 24.3114 7.85343 24.3598 7.63449 24.3641C7.41554 24.3683 7.198 24.3283 6.99489 24.2465C6.79178 24.1646 6.6073 24.0425 6.4525 23.8876C6.29771 23.7327 6.1758 23.5482 6.09407 23.345C6.01234 23.1418 5.97248 22.9243 5.97689 22.7053C5.9813 22.4864 6.02988 22.2706 6.11971 22.0709C6.20955 21.8712 6.33879 21.6917 6.4997 21.5431L12.7018 15.341L6.4997 9.14206C6.33879 8.99351 6.20955 8.814 6.11971 8.61429C6.02988 8.41458 5.9813 8.19879 5.97689 7.97984C5.97248 7.7609 6.01234 7.54333 6.09407 7.34016C6.1758 7.137 6.29771 6.95243 6.4525 6.79753C6.6073 6.64263 6.79178 6.52059 6.99489 6.43872C7.198 6.35686 7.41554 6.31685 7.63449 6.32111C7.85343 6.32536 8.06926 6.37379 8.26904 6.46349C8.46881 6.55319 8.64841 6.68231 8.79706 6.84311L14.9992 13.0436L21.2013 6.84153C21.51 6.55651 21.9171 6.40204 22.3372 6.41049C22.7573 6.41895 23.1578 6.58967 23.4548 6.88689C23.7518 7.18411 23.9223 7.58476 23.9305 8.00487C23.9386 8.42498 23.7839 8.83194 23.4986 9.14048L17.2965 15.341L23.4986 21.5431Z" fill="black"/>
                    </svg>
                    <svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg" onClick={() => restoreFolder()}>
                        <g opacity="0.9">
                            <path className='theme4' d="M4.71034 7.29169H7.29175C7.86705 7.29169 8.33341 7.75806 8.33341 8.33335C8.33341 8.90865 7.86704 9.37502 7.29175 9.37502H3.12508C1.97449 9.37502 1.04175 8.44228 1.04175 7.29169V3.12502C1.04175 2.54973 1.50812 2.08335 2.08341 2.08335C2.65871 2.08335 3.12508 2.54973 3.12508 3.12502V5.91189C4.44751 4.03002 6.31323 2.57998 8.48812 1.76701C11.1077 0.787823 13.9949 0.800456 16.6058 1.80253C19.2167 2.80459 21.371 4.72692 22.6628 7.20728C23.9546 9.68765 24.2947 12.5548 23.6189 15.2686C22.9432 17.9823 21.2984 20.3552 18.9944 21.9402C16.6903 23.5252 13.8861 24.2129 11.1102 23.8738C8.33428 23.5345 5.77823 22.1918 3.92366 20.0986C2.30027 18.2663 1.31251 15.9697 1.08993 13.5498C1.03722 12.977 1.51275 12.5092 2.08805 12.5088C2.66334 12.5082 3.12874 12.9756 3.19306 13.5474C3.40777 15.4556 4.20541 17.2611 5.48995 18.711C7.00581 20.4219 9.09506 21.5194 11.364 21.7966C13.633 22.0739 15.9251 21.5118 17.8083 20.2162C19.6916 18.9206 21.036 16.9811 21.5883 14.7629C22.1406 12.5448 21.8627 10.2013 20.8069 8.17387C19.7509 6.14649 17.9901 4.57523 15.856 3.75617C13.722 2.9371 11.362 2.92677 9.22081 3.72713C7.40641 4.40534 5.85528 5.626 4.77084 7.21074C4.75171 7.23871 4.73151 7.2657 4.71034 7.29169Z" fill="black"/>
                        </g>
                    </svg>
                </div>
            </div>
        </div>
    )
}

export default ModalFolder