import React from 'react';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Leaderboard from './pages/Leaderboard';
import Settings from './pages/Settings';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
      </Routes>
    </Router>
  );
}

export default App;
