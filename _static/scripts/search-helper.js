function findnow(term) {
    var s = document.querySelector('input.md-search__input');
    if (s) {
        s.value = term;
        s.focus();
        s.dispatchEvent(new Event('input'));
    }
    return false;
}
document.addEventListener('click', function(event) {
    var link = event.target.closest('a');
    if (link && link.getAttribute('href') && link.getAttribute('href').startsWith('?')) {
        event.preventDefault();
        // Extract the part after '?'
        var rest = link.getAttribute('href').slice('?'.length);
        findnow(rest);
    }
});
