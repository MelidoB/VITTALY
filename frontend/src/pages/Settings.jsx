import React, { useState } from 'react';
import Header from "../components/HeaderComponent";

const Settings = () => {
  const [activeSection, setActiveSection] = useState('profile');

  const renderContent = () => {
    switch (activeSection) {
      case 'profile':
        return (
          <div>
            <h2 className="text-2xl font-bold mb-4">Profile</h2>
            <p>Manage your basic personal information such as name, email, and profile picture.</p>
          </div>
        );
      case 'security':
        return (
          <div>
            <h2 className="text-2xl font-bold mb-4">Account Security</h2>
            <p>Change your password and manage security settings like two-factor authentication.</p>
          </div>
        );
      case 'notifications':
        return (
          <div>
            <h2 className="text-2xl font-bold mb-4">Notification Preferences</h2>
            <p>Toggle push notifications, email alerts, and SMS reminders for meal logging and updates.</p>
          </div>
        );
      case 'privacy':
        return (
          <div>
            <h2 className="text-2xl font-bold mb-4">Privacy Settings</h2>
            <p>Control your profile visibility and data sharing options.</p>
          </div>
        );
      case 'dietary':
        return (
          <div>
            <h2 className="text-2xl font-bold mb-4">Dietary Preferences</h2>
            <p>Select your dietary options like vegetarian, vegan, gluten-free, etc.</p>
          </div>
        );
      case 'app':
        return (
          <div>
            <h2 className="text-2xl font-bold mb-4">App Preferences</h2>
            <p>Customize language, theme, and font size for a personalized experience.</p>
          </div>
        );
      case 'support':
        return (
          <div>
            <h2 className="text-2xl font-bold mb-4">Help & Support</h2>
            <p>Find FAQs or contact support if you need assistance.</p>
          </div>
        );
      case 'logout':
        return (
          <div>
            <h2 className="text-2xl font-bold mb-4">Log Out</h2>
            <p>Click below to log out of your account.</p>
            <button 
              className="w-full bg-red-600 text-white py-2 rounded-md hover:bg-red-700 transition duration-200"
              onClick={() => alert('Logging out...')}
            >
              Confirm Logout
            </button>
          </div>
        );
      default:
        return <div>Select a section from the menu.</div>;
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 w-full text-gray-900">
      <Header />
      <div className="flex flex-col md:flex-row max-w-screen-xl mx-auto">
        {/* Sidebar Navigation */}
        <div className="md:w-80 w-full bg-gray-100 p-4 border-b md:border-r md:border-b-0">
          <h2 className="text-xl font-bold mb-4 text-gray-900">Settings</h2>
          <ul className="space-y-2">
            <li>
              <button
                onClick={() => setActiveSection('profile')}
                className={`w-full text-left p-2 rounded ${
                  activeSection === 'profile'
                    ? 'bg-blue-600 text-white'
                    : 'hover:bg-gray-200 text-gray-900'
                }`}
              >
                Profile
              </button>
            </li>
            <li>
              <button
                onClick={() => setActiveSection('security')}
                className={`w-full text-left p-2 rounded ${
                  activeSection === 'security'
                    ? 'bg-blue-600 text-white'
                    : 'hover:bg-gray-200 text-gray-900'
                }`}
              >
                Account Security
              </button>
            </li>
            <li>
              <button
                onClick={() => setActiveSection('notifications')}
                className={`w-full text-left p-2 rounded ${
                  activeSection === 'notifications'
                    ? 'bg-blue-600 text-white'
                    : 'hover:bg-gray-200 text-gray-900'
                }`}
              >
                Notifications
              </button>
            </li>
            <li>
              <button
                onClick={() => setActiveSection('privacy')}
                className={`w-full text-left p-2 rounded ${
                  activeSection === 'privacy'
                    ? 'bg-blue-600 text-white'
                    : 'hover:bg-gray-200 text-gray-900'
                }`}
              >
                Privacy
              </button>
            </li>
            <li>
              <button
                onClick={() => setActiveSection('dietary')}
                className={`w-full text-left p-2 rounded ${
                  activeSection === 'dietary'
                    ? 'bg-blue-600 text-white'
                    : 'hover:bg-gray-200 text-gray-900'
                }`}
              >
                Dietary Preferences
              </button>
            </li>
            <li>
              <button
                onClick={() => setActiveSection('app')}
                className={`w-full text-left p-2 rounded ${
                  activeSection === 'app'
                    ? 'bg-blue-600 text-white'
                    : 'hover:bg-gray-200 text-gray-900'
                }`}
              >
                App Preferences
              </button>
            </li>
            <li>
              <button
                onClick={() => setActiveSection('support')}
                className={`w-full text-left p-2 rounded ${
                  activeSection === 'support'
                    ? 'bg-blue-600 text-white'
                    : 'hover:bg-gray-200 text-gray-900'
                }`}
              >
                Help & Support
              </button>
            </li>
            <li>
              <button
                onClick={() => setActiveSection('logout')}
                className={`w-full text-left p-2 rounded ${
                  activeSection === 'logout'
                    ? 'bg-blue-600 text-white'
                    : 'hover:bg-gray-200 text-gray-900'
                }`}
              >
                Log Out
              </button>
            </li>
          </ul>
        </div>

        {/* Main Content Area */}
        <div className="flex-1 w-full p-6">
          {renderContent()}
        </div>
      </div>
    </div>
  );
};

export default Settings;
