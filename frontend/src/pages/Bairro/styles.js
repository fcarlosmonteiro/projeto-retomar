import styled from 'styled-components';
import { shade } from 'polished';

export const AnimationContainer = styled.div`
  animation: slideUp 1s cubic-bezier(0.25, 0.84, 0.83, 0.87);

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

export const BlockItems = styled.div`
  div {
    display: flex;

    span,
    strong {
      font-size: 20px;
    }

    .circle {
      color: #fff;
      font-size: 40px;
      margin-right: 15px;
    }
  }

  div:first-child {
    align-items: center;
  }

  div + div {
    animation: slideDown 0.3s cubic-bezier(0.25, 0.84, 0.83, 0.87);
    display: flex;
    align-items: center;
    margin-top: 10px;

    div {
      display: flex;
      flex-direction: column;
    }

    .circle-green {
      color: #2dff73;
      font-size: 35px;
      margin-right: 20px;
    }

    a {
      font-size: 15px;
      display: flex;
      align-items: center;
      text-decoration: none;
      color: #fff;
      transition: color 0.2s;

      &:hover {
        color: #999;
      }
    }
  }

  @keyframes slideDown {
    from {
      transform: translateY(20px);
    }

    to {
      transform: translateY(0);
    }
  }
`;

export const Title = styled.h1`
  font-size: 32px;
  margin-top: 35px;
  animation: slideDown 0.3s cubic-bezier(0.25, 0.84, 0.83, 0.87);

  @keyframes slideDown {
    from {
      transform: translateY(20px);
    }

    to {
      transform: translateY(0);
    }
  }
`;

export const Error = styled.span`
  display: block;
  color: #c53030;
  margin-top: 8px;
`;

export const ContainerAutocomplete = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
`;

export const Button = styled.button`
  width: 100%;
  height: 60px;
  background: #00c677;
  border-radius: 5px;
  border: 0;
  color: #fff;
  margin-top: 30px;
  font-weight: bold;
  transition: background-color 0.2s;

  &:hover {
    background: ${shade(0.2, '#00C677')};
  }
`;

export const LinkVoltar = styled.div`
  margin-top: 10px;

  a {
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    color: #fff;
    transition: color 0.2s;

    &:hover {
      color: #adadad;
    }
  }
`;
