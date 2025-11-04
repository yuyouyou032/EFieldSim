import { useEffect, useState } from "react";
import { fetchScene } from "./api/client.js";
import ControlsPanel from "./components/ControlsPanel.jsx";
import Scene3D from "./components/Scene3D.jsx";

export default function App() {
  const [rays, setRays] = useState([]);

  useEffect(() => {
    fetchScene({ focal_length: 10 }).then(d => setRays(d.rays ?? []))
      .catch(err => console.error("init fetch failed", err));
  }, []);

  async function onParamsChange(params) {
    try {
      const d = await fetchScene(params);
      setRays(d.rays ?? []);
    } catch (e) {
      console.error("update failed", e);
    }
  }

  return (
    <div style={{ position: "relative", width: "100vw", height: "100vh" }}>
      <Scene3D raysData={rays} />
      <ControlsPanel onParamsChange={onParamsChange} />
    </div>
  );
}