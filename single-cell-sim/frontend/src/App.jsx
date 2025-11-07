import { useState } from "react";

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ 
      width: "100vw", 
      height: "100vh", 
      background: "#333",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      color: "white",
      fontSize: "24px"
    }}>
      <h1>Test Page</h1>
      <button 
        onClick={() => setCount(c => c + 1)}
        style={{
          padding: "10px 20px",
          fontSize: "20px",
          margin: "20px",
          cursor: "pointer"
        }}
      >
        Clicked {count} times
      </button>
    </div>
  );
}