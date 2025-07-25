# Working with MkDocs

As outlined previously, MkDocs with the MkDocs Material theme are used as the basis of our documentation, utilising markdown plus other enhanced features to give our users a good experience.

## Previewing and Deploying MkDocs

Don't forget when working with MkDocs, you can preview locally by running ``mkdocs serve`` at a command prompt or bash console, and you can manually deploy to GitHub Pages (provided you have permissions to do so) with ``mkdocs gh-deploy``.

## MkDocs Plugins

The authoritative list of enabled plugins can be determined by the "mkdocs.yml" file.

**Do not adjust the contents of this file without liaising with the DCC-EX Documenter team to ensure no existing functionality is broken.**

## MkDocs Material Extensions

While basic markdown is sufficient to get pages published with MkDocs and our documentation, there are certain extensions and plugins for MkDocs and the MkDocs Material theme that both improve the maintainability of our documentation, and improve the experience for our users.

The authoritative list of enabled extensions can be determined by the "mkdocs.yml" file.

**Do not adjust the contents of this file without liaising with the DCC-EX Documenter team to ensure no existing functionality is broken.**

### Attribute Lists

Adding HTML attributes to inline or block level elements can be done using [Attribute Lists](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown/?h=attr#attribute-lists).

```markdown
![Logo example small](/_static/images/logos/logo.png){ width=100px }
![Logo example](/_static/images/logos/logo.png){ width=200px }
```

This renders:

![Logo example small](/_static/images/logos/logo.png){ width=100px }
![Logo example](/_static/images/logos/logo.png){ width=200px }

### Snippets

To help us remove unnecessary duplication of content, we have enabled the ``pymdownx.snippets`` extension, which allows us to include content from a single file in other markdown files.

```markdown
\--8<-- "includes/<directory>/<filename>"
```

### Icons and Emojis

To include an icon or emoji search for them in the [Icons, Emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/) section of the documentation.

To include, simply reference them as such:

```markdown
:thumbsup:
```

This renders:

:thumbsup:
