import React, { useState } from "react";
import Logo from "../components/Logo";
import LogoutButton from "../components/logout";
import Settings from "../components/Settings";
import Help from "../components/Help";
import DashHomeButton from "../components/DashHome";

const Header2 = ({ user }) => {
  const [userMenuOpen, setUserMenuOpen] = useState(false);
  const [showName, setShowName] = useState(true); // New state to control name visibility

  const toggleUserMenu = () => {
    setUserMenuOpen(!userMenuOpen);
    setShowName(true); // Show the name when the user menu is closed
  };

  const handleProfileClick = () => {
    setShowName(!showName); // Toggle the name visibility when the profile icon is clicked
  };

  return (
    <div className={`toolbar ${userMenuOpen ? "user-menu-open" : ""}`}>
      <Logo />
      <div className="buttons">
        <DashHomeButton />
        <div className="user-menu">
          <div className="profile" onClick={toggleUserMenu}>
            <i
              className={`fas fa-user-circle fa-4x profile-icon ${
                userMenuOpen ? "user-menu-open" : ""
              }`}
              onClick={handleProfileClick} // Clicking the profile icon toggles the name visibility
            ></i>
            {(
              <span
                className={`highlight-name ${
                  showName && !userMenuOpen ? "visible" : "hidden"
                }`}
              >
                Admin
              </span>
            )}
            <div
              className={`user-menu-items ${userMenuOpen ? "open" : "closed"}`}
            >
              <h3 className="user-header">Portfolio</h3>
              {(
                <div className="user-details">
                  <div className="header">
                    <label className="user-label username">Name:&nbsp;</label>
                    <span className="user-size">Admin</span>
                  </div>
                  <div className="header">
                    <label className="user-label email">Mail:&nbsp;</label>
                    <span className="user-size">a@a.com</span>
                  </div>
                </div>
              )}
              <div className="user-details-border"></div>
              <Settings />
              <Help />
              <LogoutButton />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Header2;
