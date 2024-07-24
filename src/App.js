import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import HomeScreen from './screens/HomeScreen';
import NewsScreen from './screens/NewsScreen';
import AboutScreen from './screens/AboutScreen';
import ToolsScreen from './screens/ToolsScreen';
import ChatWindow from './components/ChatWindow';

function App() {
  return (
    <Router>
      <Navbar />
      <Sidebar />
      <div className="chat-window">
        <Switch>
          <Route exact path="/" component={HomeScreen} />
          <Route path="/news" component={NewsScreen} />
          <Route path="/about" component={AboutScreen} />
          <Route path="/tools" component={ToolsScreen} />
        </Switch>
        <ChatWindow />
      </div>
    </Router>
  );
}

export default App;
