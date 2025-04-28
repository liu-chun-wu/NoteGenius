import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './LoginPage.css';

function LoginPage() {
  const navigate = useNavigate();
  const [account, setAccount] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    if (account.trim() === '' || password.trim() === '') {
      alert('請輸入帳號和密碼');
      return;
    }
    navigate('/category');
  };

  return (
    <div className="login-container">
      <h1 className="title">NoteGenius</h1>
      <div className="form-group">
        <input
          type="text"
          placeholder="account name"
          className="input"
          value={account}
          onChange={(e) => setAccount(e.target.value)}
        />
        <input
          type="password"
          placeholder="password"
          className="input"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <div className="button-group">
        <button className="login-btn" onClick={handleLogin}>log in</button>
        <button className="register-btn">register</button>
      </div>
    </div>
  );
}

export default LoginPage;
