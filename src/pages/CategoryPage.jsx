import React from 'react';
import { useNavigate } from 'react-router-dom';
import './CategoryPage.css'; // 等下也會寫CSS

function CategoryPage() {
  const navigate = useNavigate();

  const handleLogout = () => {
    navigate('/');
  };

  return (
    <div className="category-container">
      <div className="header">
        <h1>NoteGenius</h1>
        <button className="logout-btn" onClick={handleLogout}>log out</button>
      </div>
      <h2 className="welcome-text">welcome back</h2>

      <div className="note-grid">
        {/* 這裡是筆記列表的範例，未來可以做成動態 */}
        <div className="note-item">New</div>
        <div className="note-item">Category</div>
        <div className="note-item">Note 1</div>
        <div className="note-item">Note 2</div>
        <div className="note-item">Note 3</div>
        <div className="note-item">Note 4</div>
      </div>
    </div>
  );
}

export default CategoryPage;
