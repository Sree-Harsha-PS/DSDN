// User menu bar here.
//
import React from "react";
import { useNavigate } from "react-router-dom";

const MenuBar = () => {

  const navigate = useNavigate();


  return (
    <div className="adbar usrbar">
      <a href="/dashboard/Add-Nodes" className="menu-link">
        <div className="menu-item">
          <i className="fas fa-check-circle menu-icon"></i>
          <span className="menu-text">Add Nodes</span>
        </div>
      </a>
       <a href="/dashboard/Delete-Node" className="menu-link">
        <div className="menu-item">
          <i className="fas fa-clipboard-list menu-icon"></i>
          <span className="menu-text">Delete Node</span>
        </div>
      </a> 
      <a href="/dashboard/Node-Status" className="menu-link">
        <div className="menu-item">
          <i className="fas fa-clipboard-list menu-icon"></i>
          <span className="menu-text">Node Status</span>
        </div>
      </a> 
      {/* <a href="/dashboard/gtm-readiness-assessment" className="menu-link">
        <div className="menu-item">
          <i className="fas fa-clipboard-list menu-icon"></i>
          <span className="menu-text">GTM Readiness Assessment</span>
        </div>
      </a> */}
      {/* <a href="/dashboard/GTM-Readiness" className="menu-link">
        <div className="menu-item">
          <i className="fas fa-check-circle menu-icon"></i>
          <span className="menu-text">GTM Readiness</span>
        </div>
      </a>
      <a href="/dashboard/Bootcamp" className="menu-link">
        <div className="menu-item">
          <i className="fas fa-graduation-cap menu-icon"></i>
          <span className="menu-text">Bootcamp</span>
        </div>
      </a> */}
      {/* <a href="/dashboard/Healthcare-Domains" className="menu-link">
        <div className="menu-item">
          <i className="fas fa-medkit menu-icon"></i>
          <span className="menu-text">Purchase Products</span>
        </div>
      </a>
      <a href="/dashboard/Review-Products" className="menu-link">
        <div className="menu-item"> {/*-btm*
          <i className="fas fa-star menu-icon"></i>
          <span className="menu-text">Review Products</span>
        </div>
      </a> */}
    </div>
  );
};

export default MenuBar;
