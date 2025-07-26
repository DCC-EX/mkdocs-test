# Working with MkDocs

As outlined previously, MkDocs with the MkDocs Material theme are used as the basis of our documentation, utilising markdown plus other enhanced features to give our users a good experience.

Only a brief introduction to these are outlined below to set the context for their use within our documentation, aside from custom plugins we have written which are covered here.

Read the full [MkDocs documentation](https://www.mkdocs.org/) and [MkDocs Material documentation](https://squidfunk.github.io/mkdocs-material/) for more information.

## Previewing and Deploying MkDocs

Don't forget when working with MkDocs, you can preview locally by running ``mkdocs serve`` at a command prompt or bash console, and you can manually deploy to GitHub Pages (provided you have permissions to do so) with ``mkdocs gh-deploy``.

## DCC-EX CSS Styling

All customised styling for our branding and other customisations is contained in the "dccex_theme.css" file.

**Do not adjust the contents of this file without liaising with the DCC-EX Documenter team to ensure styling is consistent with our theme.**

## DCC-EX JavaScript Files

There are several JavaScript files included to perform various client side functions:

- clickable-cards.js - Makes a grid card clickable using the card's HREF, works with CSS to hide the link also
- ex-installer-run-helper.js - Helper to hide irrelevant installer links/pages based on the detected browser's operating system
- legacy-docs-new-tab.js - Ensures all HREF links pointing to `https://dcc-ex.com/legacy-docs/` open in a new tab
- platform.js - Helper to determine the browser's operating system
- search-helper.js - Helper to create search links, see [The search link](/contributing/documentation/4-understanding-links.md#the-search-link)

## MkDocs Material Extensions

While basic markdown is sufficient to get pages published with MkDocs and our documentation, there are certain extensions and plugins for MkDocs and the MkDocs Material theme that both improve the maintainability of our documentation, and improve the experience for our users.

The authoritative list of enabled extensions can be determined by the "mkdocs.yml" file.

**Do not adjust the contents of this file without liaising with the DCC-EX Documenter team to ensure no existing functionality is broken.**

### Admonitions - Warning, Danger, Example, Note

Use admonitions to create callouts for specific user attention, but **please ensure these are used sparingly** and only where strictly necessary. Adding general notes and using these tends to make the content too "busy", but adding a specific callout about voltage level differences is a good use case.

Some examples:

```markdown
!!! warning "This is a warning"

    Warnings are good to call out when appropriate.
```

!!! warning "This is a warning"

    Warnings are good to call out when appropriate.

```markdown
!!! danger "This is dangerous!"

    When dealing with things like voltage levels or power supplies, these are good to call out.
```

!!! danger "This is dangerous!"

    When dealing with things like voltage levels or power supplies, these are good to call out.

```markdown
??? example "A collapsible example"

    Examples can be good to call out sparingly, and this one is collapsible.
```

??? example "A collapsible example"

    Examples can be good to call out sparingly, and this one is collapsible.

```markdown
!!! note "A general note"

    This is a general note, use very sparingly.
```

!!! note "A general note"

    This is a general note, use very sparingly.

### Attribute Lists

Adding HTML attributes to inline or block level elements can be done using [Attribute Lists](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/?h=attr#attribute-lists).

**NOTE** that like all markdown syntax, there must be no spaces between the attribute list and the element it is being applied to.

```markdown
![Logo example small](/_static/images/logos/logo.png){ width=100px }
![Logo example](/_static/images/logos/logo.png){ width=200px }
```

This renders:

![Logo example small](/_static/images/logos/logo.png){ width=100px }
![Logo example](/_static/images/logos/logo.png){ width=200px }

The other most common example in our documentation is to provide a specific CSS class to an element, for example our buttons are a CSS class applied to a link:

```markdown
[Windows x64](https://github.com/DCC-EX/EX-Installer/releases/latest/download/EX-Installer-Win64.exe){ .md-button }
```

Renders [Windows x64](https://github.com/DCC-EX/EX-Installer/releases/latest/download/EX-Installer-Win64.exe){ .md-button }

Multiple attributes can be applied using spaces between them, don't use a comma or any other separator.

For example, this logo will be 100px wide and only show in light mode (switch to dark mode to hide it):

```markdown
![Logo example](/_static/images/logos/logo.png){ width=100px .only-light }
```

![Logo example](/_static/images/logos/logo.png){ width=100px .only-light }

### Snippets

To help us remove unnecessary duplication of content, we have enabled the ``pymdownx.snippets`` extension, which allows us to include content from a single file in other markdown files.

All files that are to be included as snippets must reside in the "includes" directory, and preferably within a subdirectory relevant to the topic.

**NOTE:** the code below includes extra back tick "`" characters at the beginning and end to prevent MkDocs rendering this as a snippet.

```markdown
`--8<-- "includes/snippet-example/snippet-example.md"`
```

The text below is included from this file:

--8<-- "includes/snippet-example/snippet-example.md"

### Icons and Emojis

To include an icon or emoji search for them in the [Icons, Emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/) section of the documentation.

To include, simply reference them as such:

```markdown
:thumbsup:
```

This renders :thumbsup:

## MkDocs Plugins

The authoritative list of enabled plugins can be determined by the "mkdocs.yml" file.

**Do not adjust the contents of this file without liaising with the DCC-EX Documenter team to ensure no existing functionality is broken.**

We have written two custom plugins for MkDocs to highlight the latest news articles and ensure the previous/next navigation buttons make sense within the context of what the user is seeing.

These plugins reside within the "plugins" directory and are included in "requirements.txt" for installation by contributors.

### DCC-EX Custom Latest News Plugin

This plugin simply grabs the title of the latest news/blog articles to create an unordered list which can be used in markdown files.

To include it in a file, include this text on its own line with a blank line above and below:

```markdown
<!-- LATEST-NEWS -->
```

You may need to indent this line to suit the nesting of lists etc.

This is included as a plugin in mkdocs.yml:

```yaml
plugins:
  - latest-news
```

By default, the latest 2 articles are included, this can be changed with:

```yaml
plugins:
  - latest-news:
      count: 3
```

To customise the list styling, either create the default class "news-list" or define your own:

```yaml
plugins:
  - latest-news:
      list-class: my-list-class
```

To ensure the CSS class correctly overrides MkDocs Material classes, make it specific, eg:

```css
.md-typeset li.news-headline-list {
  font-family: Audiowide,Helvetica,Arial,sans-serif;
  list-style: none;
  padding-left: 0;
  margin-left: 0 !important;
}
```

### DCC-EX Custom Scoped Nav Plugin and Custom footer.html

This plugin is used to set the scope of the previous and next navigation buttons to the directory pages are located in.

The first page in a directory will have no previous button, and the last no next button.

**NOTE:** This is calculated based on the sorting order of the page file names within the directory, and therefore custom ordering of pages using .nav.yml will cause unexpected results.

To enable this customised navigation, a custom "footer.html" template has been included and can be found in "overrides/partials/footer.html". This is required in order to show/hide the previous and next arrows as determined by the plugin.
