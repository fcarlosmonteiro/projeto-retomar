import React, { useState } from 'react';
import { Link, useHistory } from 'react-router-dom';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import { ThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import { Grid, Col, Row } from 'react-styled-flexboxgrid';

import Centered from '../../components/Centered';
import {
  Header,
  BlockItems,
  Title,
  Error,
  Button,
  LinkVoltar,
  ContainerAutocomplete,
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

function Bairro() {
  const [bairro, setBairro] = useState('');
  const [inputError, setInputError] = useState('');
  const history = useHistory();

  const bairrosEscalonados = [{ id: 1, dsBairro: 'Catete' }];

  function handleSelecionaBairro(event) {
    event.preventDefault();

    if (!bairro) {
      setInputError('Informe o bairro desejado');
    } else {
      setInputError('');
      history.push('/horarios');
    }
  }

  return (
    <>
      <Grid>
        <Row>
          <Col xs={12}>
            <Header>
              <Link to="/">
                <img src={Logo} width="150" alt="Projeto Retomar" />
              </Link>
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
              <div>
                <span className="circle-green">•</span>
                <div>
                  <strong>Rio de Janeiro</strong>
                  <Link to="/">Alterar cidade</Link>
                </div>
              </div>
            </BlockItems>
          </Col>
        </Row>
      </Grid>

      <Grid>
        <Row center="xs">
          <Col xs={12} sm={12} md={7} lg={7}>
            <Centered column>
              <Title>Qual bairro deseja pesquisar?</Title>
            </Centered>

            <ContainerAutocomplete>
              <ThemeProvider theme={darkTheme}>
                <Autocomplete
                  options={bairrosEscalonados}
                  getOptionLabel={option => option.dsBairro}
                  style={{ width: 400 }}
                  id="bairro"
                  debug
                  onChange={(event, newValue) => {
                    setBairro(newValue);
                  }}
                  renderInput={params => (
                    <TextField
                      {...params}
                      label="Digite o bairro"
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

              <Button onClick={handleSelecionaBairro}>Próximo</Button>

              <LinkVoltar>
                <Link to="/">Voltar</Link>
              </LinkVoltar>
            </Centered>
          </Col>
        </Row>
      </Grid>
    </>
  );
}

export default Bairro;
