/*
  The scripts in this file ensure EX-Installer downloads are correct for the user's operating system.
*/

/*
  This method associates the getEXInstallerLink() method below with any Markdown link tagged with the attribute:

  #download-ex-installer-link

  eg. [Download EX-Installer](#){ #download-ex-installer-link }
*/
document.addEventListener('DOMContentLoaded', function () {
  // Get a reference to your download link by its ID
  const downloadLink = document.getElementById('download-ex-installer-link');

  // Ensure the link exists on the page
  if (downloadLink) {
    // Add a click event listener to the link
    downloadLink.addEventListener('click', function (event) {
      event.preventDefault(); // <--- IMPORTANT: Prevent the browser's default link behavior

      // Call your existing JavaScript method to get the download link
      // Assumption: getEXInstallerLink() returns the appropriate download URL.
      const downloadUrl = getEXInstallerLink();

      // If the method returns a URL, navigate to it
      if (downloadUrl) {
        window.location.href = downloadUrl;
      }
      // If getEXInstallerLink() itself handles the redirection (e.g., uses window.location.href internally),
      // then you might just call it like: getEXInstallerLink(); and remove the 'if (downloadUrl)' block.
      // Adjust based on how your getEXInstallerLink() method is implemented.
    });
  }
});

/*
  This method is used to supply the user with the correct link to the latest EX-Installer for their Operating System.
  
  It appends the appropriate type to this URL:
  
  https://github.com/DCC-EX/EX-Installer/releases/latest/download/EX-Installer-

*/
function getEXInstallerLink() {
  filename = "not supported";
  switch (platform.os.family) {
    case "Windows":
      if (platform.os.architecture == 64) {
        filename = "Win64.exe";
      }
      break;
    case "Red Hat":
    case "CentOS":
    case "Ubuntu":
    case "Debian":
    case "Fedora":
    case "Linux":
      if (platform.os.architecture == 64) {
        filename = "Linux64";
      }
      break;
    case "OS X":
      if (platform.os.architecture == 64) {
        filename = "macOS";
      }
  }
  if (filename === "not supported") {
    alert("OS Version not supported");
    return;
  } else {
    window.open("https://github.com/DCC-EX/EX-Installer/releases/latest/download/EX-Installer-" + filename, "_blank");
  }
}
