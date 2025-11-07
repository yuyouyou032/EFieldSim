import { useState } from "react";

export default function ControlsPanel({ onParamsChange }) {
  const [focalLength, setFocalLength] = useState(10);
  const [amplitude, setAmplitude] = useState(1.0);
  const [frequency, setFrequency] = useState(2 * Math.PI);

  function updateParams(partial = {}) {
    const params = {
      amplitude_x: amplitude,
      amplitude_y: amplitude,
      frequency,
      ...partial
    };
    onParamsChange(params);
  }


  function onAmplitudeSlide(e) {
    const v = parseFloat(e.target.value);
    setAmplitude(v);
    updateParams();
  }

  function onAmplitudeInput(e) {
    const v = parseFloat(e.target.value);
    if (Number.isNaN(v)) return;
    setAmplitude(v);
    updateParams();
  }

  function onFrequencySlide(e) {
    const v = parseFloat(e.target.value);
    setFrequency(v);
    updateParams();
  }

  function onFrequencyInput(e) {
    const v = parseFloat(e.target.value);
    if (Number.isNaN(v)) return;
    setFrequency(v);
    updateParams();
  }

  return (
    <div style={{
      position: "absolute", top: 12, left: 12, padding: 12,
      background: "rgba(0,0,0,0.5)", color: "#fff", borderRadius: 8
    }}>
      <div style={{ marginBottom: 12 }}>
        <label style={{ display: "block", marginBottom: 6 }}>focal length: {focalLength.toFixed(1)}</label>
        <input
          type="range" min="5" max="50" step="0.5"
          value={focalLength} onChange={onFocalSlide} style={{ width: "100%" }}
        />
      </div>

      <div style={{ marginBottom: 12 }}>
        <label style={{ display: "block", marginBottom: 6 }}>amplitude: {amplitude.toFixed(2)}</label>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <input
            type="range" min="0" max="2" step="0.01"
            value={amplitude} onChange={onAmplitudeSlide} style={{ flex: 1 }}
          />
          <input
            type="number" step="0.01" value={amplitude}
            onChange={onAmplitudeInput} style={{ width: 70 }}
          />
        </div>
      </div>

      <div>
        <label style={{ display: "block", marginBottom: 6 }}>frequency: {frequency.toFixed(2)}</label>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <input
            type="range" min="0.1" max="20" step="0.01"
            value={frequency} onChange={onFrequencySlide} style={{ flex: 1 }}
          />
          <input
            type="number" step="0.01" value={frequency}
            onChange={onFrequencyInput} style={{ width: 90 }}
          />
        </div>
      </div>

    </div>
  );
}