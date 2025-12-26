import React, { useEffect, useState } from "react";
import { getTables } from "../services/api";

function Tables() {
  const [tables, setTables] = useState([]);

  useEffect(() => {
    fetchTables();
  }, []);

  const fetchTables = async () => {
    const data = await getTables();
    setTables(data);
  };

  return (
    <div>
      <h2>Live Table Dashboard</h2>

      {tables.map((table) => (
        <div
          key={table.id}
          style={{
            padding: "10px",
            margin: "5px",
            backgroundColor:
              table.status === "AVAILABLE"
                ? "lightgreen"
                : table.status === "OCCUPIED"
                ? "lightcoral"
                : "lightyellow",
          }}
        >
          Table {table.table_number} | {table.status}
        </div>
      ))}
    </div>
  );
}

export default Tables;
