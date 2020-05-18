import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    outline: 0;
    box-sizing: border-box;
  }

  body {
    background: #015C91;
    -webkit-font-smoothing: antialiased;
  }

  body, input, button {
    font: 16px Lato, sans-serif;
    color: #fff;
  }

  button {
    cursor: pointer;
  }
`;

export default GlobalStyle;
