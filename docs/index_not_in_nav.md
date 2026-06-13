# Site Index

Below is a dynamically generated list of all available pages on this website, parsed directly from the site's live sitemap.

<div id="sitemap-container">Loading sitemap...</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
    // Dynamically locate sitemap.xml relative to the root URL
    const sitemapUrl = window.location.origin + window.location.pathname.split('/').slice(0, -2).join('/') + '/sitemap.xml';

    fetch(sitemapUrl)
        .then(response => {
            if (!response.ok) throw new Error("Could not fetch sitemap.xml");
            return response.text();
        })
        .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
        .then(data => {
            const urls = data.getElementsByTagName("loc");
            let html = "<ul style='line-height: 1.8;'>";

            for (let i = 0; i < urls.length; i++) {
                let link = urls[i].textContent;

                // Clean up the URL to make a readable title
                let cleanName = link.replace(window.location.origin, "")
                                    .replace(/\/$/, "")
                                    .split("/")
                                    .pop()
                                    .replace(/[-_]/g, " ");

                // Capitalize first letter of words
                if (cleanName === "" || cleanName.includes(".html")) cleanName = "Home";
                else cleanName = cleanName.charAt(0).toUpperCase() + cleanName.slice(1);

                html += `<li><a href="${link}">${cleanName}</a> <small style="color: gray;">(${link})</small></li>`;
            }
            html += "</ul>";
            document.getElementById("sitemap-container").innerHTML = html;
        })
        .catch(err => {
            document.getElementById("sitemap-container").innerHTML = 
                `<p style="color: red;">Failed to load sitemap. Ensure the site is built and running on GitHub Pages.</p>`;
            console.error(err);
        });
});
</script>
