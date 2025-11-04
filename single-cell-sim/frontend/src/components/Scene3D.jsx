import { useEffect, useRef } from "react";
import * as THREE from "three";

export default function Scene3D({ raysData }) {
  const mountRef = useRef(null);
  const refs = useRef({ scene: null, camera: null, renderer: null, lines: [] });

  // one-time three.js setup
  useEffect(() => {
    const mount = mountRef.current;
    const width = mount.clientWidth, height = mount.clientHeight;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x111111);

    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.set(0, 20, 40);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(width, height);
    mount.appendChild(renderer.domElement);

    scene.add(new THREE.DirectionalLight(0xffffff, 1).position.set(10,20,10));

    refs.current = { scene, camera, renderer, lines: [] };

    let stop = false;
    (function loop() {
      if (stop) return;
      requestAnimationFrame(loop);
      renderer.render(scene, camera);
    })();

    // handle resize
    function onResize() {
      const w = mount.clientWidth, h = mount.clientHeight;
      renderer.setSize(w, h);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
    }
    window.addEventListener("resize", onResize);

    return () => {
      stop = true;
      window.removeEventListener("resize", onResize);
      renderer.dispose();
      mount.removeChild(renderer.domElement);
    };
  }, []);

  // update lines whenever raysData changes
  useEffect(() => {
    const { scene } = refs.current;
    if (!scene) return;

    // remove old lines
    refs.current.lines.forEach(l => scene.remove(l));
    refs.current.lines = [];

    if (!Array.isArray(raysData)) return;

    raysData.forEach(ray => {
      const positions = new Float32Array(ray.flat()); // [[x,y,z]...] → Float32Array
      const geometry = new THREE.BufferGeometry();
      geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
      const material = new THREE.LineBasicMaterial({ color: 0xffaa00 });
      const line = new THREE.Line(geometry, material);
      scene.add(line);
      refs.current.lines.push(line);
    });
  }, [raysData]);

  return <div ref={mountRef} style={{ position: "absolute", inset: 0 }} />;
}