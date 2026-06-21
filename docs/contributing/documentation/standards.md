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
- It is extremely important *for the search results to work correctly* to:
    - Ensure sure the page title is the first item on the page (after any tags).  If it is not the file name will appear in the search results, not the title.
    - Ensure that the block of text between the page title and the next heading (of any sort) is relatively short. Ideally no more than a few paragraphs. This is what what will appear in the search results.
    - Ensure that you DO NOT use tables or complex formatting in the first block of text (between the page title and the next heading) as this will be scrambled in the search results.
- Product names:
    - Bold any product names. Hyperlink them to the appropriate page where practical.
    - i.e. use '\*\*EX-CommandStation\*\*' not 'EX-CommandStation'
    - Don't abbreviate product names.
    - e.g. use '**EX-CSB1**' not 'CSB1'
    - Alsways include the hyphen('-') e.g. **EX-CSB1**, not EXCSB1.
- Avoid abbreviations that would not be easily recognised by 'Conductors'.
    - In particular *don't* use 'CS'.  Use the full name 'Command Station' or, more commonly, 'EX-CommandStation'
    - *Don't* use 'AP'.  Use 'Access Point' or 'Access Point Mode' or 'Access Point Mode (AP)'
    - *Don't* use 'STA'.  Use 'Station' or 'Station Mode' or 'Station Mode (STA)'
    - *Limit the use of* using 'RTR' or 'R2R'.  Use 'ready-to-run' or 'ready-to-run (RTR)'
    - Limit the use of- using 'DIY'.  Use 'do-it-yourself' or 'do-it-yourself (DIY)'

- Keep headings short.  If it fills the page it is too long.
- Keep sentences short.  Break them up where ever possible.
- Keep paragraphs short.  Break them up where practical.
- Keep paragraphs on the same topic. If the topic changes start a new paragraph.
- Do not start any page for a Conductor or Tinkerer with a technical explanation.  Put technical explanations at the end of the page, or preferably in a separate dedicated page.  Make it clear the the technical explanation is not required reading (unless it is).
- If you have a number of sections that describe options; present them in list them first, before the sections, with an explanation as to why they are optional.  (i.e. a bullet list with hyperlinks to the headings.)
- Where possible, avoid starting a section with a negative point of view.  i.e. Talk about the positives of what you are discussing first, before you delve into the negative or problematic aspects. <br/>e.g. Don't start with "... This is not for Conductors...", instead say "..This page is for Tinkerers ... Conductors should...".
- Use British/Australian/New Zealand/Canadian/Indian (pretty much every country except the USA) spelling e.g. 'colour' not 'color'. <br/>(Primarily because it is used in more English speaking countries)
- Preferred Terms:
    - Use **'EX-CommandStation'** not 'Command Station' when referring to something that is specific to the **DCC-EX** product.
    - Where logical to do so, use **"Motor Driver"**, in preference to 'Motor Shield'.  Do not use 'Motor Board' or 'Motorboard'.
    - In general use **'train'** or **'loco'** instead of 'locomotive' or 'engine'
    - Use **'Smart Phone'** instead of 'Cell Phone' (US only term) or 'Mobile Phone' (just about everywhere else)
    - Use **Throttle** or **Throttle (controller)** instead of 'controller' or 'controller (throttle)'

- Use railroad/railway/railway terminology that is understandable by all English-speaking people. <br/><br/>Where there are clear differences from USA to non-US terminology use both with a slash between and use the US version first. e.g. turnouts/points, consists/multiple units, switching/shunting.  (Only because the US term appears in apps like JMRI and in **EXRAIL**.)
- For dates, use **dd-mmm-yyyy** or **yyyy-mm-dd** to avoid confusion with the way dates are uniquely/weirdly written in the USA. <br/> e.g. Use 2-Mar-2022 or 2022-3-2, not 2-3-2022
- No full stop at the end of a numbered or unnumbered list unless the points are most points are multi-sentence.
- Numbered lists should generally only be used if they are describing a specific sequence, or the numbering is important to the text.
- Use second person (you and your; not I, me, my) language
- A string of nouns should be generally be sequenced in alphabetic order, unless it makes more sense within the context to display them in some other sequence.
- Double quotes (") should only be used for quoting text from people, documents or web sites.  Otherwise use single quotes (').
- Don't use curly quotes ``‘ ’ “ ”``.
- No quotes around 'Also See' type references.
- Avoid 'above' or 'below' in text.  Use hyperlinks instead.
- ``==TODO==`` means that it is still a work-in-process and needs to be updated.  It must be followed by descriptive text describing the issue to be fixed.
- Do not use images that only contain text unless there is no choice. Image text cannot be searched. Image text cannot be easily translated.
- Keep the first section (between H! and the first H2) reasonably short. This is what appears search results.
- The first section (between H! and the first H2) should describe what is on the rest if the page.

## Do Not Duplicate Content

**DO NOT CREATE DUPLICATE CONTENT** as this increases the maintenance burden significantly but, more importantly, makes it difficult for users when content appears slightly differently in two different places or even contradicts itself. When needing to repeat information in more than one place, take advantage of the [MkDocs Snippets](/contributing/documentation/mkdocs-features.md#snippets) feature. This allows you to include the same markdown content in multiple places.

## Directory Naming, Page Naming, and Titles

With the exception of the home page and the **DCC-EX** News page, **do not use "index.md"**, but rather name pages according to their primary message. Using "index.md" adjusts the rendering of pages when navigating through the menus, and the team has a preference for the navigation experience using the benefits of the [MkDocs Awesome Nav plugin](https://lukasgeiter.github.io/mkdocs-awesome-nav/) over having an initial index page.

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

**Do not adjust the top level directories without consulting the **DCC-EX** Documenter team, as these fundamentally adjust the user experience.**

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

**Note on relative paths in .nav.yml**: At the time of writing, there seems to be an undocumented bug related to MkDocs and/or the MkDocs Awesome Nav plugin that means you cannot use upwards level relative links within the ".nav.yml" file.

So, this will not work:

```yaml
nav:
  - A relative up link: ../relative/page.md
```

You must instead use an absolute path for this:

```yaml
nav:
  - A relative up link: parent/relative/page.md
```

### Managing Previous and Next Buttons

Our custom [Scoped Nav](/contributing/documentation/mkdocs-features.md#dcc-ex-custom-scoped-nav-plugin-and-custom-footerhtml) plugin automatically adjusts previous/next links to ensure that the previous and next buttons don't prompt a user to navigate automatically into irrelevant content.
