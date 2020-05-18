import styled from 'styled-components';

export const AnimationContainer = styled.div`
  animation: slideUp 0.6s cubic-bezier(0.31, 0.77, 0.78, 0.95);

  @keyframes slideUp {
    from {
      transform: translateY(200px);
    }

    to {
      transform: translateY(0);
    }
  }
`;

export const Header = styled.div`
  display: flex;
  padding: 20px 0;
  height: 100px;

  @media (max-width: 770px) {
    & {
      justify-content: center;
    }
  }
`;

export const ItemGuia = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 15px;

  div {
    display: flex;
    flex-direction: column;

    span,
    strong {
      font-size: 18px;
    }
  }

  .circle-green {
    color: #2dff73;
    font-size: 50px;
    margin-right: 15px;
  }

  a {
    font-size: 15px;
    display: flex;
    align-items: center;
    text-decoration: none;
    color: #fff;
    transition: color 0.2s;

    &:hover {
      color: #adadad;
    }
  }
`;

export const TitleCategoria = styled.h3`
  margin-top: 40px;
`;

export const EstabelecimentosList = styled.div`
  margin-top: 40px;

  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
`;

export const Estabelecimentos = styled.div`
  display: flex;

  flex: 1;
  min-height: 225px;
  margin: 10px 0;
  background: #fff;
  border-radius: 10px;
  min-height: 17em;

  .iconeCategoria {
    padding: 20px;
  }

  .estabelecimento {
    padding: 15px;
    flex: 1;

    strong {
      font-size: 1.5em;
      color: #313131;
    }

    p {
      font-size: 1em;
      color: #313131;
      margin-top: 4px;
    }

    .funcionamento {
      margin-top: 20px;

      .titleFuncionamento {
        color: #4A4A4A;
      }

      p {
        color: #313131;
      }

      div {
        margin-top: 5px;
      }

      span {
        font-size: 14px;
        color: #05a200;
        font-weight: bold;
      }
    }
  }
`;
