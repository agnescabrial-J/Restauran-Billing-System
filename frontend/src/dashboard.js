import React, { useEffect, useState } from "react";
import API from "./services/api";

function Dashboard() {
  const [tables, setTables] = useState([]);

  useEffect(() => {
    API.get("tables/").then((res) => setTables(res.data));
  }, []);

  return (
    <div>
      <h2>Live Table Dashboard</h2>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>No</th>
            <th>Capacity</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {tables.map((t) => (
            <tr key={t.id}>
              <td>{t.number}</td>
              <td>{t.capacity}</td>
              <td>{t.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;