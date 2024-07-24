import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomeScreen from './screens/HomeScreen';
import NewsScreen from './screens/NewsScreen';
import AboutScreen from './screens/AboutScreen';
import ToolsScreen from './screens/ToolsScreen';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={HomeScreen} />
        <Route path="/news" component={NewsScreen} />
        <Route path="/about" component={AboutScreen} />
        <Route path="/tools" component={ToolsScreen} />
      </Switch>
    </Router>
  );
}

export default App;
