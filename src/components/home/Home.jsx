import HelloPage from '../helloPage/HelloPage'
import MainPage from '../mainPage/MainPage'

function Home(){
    return(
        <>
        {localStorage.getItem('registered') ? (
            <MainPage />
        ) : (
            <HelloPage />
        )}
        </>
    )
}

export default Home