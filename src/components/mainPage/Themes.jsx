import { useEffect, useState } from 'react';
import { createGlobalStyle } from 'styled-components';

function Themes({ defaultTheme, children }) {
    const [isClicked, setIsClicked] = useState(() => {
        const savedTheme = localStorage.getItem('isBlackTheme');
        return savedTheme ? savedTheme === 'true' : defaultTheme; // используем сохраненное значение, если оно существует
    })
    const changeTheme = () => {
        setIsClicked(!isClicked);
    }

    const GlobalStyles = createGlobalStyle`
    body{ 
        background-color: ${props => (props.isClicked ? '#2B2B2B' : 'white')};
    }
    p,a,label,h1{
        color: ${props => (props.isClicked ? 'white' : 'black')};
    }
    .theme1, .theme2, .theme5{
        stroke:  ${props => (props.isClicked ? 'white' : 'black')};
    }
    .theme3, .theme4{
        fill: ${props => (props.isClicked ? 'white' : 'black')};
    }
    main{
        background-color: ${props => (props.isClicked ? '#383838' : '#DFDFDF')};
    }
    .file-item{
        border-color: ${props => (props.isClicked ? 'white' : 'black')};
    }
    .form-field{
        background-color: ${props => (props.isClicked ? '#383838' : '#DFDFDF')};
    }
    input[type="email"],[type="password"]{
        background-color: ${props => (props.isClicked ? '#484848' : '#B4B4B4')};
        color: ${props => (props.isClicked ? 'white' : 'black')};
    }
    input::placeholder{
        color: ${props => (props.isClicked ? 'white' : 'black')};
    }
    input[type="submit"]{
        background-color: ${props => (props.isClicked ? '#484848' : '#B4B4B4')};
        color: ${props => (props.isClicked ? 'white' : 'black')};
    }
    `

    useEffect(() => {
        localStorage.setItem('isBlackTheme', isClicked);
    }, [isClicked])

    return (
        <>
        <GlobalStyles isClicked={isClicked} />
        {children(changeTheme)}
        </>
    )
}

export default Themes