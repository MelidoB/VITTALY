import React, { useState } from "react";

function DropdownButton({ buttonText, children }) {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <div className={`dropdown-container ${isOpen ? "open" : ""}`}>
            {/* Drop-down Content (Moves above button when open) */}
            {isOpen && <div className="dropdown-content">{children}</div>}

            {/* Drop-down Button */}
            <button className="dropdown-button" onClick={() => setIsOpen(!isOpen)}>
                {buttonText} {isOpen ? "▲" : "▼"}
            </button>
        </div>
    );
}

export default DropdownButton;



