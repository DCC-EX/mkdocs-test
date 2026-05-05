function findnow(term) {
    var s = document.querySelector('input.md-search__input');
    if (s) {
        s.value = term;
        s.focus();
        s.dispatchEvent(new Event('input'));    
    }
}

// Replace search links with onClick handlers on page load
function setupSearchLinks() {
    var links = document.querySelectorAll('a[href*="/?"]');
    links.forEach(function(link) {
        var href = link.getAttribute('href');
        if (href && href.includes('/?')) {
            var rest = href.split('?')[1];
            if (rest && !rest.includes('=')) {
                var searchTerm = decodeURIComponent(rest);
                // Replace href with '#' and set onClick handler
                link.setAttribute('href', null);
                link.onclick = function(event) {
                    event.preventDefault();
                    event.stopPropagation();
                    findnow(searchTerm);
                    return false;
                };
            }
        }
    });
}

// Run setup when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupSearchLinks);
} else {
    setupSearchLinks();
}

// If links are added dynamically after page load, they will use the old click listener
/* document.addEventListener('click', function(event) {
    var link = event.target.closest('a');
    if (link && link.getAttribute('href') && link.getAttribute('href').includes('/?')) {
        // Extract the part after '?'
        var rest = link.getAttribute('href').split('?')[1];
        if (rest && !rest.includes('=')) {
            // Prevent the anchor navigation and run the search instead
            event.preventDefault();
            event.stopPropagation();
            findnow(decodeURIComponent(rest));
            return false;
        }
    }
});
*/
