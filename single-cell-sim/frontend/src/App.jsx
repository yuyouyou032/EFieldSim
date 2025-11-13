import { useEffect, useState } from "react";
import { fetchScene } from "./api/client.js";
import ControlsPanel from "./components/ControlsPanel.jsx";

export default function App() {
  const [resultantField, setResultantField] = useState({
    deltaPhis: [0, 0],
    Ex: [],
    Ey: [],
    meta: {}
  });

  useEffect(() => {
    fetchScene({ 
      amplitude_x: 1.0, 
      amplitude_y: 1.0,
      frequency: 2 * Math.PI,
      phase_diff: 0
    }).then(d => setResultantField({
      deltaPhis: [d.delta_phi_1, d.delta_phi_2],
      Ex: d.resultantEx ?? [],
      Ey: d.resultantEy ?? [],
      meta: d.meta ?? {}
    }))
    .catch(err => console.error("init fetch failed", err));
  }, []);

  async function onParamsChange(params) {
    try {
      const d = await fetchScene(params);
      setResultantField({
        deltaPhis: [d.delta_phi_1, d.delta_phi_2],
        Ex: d.resultantEx ?? [],
        Ey: d.resultantEy ?? [],
        meta: d.meta ?? {}
      });
    } catch (e) {
      console.error("update failed", e);
    }
  }

  return (
    <div style={{ position: "relative", width: "100vw", height: "100vh", background: "#333" }}>
      <ControlsPanel onParamsChange={onParamsChange} />
      {/* Scene3D disabled for now */}
    </div>
  );
}
