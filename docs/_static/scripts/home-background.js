const homeBackgroundImages = [
  "_static/images/home/home1.png",
  "_static/images/home/home2.png",
];

function setRandomHomeBackground() {
  const backgroundBox = document.querySelector(".paragraph-bg-box");
  if (!backgroundBox) return;

  const image = homeBackgroundImages[
    Math.floor(Math.random() * homeBackgroundImages.length)
  ];
  backgroundBox.style.backgroundImage =
    `url("${new URL(image, document.baseURI).href}")`;
}

if (typeof document$ !== "undefined") {
  document$.subscribe(setRandomHomeBackground);
} else if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", setRandomHomeBackground);
} else {
  setRandomHomeBackground();
}
