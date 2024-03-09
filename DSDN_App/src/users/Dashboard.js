import React, { useState, useEffect } from "react";
import axios from "axios";
import Footer from "../layout//Footer";
import Header2 from "../layout/Header2";
import useAuth from "../hooks/useAuth";
import MenuBar from "../layout/MenuBar";



const Dashboard = () => {
  const isAuthenticated = useAuth();
  const [user, setUser] = useState(null);



  useEffect(() => {
    const storedUser = JSON.parse(localStorage.getItem("user"));
    if (storedUser) {
      setUser(storedUser);
    }
    console.log(user)
    // if(![user.privileges.accessDashboard]){
    //   return <Subscription />;
    // }
  }, []);


  if (!isAuthenticated) {
    return null;
  }

  return (
    <div>
      <Header2 user={user} />
      <div className="d-content page-view">
        <div className="dashboard">
          <MenuBar />
          <div className="dashboard-content">
          <table className="stats-table">
              <tr>
                <th className="header-cell" colSpan={4}>Dashboard Analytics</th>
              </tr>
              <tr>
                <td className="category-heading" colSpan="1">
                  Total 
                </td>
                <td className="category-heading" colSpan="1">
                  Total
                </td>
                <td className="category-heading" colSpan="1">
                  Total 
                </td>
                <td className="category-heading" colSpan="1">
                  Total 
                </td>
              </tr>
              <tr>
                <td className="data-cell" colSpan="1">
                 
                </td>
                <td className="data-cell" colSpan="1">
                                
                </td>
                <td className="data-cell" colSpan="1">
                                 
                </td>
                <td className="data-cell" colSpan="1">
                                   
                </td>
              </tr>
            </table>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Dashboard;
