# Documentation Standards

This guide outlines the mandatory standards to adhere to for page naming, directory structure, and other related items.

We try to keep as few mandatory standards as possible, but these items must be adhered to in order for our documentation to be maintainable.

## General Content

When creating content, remember to keep the target user in mind at all times, with a strong preference to Conductor level users. A significant (and growing) proportion of our user base do not understand software, nor a lot of electronics or embedded systems. Use terminology they are likely understand.

Most importantly, **keep pages concise, to the point, and avoid excess words or waffle**. Not only does this make the key messages clear and easy to read for our users, but maintaining lengthy pages that are a wall of text becomes onerous, daunting, and reduces the likelihood of keeping our documentation current.

So:

- Brevity is good, keep topics to the concise point (eg. Conductors don't care about DCC waveforms, they care about running a train).
- Avoid jargon where possible.
- If something does need elaboration, link to a relevant reference.
- Don't document things generally available on the Internet, eg. we don't document MkDocs or the Material theme as there is good documentation available, we only document the context of our use cases.

## Do Not Duplicate Content

**DO NOT CREATE DUPLICATE CONTENT** as this increases the maintenance burden significantly but, more importantly, makes it difficult for users when content appears slightly differently in two different places or even contradicts itself. When needing to repeat information in more than one place, take advantage of the [MkDocs Snippets](/contributing/documentation/mkdocs-features.md#snippets) feature. This allows you to include the same markdown content in multiple places.

## Directory Naming, Page Naming, and Titles

With the exception of the home page and the DCC-EX News page, **do not use "index.md"**, but rather name pages according to their primary message. Using "index.md" adjusts the rendering of pages when navigating through the menus, and the team has a preference for the navigation experience using the benefits of the [MkDocs Awesome Nav plugin](https://lukasgeiter.github.io/mkdocs-awesome-nav/) over having an initial index page.

- All directory and page names must be in lower case and use "-" instead of spaces.
- Page ordering is determined by the Awesome Nav ".nav.yml" file, see [Directory Structure](/contributing/documentation/standards.md#directory-structure-and-navigation).
- The page title is determined by the top level heading, see [Headings](/contributing/documentation/formatting-guide.md#headings).

## Address all MkDocs Warnings and Errors

When running locally with ``mkdocs serve``, ensure any INFO, WARNING, or ERROR level messages are dealt with prior to submitting pull requests or deploying a new version.

!!! warning

    When we release the new MkDocs based documentation, the deployment GitHub workflow will enforce ``strict`` mode, meaning any issues will generate a workflow error, preventing updates being deployed.

## Directory Structure and Navigation

Note firstly that we use the [MkDocs Awesome Nav plugin](https://lukasgeiter.github.io/mkdocs-awesome-nav/) to control the menu structure, which uses a ".nav.yml" file in any directory where the default needs to be overridden.

The top level directories under the "docs" directory determine the tabs or horizontal menu items on the header bar, with the subsequent directories and files in each of these determining the menu on the left pane.

**Do not adjust the top level directories without consulting the DCC-EX Documenter team, as these fundamentally adjust the user experience.**

If a new top level directory is to be added, it needs to be added to the "/docs/.nav.yml" file in the appropriate order. Files and directories created within existing top level directories will automatically be added to the menus (see [Page Naming and Titles](#directory-naming-page-naming-and-titles) for page ordering).

### Managing Navigation files ".nav.yml"

When the default sort order or structure of a directory is not presenting as desired, a ".nav.yml" file can be created to determine sort order and navigation contents according to how the navigation structure is desired.

This is part of the MkDocs Awesome Nav plugin and all options are outlined on the [Features](https://lukasgeiter.github.io/mkdocs-awesome-nav/features/nav/) page.

If the directory you're creating a new Markdown file in has no ".nav.yml" file, the default sort order will be used, meaning you must preview the changes to ensure the end result is as desired.

If there is an existing ".nav.yml" file, simply add the new file in the correct order to the file.

**Be sure to review the build output** for information and warnings regarding pages. If the page you are creating has not been added, you will receive an *informational* message that it exists, but is not in the navigation tree. If you have added it incorrectly to the ".nav.yml" file, you will receive a *warning* message that an entry has been defined that does not exist.

A typical ".nav.yml" file should look like this:

```yaml
nav:
  - Contributing to Documentation: docs.md
  - Documentation Standards: standards.md
  - Formatting Guide: formatting-guide.md
  - Understanding Links: understanding-links.md
  - Using Our Logos: logos.md
  - Working With MkDocs: mkdocs-features.md
  - Mermaid Diagrams: mermaid-diagrams.md
```

### Managing Previous and Next Buttons

Our custom [Scoped Nav](/contributing/documentation/mkdocs-features.md#dcc-ex-custom-scoped-nav-plugin-and-custom-footerhtml) plugin automatically adjusts previous/next links to ensure that the previous and next buttons don't prompt a user to navigate automatically into irrelevant content.
