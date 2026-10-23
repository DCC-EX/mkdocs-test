(() => {
  const homeBackgroundImages = [
    "_static/images/home/home1.png",
    "_static/images/home/home2.png",
    "_static/images/home/home3.png",
    "_static/images/home/home4.png",
    "_static/images/home/home5.png",
    "_static/images/home/home6.png",
    "_static/images/home/home7.png",
  ];
  let previousImage;
  let refreshTimer;

  function setRandomHomeBackground() {
    const backgroundBox = document.querySelector(".paragraph-bg-box");
    if (!backgroundBox) return false;

    const availableImages = homeBackgroundImages.filter(
      image => image !== previousImage
    );
    const images = availableImages.length > 0
      ? availableImages
      : homeBackgroundImages;
    const image = images[Math.floor(Math.random() * images.length)];
    previousImage = image;
    backgroundBox.style.backgroundImage =
      `url("${new URL(image, document.baseURI).href}")`;
    return true;
  }

  function startHomeBackgroundRefresh() {
    if (!setRandomHomeBackground()) return;

    window.clearInterval(refreshTimer);
    refreshTimer = window.setInterval(setRandomHomeBackground, 10_000);
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(startHomeBackgroundRefresh);
  } else if (document.readyState === "loading") {
    document.addEventListener(
      "DOMContentLoaded",
      startHomeBackgroundRefresh,
      { once: true }
    );
  } else {
    startHomeBackgroundRefresh();
  }
})();
