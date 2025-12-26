import React, { useState } from "react";
import API from "./services/api";

function Orders() {
  const [tableId, setTableId] = useState("");

  const createOrder = async () => {
    await API.post("orders/create/", { table_id: tableId });
    alert("Order Created");
  };

  return (
    <div>
      <h2>Create Order</h2>
      <input placeholder="Table ID" onChange={(e) => setTableId(e.target.value)} />
      <button onClick={createOrder}>Create Order</button>
    </div>
  );
}

export default Orders;