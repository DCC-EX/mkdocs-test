(() => {
  const homeBackgroundImages = [
    "_static/images/home/home1.png",
    "_static/images/home/home2.png",
    "_static/images/home/home3.png",
    "_static/images/home/home4.png",
    "_static/images/home/home5.png",
    "_static/images/home/home6.png",
    "_static/images/home/home7.png",
    "_static/images/home/home8.png",
    "_static/images/home/home9.png",
    "_static/images/home/home10.png",
    "_static/images/home/home11.png",
    "_static/images/home/home12.png",
  ];
  let previousImage;
  let refreshTimer;
  let activeBackgroundBox;
  let activeBackgroundLayer;

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
    const imageUrl = `url("${new URL(image, document.baseURI).href}")`;

    if (backgroundBox !== activeBackgroundBox) {
      activeBackgroundBox = backgroundBox;
      activeBackgroundLayer = "a";
      backgroundBox.style.setProperty("--home-background-image-a", imageUrl);
      backgroundBox.classList.add("home-background-a");
      backgroundBox.classList.remove("home-background-b");
      return true;
    }

    activeBackgroundLayer = activeBackgroundLayer === "a" ? "b" : "a";
    backgroundBox.style.setProperty(
      `--home-background-image-${activeBackgroundLayer}`,
      imageUrl
    );
    backgroundBox.classList.toggle("home-background-a", activeBackgroundLayer === "a");
    backgroundBox.classList.toggle("home-background-b", activeBackgroundLayer === "b");
    return true;
  }

  function startHomeBackgroundRefresh() {
    if (!setRandomHomeBackground()) return;

    window.clearInterval(refreshTimer);
    refreshTimer = window.setInterval(setRandomHomeBackground, 15_000);
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
