import React, { useState } from "react";

function DropdownButton({ buttonText, children }) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className={`dropdown-container ${isOpen ? "open" : ""}`}>
      {isOpen && <div className="dropdown-content">{children}</div>}
      <button className="dropdown-button" onClick={() => setIsOpen(!isOpen)}>
        {buttonText} {isOpen ? "▲" : "▼"}
      </button>
    </div>
  );
}

export default DropdownButton;
