import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginScreen from './Login';
import Dashboard from './users/Dashboard';
import NodeAdder from './users/AddNodes';
import NodeDeleter from './users/DeleteNodes';
import NotFoundPage from './users/NotFound';
// core components


export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginScreen />} />
        <Route path ="/dashboard" element={<Dashboard />} />
        <Route path="/dashboard/Add-Nodes/*" element={<NodeAdder />} />
        <Route path="/dashboard/Delete-Node/*" element={<NodeDeleter />} />
        <Route path="*" element={<NotFoundPage />} />
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
