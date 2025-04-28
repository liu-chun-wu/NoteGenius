import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import CategoryPage from './pages/CategoryPage';
import EditPage from './pages/EditPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/category" element={<CategoryPage />} />
        <Route path="/edit/:noteId" element={<EditPage />} />
      </Routes>
    </Router>
  );
}

export default App;
