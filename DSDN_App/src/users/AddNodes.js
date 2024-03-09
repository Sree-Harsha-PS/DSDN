import React, { useState } from 'react';
import axios from 'axios';
import Footer from "../layout/Footer"
import AdminMenuBar from "../layout/MenuBar";
// import useAuth from "../hooks/useAuth";
import Header2 from "../layout/Header2";


const NodeAdder = () => {
  const [name, setName] = useState('');
  const [web,  setWeb] = useState('');
  const [id, setID] = useState('');
  const [status, setStatus] = useState(null);
  const [leaderIP, setLeaderIP] = useState();
  const[OTP,setOTP] = useState('');


  const fetchLeaderIP = async () => {
    let url = `http://127.0.1.1:3000/GetLeaderIPNode`;

    const params = new URLSearchParams();

    try {
      const response = await axios.post(url + params.toString());
      setLeaderIP(response.data.leaderIP);
    } catch (error) {
      console.error(error);
    }
  };

  const handleOTP = async (e) => {
    e.preventDefault();
    fetchLeaderIP();
  
    // Display an alert message asking for OTP
    const inputOTP = prompt('Please enter the OTP:');
    if (inputOTP !== null) {
      setOTP(inputOTP);
      console.log(leaderIP)
      try {
        await axios.post(`${leaderIP}/GetOTPFromAdmin`, {
          OTP: inputOTP
        });
        setOTP('');
  
        // Inform user that OTP verification is successful
        alert('OTP verification successful!');
      } catch (error) {
        console.error(error);
        console.log('Error response:', error.response);
        setStatus('failure');
        // show an error message or perform any other error handling
      }
    }
  };
  



  const handleSubmit = async (e) => {
    e.preventDefault();
    fetchLeaderIP();
    
    try {
      await axios.post(`${process.env.REACT_APP_BASE_URL}/AddNode`, {
        name,
        web,
        id,
    });

        // Call handleOTP to request OTP
      handleOTP(e);

      setName('');
      setWeb('');
      setID('');
      setStatus('success');

      // Clear the success message after 2 seconds
      setTimeout(() => {
        setStatus(null);
      }, 1000);
      
    } catch (error) {
      console.error(error);
      console.log('Error response:', error.response);
      setStatus('failure');
      // show an error message or perform any other error handling
    }
  };

  const renderDealerStatusMessage = () => {
    if (status === 'success') {
      return <div className="popup success">Node successfully registered!</div>;
    } else if (status === 'failure') {
      const errorMessage = 'Node failed to register. Please try again.';
      return (
        <div className="popup failure">
          {errorMessage}
          <br />
          <button onClick={() => setStatus(null)}>Try Again</button>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="page-view">
      <Header2 />
      <div className="d-content">
        <div className="dashboard">
          <AdminMenuBar />
          <div className="hosp-content">
            <h1>Add Nodes</h1>
            {renderDealerStatusMessage()}
            <form onSubmit={handleSubmit} className="hospital-f">
              
            <div className="form-group">
                <label htmlFor="mail">Node ID :</label>
                <input
                  type="text"
                  id="mail"
                  value={id}
                  onChange={(e) => setID(e.target.value)}
                  placeholder="Node-ID"
                  className="form-outline"
                />
              </div>
              <div className="form-group">
                <label htmlFor="role">IP Address :</label>
                <input
                  type="text"
                  id="role"
                  value={web}
                  onChange={(e) => setWeb(e.target.value)}
                  placeholder="IP Address"
                  className="form-outline"
                />
              </div>
              <div className="form-group">
                <label htmlFor="dealerName">Listed Name :</label>
                <input
                  type="text"
                  id="dealerName"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Listed Name"
                  className="form-outline"
                />
              </div>
              {/* <div className="form-group">
                <label htmlFor="phone">Contact Mobile:</label>
                <input
                  type="text"
                  id="phone"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  placeholder="Contact Mobile"
                  className="form-outline"
                />
              </div> */}
              <button type="submit" className="hsubtn login-btn">
                Submit
              </button>
              
            </form>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
  
};

export default NodeAdder;