import { useState } from "react";

export default function ControlsPanel({ onParamsChange }) {
  const [focalLength, setFocalLength] = useState(10);

  function onSlide(e) {
    const v = parseFloat(e.target.value);
    setFocalLength(v);
    onParamsChange({ focal_length: v });
  }

  return (
    <div style={{
      position: "absolute", top: 12, left: 12, padding: 12,
      background: "rgba(0,0,0,0.5)", color: "#fff", borderRadius: 8
    }}>
      <label>focal length: {focalLength.toFixed(1)}</label>
      <input
        type="range" min="5" max="50" step="0.5"
        value={focalLength} onChange={onSlide} style={{ width: 220 }}
      />
    </div>
  );
}