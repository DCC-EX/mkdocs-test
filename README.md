# MkDocs Testing

Repository to test if MkDocs meets the DCC-EX team's needs for a fresh start on simpler to maintain documentation.

MkDocs is being tested with the Material theme, which is reported to have an excellent search engine and other built-in features that reduce dependency complexity.

## Evaluation requirements

This is the simple working list of requirements to evaluate against:

- Must have at least a basic DCC-EX look/feel colour theme
- Must have useful search capability
- Must target RTR user base primarily
- Must be easy to contribute to for non-developers, nothing more complicated than Markdown syntax
- Must render well on both mobile and web
- Must reduce maintenance/management complexity as much as possible
- Must have DCC-EX News type blog/RSS feed
- Must support internal reference links
- Should enable adding new content without having to faff about with site structure
- Should have a glossary of terms
- Should be easy to preview locally
- Could have an auto generated list of references where glossary terms are in docs
- Could have a selector to change between production and development versions
- Will not have a complicated "language" or other that people need to learn in order to contribute

## MkDocs links

[MkDocs website](https://www.mkdocs.org/)
[MkDocs Material theme](https://squidfunk.github.io/mkdocs-material/)
[MkDocs Awesome Nav plugin](https://lukasgeiter.github.io/mkdocs-awesome-nav/)

## MkDocs requirements

MkDocs does require Python in order to be previewed and built locally, and all testing is being performed with Python 3.13.

**Minimum python version seems to be 3.10**.

Previewing and building locally is recommended to be done in a virtual environment, with requirements installed.

macOS:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Linux:

You have pthon3 and the python3-venv installed with  packet manager of your choice

``` bash
cd mkdocs-test
mkdir venv
python3.10 -m venv venv # 3.10 or later
. ./venv/bin/activate
```

Now you should have a prompt that starts with "(venv)"

``` bash
pip3 install -r requirements.txt
pull_exrail.sh
```

Windows:

```console
virtualenv venv
venv\scripts\activate
pip install -r requirements.txt
pull_exrail.ps1
```

## Previewing and building MkDocs

Previewing locally is very simple:

```bash
mkdocs serve
```

Navigate to the local preview in a browser at <http://localhost:8000/mkdocs-test/>.

Building locally is equally as simple:

```bash
mkdocs build
```

MkDocs also has a feature to deploy to GitHub pages without using a workflow:

```bash
mkdocs gh-deploy
```

## Design Principles for DCC-EX (Pete)

- Must have at least a basic DCC-EX look/feel colour theme
- Must have useful search capability
- Must target RTR user base primarily
- Must be easy to contribute to for non-developers, nothing more complicated than Markdown syntax
- Must render well on both mobile and web
- Must reduce maintenance/management complexity as much as possible
- Must have DCC-EX News type blog/RSS feed
- Must support internal reference links
- Should enable adding new content without having to faff about with site structure
- Should have a glossary of terms
- Should be easy to preview locally
- Could have an auto generated list of references where glossary terms are in docs
- Could have a selector to change between production and development versions
- Will not have a complicated "language" or other that people need to learn in order to contribute

That's actually one of the problems, we have too many complex pages! Or at least long pages anyway.

Half the wins we should be able to get here actually have nothing to do with MkDocs, Sphinx, Markdown, or reStructuredText, but rather in just taking a different approach to how we do things full stop.

Instead of trying to cater for every possible custom tinkerer/engineer option on the planet, we need to start with the RTR user front and centre, and use that as the basis for the structure.

So, we should focus on getting the CSB1 process in there first, and the latest EX-Installer updates.

The drive for MkDocs (or something simpler than RST) is that it just uses Markdown, which is a lot simpler for people to come to grips with, and if you don't want to run MkDocs locally, you can at least preview Markdown in VSCode directly, you just won't see it in the context of the website.

Using a paid WYSIWIG editor or service is ok, but it does mean everyone who contributes will need an account, and people outside the team can't just submit a PR of updates for us to review/approve, meaning we will always be blockers for getting those updates in. Further, it means as we figure out how to add doco from code comments, that will become complex or impossible depending on the service.

I'm planning to keep playing with MkDocs, but we do need to figure out what the actual structure should look like.

I'm leaning towards the user journey type idea I started with which is what drove us to have the links on the front page helping direct people to the right starting point. I'm open to whatever is the best approach, as long as it is simple for users to use.

Which ever way we go, we absolutely must reduce the amount of text we've used. No waffle. A wall of text is not only hard to read, but makes it hard to maintain.

## Additional comments (cf early discord chat, Chris)

I think part of the problem was we used too many things like callouts and side notes and tried too hard to create massively long discussions showing every possible way of doing obscure stuff...

For example, you don't need  "what's on this page" when each page only has one thing.

Keeping pages task-oriented automatically helps stuff become intelligible and commands that play together get discussed together in context but leave out the discussion of parameters that are unnecessary, irrelevant, or could be added later.

For things like the diy build, the things like mega, esp32  csb1, nucleo really need to show on only one small page where you select the one you are interested in... we should avoid anything that smells like  " on a csb1 you do it like this but on an stm32 you do it like that"

## Recommended VSCode Extensions for Markdown (Pete)

I highly recommend including two Markdown related VSCode extensions to help keep consistent formatting:

- Markdown Preview Mermaid Support by Matt Bierner - enables previewing Mermaid diagrams in VSCode
- markdownlint by David Anson - helps keep consistent, good formatting in Markdown files (like flake8 for Python)
