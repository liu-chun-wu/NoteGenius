import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LoginPage.css'; // 我們等一下也做CSS

function LoginPage() {
  const navigate = useNavigate();

  const handleLogin = () => {
    navigate('/category'); // 登入後跳到分類頁
  };

  return (
    <div className="login-container">
      <h1 className="title">NoteGenius</h1>
      <div className="form-group">
        <input type="text" placeholder="account name" className="input" />
        <input type="password" placeholder="password" className="input" />
      </div>
      <button className="login-btn" onClick={handleLogin}>
        log in
      </button>
      <button className="register-btn">
        register
      </button>
    </div>
  );
}

export default LoginPage;
