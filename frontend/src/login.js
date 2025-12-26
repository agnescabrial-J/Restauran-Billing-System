import React, { useState } from "react";
import API from "./services/api";

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    try {
      const res = await API.post("token/", { username, password });

      // ✅ STORE JWT
      localStorage.setItem("token", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);

      console.log("LOGIN TOKEN:", res.data.access);

      onLogin();
    } catch (err) {
      alert("Invalid credentials");
      console.error(err);
    }
  };

  return (
    <div style={styles.card}>
      <h2>Staff Login</h2>
      <input
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={login}>Login</button>
    </div>
  );
}

const styles = {
  card: {
    width: "300px",
    margin: "100px auto",
    padding: "20px",
    border: "1px solid #ccc",
    textAlign: "center",
  },
};

export default Login;