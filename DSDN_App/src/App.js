import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import './App.css';
import LoginScreen from './Login';
import NodeAdder from './users/AddNodes';
import Dashboard from './users/Dashboard';
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
