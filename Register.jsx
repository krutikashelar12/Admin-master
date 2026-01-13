// src/auth/Register.jsx
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./login.css";

const REGISTER_API = "http://127.0.0.1:8000/users"; // backend endpoint

export default function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    username: "",
    password: "",
  });

  const handleRegister = async () => {
    const { full_name, email, username, password } = formData;

    if (!full_name || !email || !username || !password) {
      alert("Please fill all fields");
      return;
    }

    try {
      await axios.post(REGISTER_API, {
        full_name,
        email,
        username,
        password,
        role: "PG_ADMIN",        // 👈 IMPORTANT
        status: "ACTIVE",
      });

      alert("Account created successfully! Please login.");
      navigate("/login");
    } catch (error) {
      console.error(error.response?.data || error.message);
      alert("Error creating account");
    }
  };

  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <h1>Create Account</h1>

        <input
          type="text"
          placeholder="Full Name"
          value={formData.full_name}
          onChange={(e) =>
            setFormData({ ...formData, full_name: e.target.value })
          }
        />

        <input
          type="email"
          placeholder="Email"
          value={formData.email}
          onChange={(e) =>
            setFormData({ ...formData, email: e.target.value })
          }
        />

        <input
          type="text"
          placeholder="Username"
          value={formData.username}
          onChange={(e) =>
            setFormData({ ...formData, username: e.target.value })
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={formData.password}
          onChange={(e) =>
            setFormData({ ...formData, password: e.target.value })
          }
        />

        <button onClick={handleRegister}>Create Account</button>

        <p onClick={() => navigate("/login")} className="link-text">
          Back to Login
        </p>
      </div>
    </div>
  );
}
