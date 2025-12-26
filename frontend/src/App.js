import React, { useState } from "react";
import Login from "./login";
import Dashboard from "./dashboard";
import Orders from "./orders";
import Billing from "./billing";

function App() {
  const [loggedIn, setLoggedIn] = useState(!!localStorage.getItem("token"));

  if (!loggedIn) return <Login onLogin={() => setLoggedIn(true)} />;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Restaurant Live Table System</h1>
      <Dashboard />
      <Orders />
      <Billing />
    </div>
  );
}

export default App;