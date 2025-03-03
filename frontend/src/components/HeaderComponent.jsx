import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="header p-4 flex items-center justify-between">
      <div className="flex items-center space-x-3">
        <img src="/vite.svg" alt="Vittaly Logo" className="w-8 h-8" />
        <h1 className="text-xl font-bold">Vittaly</h1>
      </div>
      <nav>
        <ul className="flex space-x-4">
          <li>
            <Link to="/" className="hover:underline">
              Dashboard
            </Link>
          </li>
          <li>
            <Link to="/settings" className="hover:underline">
              Settings
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
