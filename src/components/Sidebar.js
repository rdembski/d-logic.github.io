import React from 'react';
import { Link } from 'react-router-dom';

function Sidebar() {
  return (
    <div className="sidebar">
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/news">News</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/tools">Tools</Link></li>
      </ul>
    </div>
  );
}

export default Sidebar;
