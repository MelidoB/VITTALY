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
              className="w-full bg-red-600 hover:bg-red-700 transition duration-200 rounded-md text-white py-2"
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
    <div className="min-h-screen bg-background text-primary w-full">
      <Header />
      <div className="flex flex-col md:flex-row max-w-screen-xl mx-auto">
        {/* Sidebar Navigation */}
        <div className="md:w-80 w-full bg-card p-4 border-b md:border-r md:border-b-0">
          <h2 className="text-xl font-bold mb-4">Settings</h2>
          <ul className="space-y-2">
            {['profile', 'security', 'notifications', 'privacy', 'dietary', 'app', 'support', 'logout'].map(
              (section) => (
                <li key={section}>
                  <button
                    onClick={() => setActiveSection(section)}
                    className={`w-full text-left p-2 rounded ${
                      activeSection === section
                        ? 'bg-accent text-white'
                        : 'hover:bg-hover-bg'
                    }`}
                  >
                    {section.charAt(0).toUpperCase() + section.slice(1)}
                  </button>
                </li>
              )
            )}
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
