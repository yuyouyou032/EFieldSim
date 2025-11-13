import { useState } from "react";

export default function ControlsPanel({ onParamsChange }) {
  const [phaseDiff, setPhaseDiff] = useState(Math.PI/2);
  const [amplitude_x, setAmplitude_x] = useState(1.0);
  const [amplitude_y, setAmplitude_y] = useState(1.0);
  const [frequency, setFrequency] = useState(2 * Math.PI);

  function updateParams(partial = {}) {
    const params = {
      amplitude_x,
      amplitude_y,
      frequency,
      phase_diff: 0,
      ...partial
    };
    onParamsChange(params);
  }


  // function onAmplitudeSlide(e) {
  //   const v = parseFloat(e.target.value);
  //   setAmplitude(v);
  //   updateParams();
  // }

  // function onAmplitudeInput(e) {
  //   const v = parseFloat(e.target.value);
  //   if (Number.isNaN(v)) return;
  //   setAmplitude(v);
  //   updateParams();
  // }

  function onAmplitude_xSlide(e) {
    const v = parseFloat(e.target.value);
    setAmplitude_x(v);
    updateParams();
  }

  function onAmplitude_xInput(e) {
    const v = parseFloat(e.target.value);
    if (Number.isNaN(v)) return;
    setAmplitude_x(v);
    updateParams();
  }

  function onAmplitude_ySlide(e) {
    const v = parseFloat(e.target.value);
    setAmplitude_y(v);
    updateParams();
  }

  function onAmplitude_yInput(e) {
    const v = parseFloat(e.target.value);
    if (Number.isNaN(v)) return;
    setAmplitude_y(v);
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

  function onPhaseDiffInput(e) {
    const v = parseFloat(e.target.value);
    if (Number.isNaN(v)) return;
    setPhaseDiff(v);
    updateParams({ phase_diff: v });
  }

  function onPhaseDiffSlide(e) {
    const v = parseFloat(e.target.value);
    setPhaseDiff(v);
    updateParams({ phase_diff: v });
  }

  return (
    <div style={{
      position: "absolute", top: 12, left: 12, padding: 12,
      background: "rgba(0,0,0,0.5)", color: "#fff", borderRadius: 8
    }}>

      <div style={{ marginBottom: 12 }}>
        <label style={{ display: "block", marginBottom: 6 }}>phase difference: {phaseDiff.toFixed(2)}</label>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
        <input
          type="range" min="-10" max="10" step="0.5"
          value={phaseDiff} onChange={onPhaseDiffSlide} style={{ width: "100%" }}
        />
        <input
            type="number" step="0.01" value={phaseDiff}
            onChange={onPhaseDiffInput} style={{ width: 70 }}
          />
        </div>
      </div>

      <div style={{ marginBottom: 12 }}>
        <label style={{ display: "block", marginBottom: 6 }}>amplitude X: {amplitude_x.toFixed(2)}</label>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <input
            type="range" min="0" max="2" step="0.01"
            value={amplitude_x} onChange={onAmplitude_xSlide} style={{ flex: 1 }}
          />
          <input
            type="number" step="0.01" value={amplitude_x}
            onChange={onAmplitude_xInput} style={{ width: 70 }}
          />
        </div>
      </div>

      <div style={{ marginBottom: 12 }}>
        <label style={{ display: "block", marginBottom: 6 }}>amplitude Y: {amplitude_y.toFixed(2)}</label>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <input
            type="range" min="0" max="2" step="0.01"
            value={amplitude_y} onChange={onAmplitude_ySlide} style={{ flex: 1 }}
          />
          <input
            type="number" step="0.01" value={amplitude_y}
            onChange={onAmplitude_yInput} style={{ width: 70 }}
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