import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginScreen from './Login';
// import Dashboard from './users/Dashboard';

// core components


export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginScreen />} />
        {/* <Route path ="/dashboard" element={<Dashboard />} /> */}
        {/* <Redirect from="/" to="/admin/dashboard" /> */}
      </Routes>
    </Router>
  );
}





// ReactDOM.render(
//   <BrowserRouter>
//     <Switch>
//       <Route path="/admin" component={Admin} />
//       <Route path="/rtl" component={RTL} />
//       <Redirect from="/" to="/admin/dashboard" />
//     </Switch>
//   </BrowserRouter>,
//   document.getElementById("root")
// );


// function Login() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
