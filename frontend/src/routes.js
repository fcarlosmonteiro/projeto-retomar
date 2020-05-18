import React from 'react';
import { Switch, Route } from 'react-router-dom';

import Home from 'pages/Home';
import Bairro from 'pages/Bairro';
import Horarios from 'pages/Horarios';

function Routes() {
  return (
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/bairro" component={Bairro} />
      <Route path="/horarios" component={Horarios} />
    </Switch>
  );
}

export default Routes;
