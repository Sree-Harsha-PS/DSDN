import { useState } from 'react';
import style from './Login.module.css';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const LoginScreen = () => {


    const [screenWidth, setScreenWidth] = useState(window.innerWidth);
    const [screenHeight, setScreenHeight] = useState(window.innerHeight);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        // Function to update screen dimensions on resize
        const updateDimensions = () => {
            setScreenWidth(window.innerWidth);
            setScreenHeight(window.innerHeight);
        };

        // Event listener to handle resize
        window.addEventListener('resize', updateDimensions);

        // Clean up the event listener on component unmount
        return () => window.removeEventListener('resize', updateDimensions);
    }, []);

    const horizontal = () => {
        const horizontal = screenWidth / 50;

        const elements = [];

        for (let index = 0; index < horizontal; index++) {
            elements.push(<div key={index} className={`boxColor`} style={{ height: '50px', width: '50px', backgroundColor: '#1f1f1f', marginRight: '4px', display: 'inline-block' }}></div>)
        }
        return elements;

    }

    const showBoxes = () => {
        const vertical = screenHeight / 50;

        const elements = [];

        for (let index = 0; index < vertical; index++) {
            elements.push(<div key={index} className={style.boxCover}>
                {horizontal()}
            </div>)
        }
        return elements;
    }


    function resetBoxColor(element) {
        element.style.backgroundColor = "#1f1f1f";
    }


    useEffect(() => {
        // Attach hover event listener to all boxes
        const boxes = document.querySelectorAll(".boxColor");

        boxes.forEach((box) => {
            box.addEventListener("mouseover", () => {
                box.style.backgroundColor = "#00f700"; // Change color on hover
            });

            box.addEventListener("mouseout", () => {
                // Revert color back to original after a delay (e.g., 1 second)
                setTimeout(() => {
                    resetBoxColor(box);
                }, 400);
            });
        });
    }, [])

    const handleLogin = async (e) => {
        e.preventDefault();
    
        // Access the form elements by their name attributes
        // const username = e.target.elements.username.value;
        // const password = e.target.elements.password.value;
        console.log(username,password);
    
        // Perform authentication logic here (e.g., API call to backend)
        if (username === "a@a.com" && password === "123") {
            // Successful login logic (redirect, set auth token, etc.)
            console.log("Login successful");
        } else {
            // Unsuccessful login logic (show error message, clear inputs, etc.)
            console.log("Login failed");
        }

        // Check if the email and password fields are empty
    if (!username || !password) {
        console.log('Email and password are required');
        return;
      }
    
      try {
        // Make a POST request to the server to authenticate the admin
        const response = await axios.post(`http://127.0.1.1:3000/api/admin/login`, {
          username,
          password,
        });
    
        // Store the token in local storage
        localStorage.setItem('token', response.data.token);
    
        // Redirect to the appropriate dashboard
        navigate('/dashboard');
        
      } catch (error) {
        console.error('Login failed', error);
        // Clear the entered password field only if the login failed
        if (error.response && error.response.status === 401) {
          setPassword('');
        }
      }
    };
    
    


    return (
        <div className={style.fullScreen}>
            {showBoxes()}

            <div className={style.loginContainer}>
                <div className={style.loginContent}>
                    <h1 className={style.welcomeText}>Admin Login</h1>
                    <form className={style.loginForm} onSubmit={handleLogin}>
                        <input 
                            type="text" 
                            placeholder="Username" 
                            className={style.inputField}
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                             />
                        <input 
                            type="password" 
                            placeholder="Password" 
                            className={style.inputField}
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                             />
                        <button type="submit" className={style.loginButton}>Signup</button>
                    </form>
                </div>
            </div>
        </div>


    )
}
export default LoginScreen;