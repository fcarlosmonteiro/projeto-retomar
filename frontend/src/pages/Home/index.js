import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import { ThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import { Grid, Col, Row } from 'react-styled-flexboxgrid';

import Centered from '../../components/Centered';
import {
  ContainerAutocomplete,
  Header,
  BlockItems,
  Title,
  Error,
  Button,
} from './styles';

import Logo from '../../images/retomar-svg.svg';

const darkTheme = createMuiTheme({
  overrides: {
    MuiFormLabel: {
      focused: true,
      root: {
        '&$focused': {
          color: '#00c677',
          borderBottom: '#00c677',
        },
      },
    },
    MuiInput: {
      underline: {
        '&$focused': {
          borderBottom: '1px solid #00c677',
        },
      },
    },
  },
  palette: {
    type: 'dark',
  },
});

function Home() {
  const [cidade, setCidade] = useState('');
  const [inputError, setInputError] = useState('');
  const history = useHistory();

  const cidadesEscalonadas = [
    { 
      idEstado: 1,
      idCidade: 1, 
      dsCidade: 'Dois Vizinhos, PR, Brasil ',
      listBairro:[
        { id: 1, dsBairro: 'Centro'}
      ] 
    },
    { 
      idEstado: 2,
      idCidade: 2,
      dsCidade: 'San Andrés, SC, Colômbia',
      listBairro:[
        { id: 1, dsBairro: 'Playa Spratt Bight'}
      ] 
    },
    { 
      idEstado: 3,
      idCidade: 3,
      dsCidade: 'Rio de Janeiro, RJ, Brasil',
      listBairro:[
        { id: 1, dsBairro: 'Catete'}
      ] 
    }
  ];

  function handleSelecionaCidade(event) {
    event.preventDefault();

    if (!cidade) {
      setInputError('Informe a cidade desejada');
    } else {
      setInputError('');
      history.push('/bairro', {cidade:cidade});
    }
  }

  return (
    <>
      <Grid>
        <Row>
          <Col xs={12}>
            <Header>
              <img src={Logo} width="150" alt="Projeto Retomar" />
            </Header>
          </Col>
        </Row>
      </Grid>

      <Grid>
        <Row>
          <Col xs={12}>
            <BlockItems>
              <div>
                <span className="circle">•</span>
                <span>
                  Confira o <strong>horário de funcionamento</strong> dos estabelecimentos da sua
                  cidade
                </span>
              </div>
            </BlockItems>
          </Col>
        </Row>
      </Grid>

      <Grid>
        <Row center="xs">
          <Col xs={12} sm={12} md={7} lg={7}>
            <Centered column>
              <Title>Qual sua cidade?</Title>
            </Centered>

            <ContainerAutocomplete>
              <ThemeProvider theme={darkTheme}>
                <Autocomplete
                  options={cidadesEscalonadas}
                  getOptionLabel={option => option.dsCidade}
                  style={{ width: 400 }}
                  id="cidade"
                  autoHighlight
                  value={cidade}
                  onChange={(event, newValue) => {
                    setCidade(newValue);
                  }}
                  renderInput={params => (
                    <TextField
                      {...params}
                      label="Digite sua cidade"
                      margin="normal"
                    />
                  )}
                />
              </ThemeProvider>
            </ContainerAutocomplete>
          </Col>
        </Row>

        <Row center="xs">
          <Col xs={12} sm={6} md={3} lg={3}>
            <Centered column>
              {inputError && <Error>{inputError}</Error>}

              <Button onClick={handleSelecionaCidade}>Próximo</Button>
            </Centered>
          </Col>
        </Row>
      </Grid>
    </>
  );
}

export default Home;
