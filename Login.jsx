import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./login.css";

export default function Login() {
  const navigate = useNavigate();
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  const handleLogin = () => {
    if (!formData.username || !formData.password) {
      alert("Please enter username and password");
      return;
    }

    // dummy login
    localStorage.setItem("token", "dummyToken");
    navigate("/dashboard");
  };

  return (
    <div className="login-wrapper">
      <div className="login-card">
        <div className="icon-circle">🔒</div>

        <h1>Welcome Back</h1>
        <p className="subtitle">Sign in to Master Data Admin</p>

        {/* Username */}
        <div className="form-group">
          <label>Username</label>
          <div className="input-box">
            <span className="input-icon">👤</span>
            <input
              type="text"
              placeholder="Enter username"
              value={formData.username}
              onChange={(e) =>
                setFormData({ ...formData, username: e.target.value })
              }
            />
          </div>
        </div>

        {/* Password */}
        <div className="form-group">
          <label>Password</label>
          <div className="input-box">
            <span className="input-icon">🔑</span>
            <input
              type={showPassword ? "text" : "password"}
              placeholder="Enter password"
              value={formData.password}
              onChange={(e) =>
                setFormData({ ...formData, password: e.target.value })
              }
            />
            <span
              className="eye"
              onClick={() => setShowPassword(!showPassword)}
            >
              👁
            </span>
          </div>
        </div>

        <button className="login-btn" onClick={handleLogin}>
          Sign In
        </button>

        <div className="footer-text">
          Don&apos;t have an account?
          <span onClick={() => navigate("/register")}>
            {" "}
            Create New Account
          </span>
        </div>
      </div>
    </div>
  );
}
