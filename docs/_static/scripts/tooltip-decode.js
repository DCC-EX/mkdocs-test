document.addEventListener('DOMContentLoaded', function() {
  // Decode encoded line breaks in title attributes and data-tooltip attributes
  function decodeText(s) {
    if (!s) return s;
    return s.replace(/&#10;|\\n/g, '\n');
  }

  // Fix existing title attributes
  document.querySelectorAll('a[title]').forEach(function(a) {
    var t = a.getAttribute('title');
    if (t && (t.indexOf('&#10;') !== -1 || t.indexOf('\\n') !== -1)) {
      a.title = decodeText(t);
    }
  });

  // Support data-tooltip attributes (if gen_toc is changed to emit data-tooltip)
  document.querySelectorAll('a[data-tooltip]').forEach(function(a) {
    var t = a.getAttribute('data-tooltip');
    if (t) {
      a.title = decodeText(t);
    }
  });
});
