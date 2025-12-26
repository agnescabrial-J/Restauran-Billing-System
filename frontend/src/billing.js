import React, { useState } from "react";
import API from "./services/api";

function Billing() {
  const [tableId, setTableId] = useState("");
  const [billId, setBillId] = useState(null);

  const generateBill = async () => {
    const res = await API.post(`billing/generate/${tableId}/`);
    setBillId(res.data.bill_id);
  };

  const downloadPDF = () => {
    window.open(`http://127.0.0.1:8000/api/billing/download/${billId}/`);
  };

  return (
    <div>
      <h2>Billing</h2>
      <input placeholder="Table ID" onChange={(e) => setTableId(e.target.value)} />
      <button onClick={generateBill}>Generate Bill</button>

      {billId && <button onClick={downloadPDF}>Download PDF</button>}
    </div>
  );
}

export default Billing;