// 🎯 3D Tilt Effect
document.addEventListener("mousemove", (e) => {
  const x = (window.innerWidth / 2 - e.clientX) / 25;
  const y = (window.innerHeight / 2 - e.clientY) / 25;

  const building = document.getElementById("building");
  if (building) {
    building.style.transform = `rotateY(${x}deg) rotateX(${y}deg)`;
  }
});

// 🎬 Smooth Transition Helper
function smoothEnter(element) {
  element.style.transform = "scale(0.9)";
  element.style.opacity = "0";

  setTimeout(() => {
    element.style.transform = "scale(1)";
    element.style.opacity = "1";
  }, 100);
}