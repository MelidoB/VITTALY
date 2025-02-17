import React from 'react';
import { Route, Routes } from 'react-router-dom';
import "./App.css";
import Dashboard from './pages/Dashboard';
import Settings from './pages/Settings';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </div>
  );
}

export default App;
