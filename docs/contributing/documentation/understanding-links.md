# Understanding Links

## What the html browser sees is this

An ABSOLUTE link in html starts with `/`  which makes the browser prepend the web server address so `href="/blah/blah.html"`  for example would link to `"http:://dcc-ex.com/blah/blah.html"` which would be BAD because  we actually wanted  `http:://dcc-ex.com/mkdocs-test/blah/blah.html` but there was no way of doing that if you didn't know the sub-directory mkdocs-test in advance and code it on all your links.

To resolve this, you have to use RELATIVE hrefs, in which the link is relative to the current page.  So if you are on page   `blah1/blah2/blah3.html` and you want a link or image in  `_static/images/stuff.jpg`  you have to use `href="../../_static/images/stuff.jpg"`

So.. RELATIVE HTML links are the only reliable way to work, otherwise your website is borked if you install it in for example `http:://dcc-ex.com/newsite/`

## What the ProperDocs author sees

In ProperDocs,  the markdown to html generator  passes through RELATIVE links unchanged, this means that you can easily refer to images in the same directory as the current page by just giving the name, or get to any other directory with the appropriate number of ../ to go up the tree.

When typing a link in VSCode, the intellisense dropdown will help you complete the link by following the path from the current folder.
    
If you enter `[your title](.` as soon as you type ``.`` VSC will show you a list of folder and .md files in the current folder to select from. If you type ``..`` or ``../`` or ``../..`` etc. you can navigate up and down the folder structure to find the document you need.  This embeds the relative link to the document.

The technique above ensures that the link is valid.  However if you move the current page to another directory so the relative link is no longer going to find the image or page you want. This trade off is worth that risk.

Note that relative links are the only way to get images to preview in VSC.

## The search link

The search link like `?turnout` is passed through unchanged by ProperDocs but is intercepted in the browser by our own  [JavaSCript code](/_static/scripts/search-helper.js)
