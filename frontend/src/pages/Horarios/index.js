import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import { ThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import Avatar from '@material-ui/core/Avatar';
import StoreIcon from '@material-ui/icons/Store';
import { Grid, Col, Row } from 'react-styled-flexboxgrid';

import {
  AnimationContainer,
  Header,
  ItemGuia,
  TitleCategoria,
  EstabelecimentosList,
  Estabelecimentos,
} from './styles';

import Logo from '../../images/retomar-svg.svg';
import scheduleJSON from '../../schedule/schedule.json';

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

function Horarios() {
  const [categoria, setCategoria] = useState('');

  const categoriasEstabelecimentos = [
    {
      idCategoria: 1,
      dsCategoria: 'Essenciais',
      correspondingTypes: [
        'atm',
        'bank',
        'hospital',
        'pharmacy',
        'supermarket',
      ],
    },
    {
      idCategoria: 2,
      dsCategoria: 'Saúde',
      correspondingTypes: [
        'physiotherapist',
        'hospital',
        'doctor',
        'dentist',
        'drugstore',
        'pharmacy',
      ],
    },
    {
      idCategoria: 3,
      dsCategoria: 'Alimentação',
      correspondingTypes: [
        'supermarket',
        'restaurant',
        'meal_takeaway',
        'meal_delivery',
        'bakery',
        'bar',
        'cafe',
      ],
    },
    {
      idCategoria: 4,
      dsCategoria: 'Entretenimento',
      correspondingTypes: [
        'zoo',
        'tourist_attraction',
        'stadium',
        'rv_park',
        'park',
        'night_club',
        'museum',
        'movie_theater',
        'movie_rental',
        'library',
        'casino',
        'campground',
        'bowling_alley',
        'bar',
        'amusement_park',
        'aquarium',
        'art_gallery',
      ],
    },
    {
      idCategoria: 5,
      dsCategoria: 'Beleza e Corpo',
      correspondingTypes: ['hair_care', 'spa', 'gym', 'beauty_salon'],
    },
    {
      idCategoria: 6,
      dsCategoria: 'Loja',
      correspondingTypes: [
        'store',
        'pet_store',
        'shopping_mall',
        'shoe_store',
        'liquor_store',
        'jewelry_store',
        'home_goods_store',
        'hardware_store',
        'furniture_store',
        'gas_station',
        'florist',
        'electronics_store',
        'department_store',
        'convenience_store',
        'clothing_store',
        'car_dealer',
        'book_store',
        'bicycle_store',
      ],
    },
    {
      idCategoria: 7,
      dsCategoria: 'Serviços',
      correspondingTypes: [
        'veterinary_care',
        'university',
        'travel_agency',
        'transit_station',
        'storage',
        'school',
        'secondary_school',
        'roofing_contractor',
        'real_estate_agency',
        'primary_school',
        'post_office',
        'police',
        'plumber',
        'parking',
        'painter',
        'moving_company',
        'movie_rental',
        'atm',
        'bank',
        'lodging',
        'locksmith',
        'local_government_office',
        'lawyer',
        'laundry',
        'insurance_agency',
        'funeral_home',
        'fire_station',
        'embassy',
        'electrician',
        'courthouse',
        'city_hall',
        'cemetery',
        'accounting',
        'car_rental',
        'car_repair',
        'car_wash',
      ],
    },
    {
      idCategoria: 8,
      dsCategoria: 'Religioso',
      correspondingTypes: ['synagogue', 'church', 'hindu_temple', 'mosque'],
    },
    {
      idCategoria: 9,
      dsCategoria: 'Transporte',
      correspondingTypes: [
        'train_station',
        'taxi_stand',
        'subway_station',
        'light_rail_station',
        'airport',
        'bus_station',
      ],
    },
  ];

  function handleSelecionaCategoria(newValue) {
    setCategoria(newValue);
    // Iterar JSON filtrando categoria
  }

  function formatStoreName(storeName) {
    return storeName
      .toLowerCase()
      .split(' ')
      .map(
        storeNames => storeNames.charAt(0).toUpperCase() + storeNames.slice(1),
      )
      .join(' ');
  }

  function translateCategorias(types) {
    const categorias = [];

    categoriasEstabelecimentos.map(categoriaActual => {
      categoriaActual.correspondingTypes.map(correspondingType => {
        if (
          types.includes(correspondingType) &&
          !categorias.includes(categoriaActual)
        ) {
          categorias.push(categoriaActual);
          return categorias;
        }
        return categorias;
      });
      return categorias;
    });

    return categorias;
  }

  function formatDaysSchedule(store, turno) {
    const openDays = [];

    store.map(scheduleDay => {
      if (scheduleDay.monday[turno] === 1) {
        openDays.push('Segunda-feira');
      }
      if (scheduleDay.tuesday[turno] === 1) {
        openDays.push('terça-feira');
      }
      if (scheduleDay.wednesday[turno] === 1) {
        openDays.push('quarta-feira');
      }
      if (scheduleDay.thursday[turno] === 1) {
        openDays.push('quinta-feira');
      }
      if (scheduleDay.friday[turno] === 1) {
        openDays.push('sexta-feira');
      }
      return openDays;
    });
    let strDays = '';

    if (openDays.length === 5) {
      return 'Todos os dias';
    }
    if (openDays.length > 1) {
      openDays[openDays.length - 1] = `e ${openDays[openDays.length - 1]}`;
    }
    if (openDays.length === 2) {
      strDays = `${openDays[0]} ${openDays[1]}`;
      return strDays.charAt(0).toUpperCase() + strDays.slice(1);
    }
    openDays.map((d, index) => {
      strDays += index !== openDays.length - 1 ? `${d}, ` : d;
      return strDays;
    });
    return strDays.charAt(0).toUpperCase() + strDays.slice(1);
  }

  function buildEstabelecimentosList() {
    return scheduleJSON.map(store => {
      const categoriasStore = translateCategorias(store.types);
      const categoriasText = categoriasStore.map((m, index) =>
        categoriasStore.length - 1 !== index
          ? `${m.dsCategoria}, `
          : m.dsCategoria,
      );
      let inFilter = false;
      if (categoria === undefined || categoria === null || categoria === '') {
        inFilter = true;
      } else {
        categoriasStore.map(cat => {
          if (cat.idCategoria === categoria.idCategoria) {
            inFilter = true;
            return true;
          }
          return false;
        });
      }
      const manha = formatDaysSchedule(store.schedule, 0);
      const tarde = formatDaysSchedule(store.schedule, 1);
      if (inFilter) {
        return (
          <Col xs={12} md={6}>
            <Estabelecimentos key={store.storeId}>
              <div className="iconeCategoria">
                <Avatar>
                  <StoreIcon />
                </Avatar>
              </div>
              <div className="estabelecimento">
                <strong>{formatStoreName(store.store)}</strong>
                <p>{store.vicinity}</p>
                <p>{categoriasText}</p>
                <div className="funcionamento">
                  <p className="titleFuncionamento">HORÁRIO DE FUNCIONAMENTO</p>
                  {manha && (
                    <div>
                      <p>{manha}:</p>
                      <span>das 8:00 às 12:00</span>
                    </div>
                  )}
                  {tarde && (
                    <div>
                      <p>{tarde}:</p>
                      <span>das 13:30 às 18:00</span>
                    </div>
                  )}
                </div>
              </div>
            </Estabelecimentos>
          </Col>
        );
      }
      return <div />;
    });
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

      <AnimationContainer>
        <Grid>
          <Row>
            <Col xs={12} sm={4} lg={2}>
              <ItemGuia>
                <span className="circle-green">•</span>
                <div>
                  <strong>Rio de Janeiro</strong>
                  <Link to="/">Alterar cidade</Link>
                </div>
              </ItemGuia>
            </Col>

            <Col xs={12} sm={4} lg={2}>
              <ItemGuia>
                <span className="circle-green">•</span>
                <div>
                  <strong>Bairro Catete</strong>
                  <Link to="/bairro">Alterar bairro</Link>
                </div>
              </ItemGuia>
            </Col>
          </Row>

          <Row>
            <Col xs={12}>
              <TitleCategoria>Filtre por uma categoria:</TitleCategoria>
            </Col>
          </Row>
          <Row>
            <Col xs={12}>
              <ThemeProvider theme={darkTheme}>
                <Autocomplete
                  options={categoriasEstabelecimentos}
                  getOptionLabel={option => option.dsCategoria}
                  getOptionSelected={option => option.dsCategoria}
                  style={{ width: 300 }}
                  id="cidade"
                  debug
                  onChange={(event, newValue) => {
                    handleSelecionaCategoria(newValue);
                  }}
                  renderInput={params => (
                    <TextField {...params} label="Categoria" margin="normal" />
                  )}
                />
              </ThemeProvider>
            </Col>
          </Row>
          <Row>
            <EstabelecimentosList>
              {buildEstabelecimentosList()}
            </EstabelecimentosList>
          </Row>
        </Grid>
      </AnimationContainer>
    </>
  );
}

export default Horarios;
