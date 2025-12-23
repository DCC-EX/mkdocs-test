# Contributing to Documentation

This page outlines what you need in order to contribute to the documentation, along with the various markdown attributes and so forth you can use.

The documentation is hosted using GitHub Pages and is written in Markdown format, using MkDocs to publish the content. We use the MkDocs Material theme to give us the framework for the look and feel of the website, along with a number of other useful plugins and extensions to enhance the content.

**Important! Once up and running with the information on this page, please ensure you are familiar with general markdown syntax.**

Refer to the [Markdown Guide](https://www.markdownguide.org/).

## How to Contribute

For contributions from the general public, we recommend forking the [GitHub repository](https://github.com/DCC-EX/dcc-ex.github.io) and submitting pull requests for the DCC-EX Documenter team to review and merge.

If you wish to contribute more fully and become a part of the DCC-EX Documenter team, reach out to us via [Discord](https://discord.gg/y2sB4Fp). To gain access to the [GitHub repository](https://github.com/DCC-EX/dcc-ex.github.io), one of the DCC-EX team administrators will need to add you to the "Web" team in GitHub.

## MkDocs Links

Here are some handy links with more info:

- [MkDocs website](https://www.mkdocs.org/) - The official MkDocs documentation.
- [MkDocs Material theme](https://squidfunk.github.io/mkdocs-material/) - The MkDocs Material theme documentation.
- [MkDocs Awesome Nav plugin](https://lukasgeiter.github.io/mkdocs-awesome-nav/) - MkDocs Awesome Nav plugin is what we use for dynamic page structure.
- [MkDocs RSS plugin](https://guts.github.io/mkdocs-rss-plugin/) - The MkDocs RSS Plugin publishes our DCC-EX News feed.
- [MkDocs Open in New Tab plugin](https://github.com/JakubAndrysek/mkdocs-open-in-new-tab) - The Open in New Tab plugin ensures all links to external websites open in a new tab to ensure the users' browsing experience in our documentation is consistent.

## What You Need to Install

This is the list of software you need to successfully contribute to the documentation, including being able to preview it locally:

- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)
- [Python](https://www.python.org/) - Version 3.13 is recommended, minimum required is 3.10

There are two VSCode plugins that are highly recommended also:

- Markdown Preview Mermaid Support by Matt Bierner - enables previewing Mermaid diagrams in VSCode
- markdownlint by David Anson - helps keep consistent, good formatting in Markdown files (like flake8 for Python)

## Getting Started

Once you have installed VSCode and Python, you need to clone the [GitHub repository](https://github.com/DCC-EX/dcc-ex.github.io), set up a virtual environment, and install the MkDocs requirements.

We recommend using the built-in Git functionality of VSCode to clone the repository, or you can use [GitHub Desktop](https://github.com/apps/desktop) or command line Git, whichever you prefer. There is plenty of information generally available on that so we won't cover it here, and instead will focus on the specifics required to ready to contribute to MkDocs content.

Follow the appropriate section below to setup MkDocs in Python for your operating system:

### Setup on macOS

```bash
cd mkdocs-test
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Setup on Linux

``` bash
cd mkdocs-test
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

### Setup on Windows

```console
cd mkdocs-test
virtualenv venv
venv\scripts\activate
pip install -r requirements.txt
```

## Previewing and building MkDocs

Previewing locally is very simple:

```bash
mkdocs serve
```

Navigate to the [local preview in a browser](http://localhost:8000/mkdocs-test/).

When finished with the local preview, stop the local server with either ++ctrl+c++ (Windows/Linux) or ++cmd+c++ (macOS).

Building locally is equally as simple:

```bash
mkdocs build --strict
```

MkDocs also has a feature to deploy to GitHub pages without using a workflow:

```bash
mkdocs gh-deploy
```
