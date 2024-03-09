// Footer Component 
// Just have added Versioning.
//
import React from 'react';
import imgP from "../images/gtm.png";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="left-content">
          <span className="footer-text">
          <div className="image">
            <img src={imgP} alt="logoH" className="logo" />
          </div>
            <h1>&copy; 2024 DSDN</h1>
            <h3>V1.0.0</h3>
          </span>
         <br />
        </div>
        <div className="right-content">
          <span className="footer-text">
            <h2>About</h2>
          </span>
          <span className="footer-text">
            <h2>Copyright Policy</h2>
          </span>
          <span className="footer-text">
            <h2>Terms and Conditions</h2>
          </span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
