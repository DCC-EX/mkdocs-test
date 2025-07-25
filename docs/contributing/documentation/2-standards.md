# Documentation Standards

This guide outlines the mandatory standards to adhere to for page naming, directory structure, and other related items.

We try to keep as few mandatory standards as possible, but these items must be adhered to in order for our documentation to be maintainable.

## General Content

When creating content, remember to keep the target user in mind at all times, with a strong preference to Conductor level users. A significant (and growing) proportion of our user base do not understand software, nor a lot of electronics or embedded systems. Use terminology they are likely understand.

Most importantly, **keep pages concise, to the point, and avoid excess words or waffle**. Not only does this make the key messages hard to read, but maintaining lengthy pages that are a wall of text becomes onerous, daunting, and reduces the likelihood of keeping our documentation current.

So:

- Brevity is good, keep topics to the concise point (eg. Conductors don't care about DCC waveforms, they care about running a train).
- Avoid jargon where possible.
- If something does need elaboration, link to a relevant reference.
- Don't document things generally available on the Internet, eg. we don't document MkDocs or the Material theme as there is good documentation available, we only document the context of our use cases.

## Directory Naming, Page Naming, and Titles

- All directory and page names must be in lower case and use "-" instead of spaces.
- If specific page ordering is required, simply preface with the appropriate page number eg. "1-standards-formatting.md".
- The page title is determined by the top level heading, see [Headings](/contributing/documentation/3-formatting-guide.md#headings).

## Address all MkDocs Warnings and Errors

When running locally with ``mkdocs serve``, ensure any INFO, WARNING, or ERROR level messages are dealt with prior to submitting pull requests or deploying a new version.

## Directory Structure

Note firstly that we use the [MkDocs Awesome Nav plugin](https://lukasgeiter.github.io/mkdocs-awesome-nav/) to control the menu structure, which uses a ".nav.yml" file in any directory where the default needs to be overridden.

The top level directories under the "docs" directory determine the tabs or horizontal menu items on the header bar, with the subsequent directories and files in each of these determining the menu on the left pane.

**Do not adjust the top level directories without consulting the DCC-EX Documenter team, as these fundamentally adjust the user experience.**

If a new top level directory is to be added, it needs to be added to the "/docs/.nav.yml" file in the appropriate order. Files and directories created within existing top level directories will automatically be added to the menus (see [Page Naming and Titles](#directory-naming-page-naming-and-titles) for page ordering).
