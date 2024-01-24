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
        background-color: ${props => (props.isClicked && '#2B2B2B')};
    }
    p,a,label,h1{
        color: ${props => (props.isClicked && 'white')};
    }
    .theme1, .theme2, .theme5{
        stroke:  ${props => (props.isClicked && 'white')};
    }
    .theme3, .theme4{
        fill: ${props => (props.isClicked && 'white')};
    }
    main{
        background-color: ${props => (props.isClicked && '#383838')};
    }
    .file-item{
        border-color: ${props => (props.isClicked && 'white')};
    }
    .form-field{
        background-color: ${props => (props.isClicked && '#383838')};
    }
    input[type="email"],[type="password"]{
        background-color: ${props => (props.isClicked && '#484848')};
        color: ${props => (props.isClicked ? 'white' : 'black')};
    }
    input::placeholder{
        color: ${props => (props.isClicked && 'white')};
    }
    input[type="submit"]{
        background-color: ${props => (props.isClicked && '#484848')};
        color: ${props => (props.isClicked ? 'white' : 'black')};
    }
    .modal-window{
        background-color: ${props => (props.isClicked && '#515151')};
    }
    .subtitle{
        color: ${props => (props.isClicked && '#BCBCBC')};
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