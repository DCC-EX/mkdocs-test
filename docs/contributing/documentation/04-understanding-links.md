# Understanding Links

## What the html browser sees is this

An ABOSLUTE link in html starts with `/`  which makes the browser prepend the web server address so `href="/blah/blah.html"`  for example would link to `"http:://dcc-ex.com/blah/blah.html"` which would be BAD because  we actually wanted  `http:://dcc-ex.com/mkdocs-test/blah/blah.html` but there was no way of doing that if you didn't know the sub-directory mkdocs-test in advance and code it on all your links.

To resolve this, you have to use RELATIVE hrefs, in which the link is relative to the current page.  So if you are on page   `blah1/blah2/blah3.html` and you want a link or image in  `_static/images/stuff.jpg`  you have to use `href="../../_static/images/stuff.jpg"`

So.. RELATIVE HTML links are the only reliable way to work, otherwise your website is borked if you install it in for example `http:://dcc-ex.com/newsite/`

## What the mkdocs author sees

In mkdocs,  the markdown to html generator  passes through RELATIVE links unchanged, this means that you can easily refer to images in the same directory as the current page by just giving the name, or get to any other directory with the appropriate number of ../ to go up the tree.  That's great until you move the current page to another directory so the relative link is no longer going to find the image or page you want.

MkDocs has a solution. When you code what appears to be an absolute link like `/_static/images/spaff.png` then the HTM generated will look like `href="../../_static/images/spaff.png"`  with the appropriate number of `../` to walk back up the tree from the current file to the docs directory. So basically you code what looks like an ABSOLUTE link, but the html is generated with a relative link. Hooray!

BUT there is one annoying little quirk...

The intellisense when typing the start of a link like `[look here](/`   gives you a dropdown starting at docs  so you get `/docs/_static/images/spaff.jpg`   which wont get converted so it gives `href="/docs/_static/images/spaff.jpg"`  which isn't found because the `/docs/` directory level isnt copied to the website.

Pending a VSCode or mkDocs fix (both applied for) the only solution is to manually remove the `/docs` prefix from the link created by intellisense.

## The search link

The search link like `?turnout` is passed through unchanged by mkDocs but is intercepted in the browser by our own  [JavaSCript code](/_static/scripts/search-helper.js)
