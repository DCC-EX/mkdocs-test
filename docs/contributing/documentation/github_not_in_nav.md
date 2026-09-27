# GitHub repository

In order for GitHub pages to function correctly and automatically publish updated content, the content must be located in a specific repository named after the GitHub organisation, and therefore our website repository is [mk-docs-test](https://github.com/DCC-EX/mkdocs-test).

In addition to this, rather than using the main or master branch, the default branch is called "main", so any branches created for contributing to documentation must use this as the parent, and all pull requests must be submitted against this same branch.

## Procedure

### Procedure overview

Ideally the documentation cycle would look like this..

![Ideal GitHub Documentation Cycle](../../_static/images/github/github_doc_cycle1.png){ width=400px}

Changes to the original would be pulled down from the original repository directly to your local (PC) repository.  You would push your changes to your GitHub website repository. Then create a *Pull request* to send them to the original for review.

While this is possible, both **GitHub Desktop** and **VSCode** make it extremely cumbersome to do so.

*So instead a slightly longer approach is described below...*

![GitHub Documentation Cycle](../../_static/images/github/github_doc_cycle2.png){ width=400px}

Changes to the original would be pulled down from the original repository to your GitHub website repository with a *Pull Request*.  You will then pull those changes to you local (PC) repository. You will push your changes to your GitHub website repository. Then create a *Pull Request* to send them to the original for review.

There are a number of possible ways to do this but the instructions below are reasonably simple and work:

After installing the required software (particularly **GitHub Desktop** and **VSCode**) ...

One time only:

1. Cloning the repository on the **GitHub website**
2. Using **GitHub Desktop** to download the repository to your PC

Ongoing:

3. Opening the repository in **VSCode**
4. Making your changes
5. Previewing your changes on your PC
6. Using **GitHub Desktop** to *push* your changes back to your clone of the Repository on GitHub
7. Creating a *pull request* to send your changes for review

You will periodically need to update your repository:

a. Create a pull request on the **GitHub website** to get any changes from the original repository to your repository on GitHub website
b. Use **GitHub Desktop** to pull the changes to your repository on your PC

----

### One time only

#### 1. Cloning the repository on GitHub website

1. First you will need to create an account on Github if you don't already have one.
2. Go to the original repository ``https://github.com/DCC-EX/mkdocs-test``
3. Click on the `Fork` button and create a new fork.  (Do not alter the Repository name ``mkdocs-test``.)

You will now have a new fork located at ``https://github.com/<your_account_name>/mkdocs-test``.  Take note of this for the next step.

#### 2. Download the repository to your PC with GitHib Desktop

In **GitHub Desktop**:

1. Select :menuselection:`File --> Clone Repository`
2. Enter the name of you repository ``<your_account_name>/mkdocs-test``
3. Select a location on your PC to store the repository.
4. Click :guilabel:`Clone`
5. Make sure that ``Sphinx`` is selected as the 'Current Branch'

A copy of the repository should now be on the PC.

You can open it in VSCode by selecting ``Repository -> Open in Visual Studio Code``

----

### Ongoing

#### 3. Open the repository in VSCode

You can open the repository in VSCode at any time by using `File --> Open Folder` and navigating to the folder you selected in step 2.

You can subsequently open the repository in VSCode using `File --> Open Recent` and selecting the repository name.

You can subsequently open the repository in VSCode from **GitHub Desktop**.

#### 4. Make your changes

You can use the navigation tree on the left to find the file you want to change. Clicking on a file will open it in the edit window.


For this section, we are assuming that you are using VSCode with Git installed, allowing the built-in functionality for Git management in VSCode to work.

To clone the documentation repository, and ensure you are on the correct branch, follow these steps:

1. In VSCode, either click on the Source Control icon in the left pane, or press <Ctrl> + <Shift> + "g" + "g" (Yes, press "g" twice).
2. Click the "Clone Repository" button.
3. Enter the documentation repository URL ``https://github.com/DCC-EX/mkdocs-test`` then press <Enter>.
4. Select the appropriate folder on your hard drive to clone it to, then click "Select Repository Location".
5. The clone will take a minute or two to complete depending on the speed of your computer and internet connection.
6. Once complete, click "Open".
7. At the bottom of the window, ensure that the branch "sphinx" is listed beside the Source Control icon.
8. When you're ready to start editing, click the Source Control or press <Ctrl> + <Shift> +"g" + "g" again.
9. Click the three dots "..." beside "SOURCE CONTROL" in bold text and select "Checkout to".
10. Enter a new name for your branch, then click "Create new branch".

At this point, any editing you do will be on a new branch linked to the parent "sphinx" branch.

While editing, be sure to save often, stage and commit your changes, and publish them. This way, should anything go wrong with your computer, your work will be saved in GitHub rather than be lost.

#### 5. Live previews

Providing you followed the installation guide for VSCode on the page accurately, there are several methods available for generating previews as you are editing the reStructuredText code.

==TODO== LOW - how to preview options

* In VSC, you can get a basic preview with the preview button (icon of two pages with a magnifying glass). Top right of the editing page.  This only shows basic formatting.

* You can push to your github repository and view the build (see below).

* On MS Windows you can use one of the `.bat` files to get a full preview:

    * local_build_for_win11.bat
    * local_dirty_build_for_win11.bat
    * local_serve_dirty_for_win11.bat
    * local_serve_for_win11.bat

``local_serve_for_win11.bat`` is the simplest and most accurate but is slow.

#### 6. Push your changes to your GitHub repository

You will need to:

* Commit your changes
* Push your changes

In **GitHub Desktop**:

1. Open/select the repository
2. note and review the changes that have been made
3. Add a ``Summary`` of your changes
4. Add a ``Description`` of your changes, if the summary is not sufficient
5. click `Commit to main`
6. click `Push origin`

#### 7. Creating a *pull request* to send your changes for review

1. Open the **GitHub website**
2. Open/select your repository ``https://github.com/<your_account_name>/dcc-ex.github.io``

On the 'code' page you should see "This branch is *x* commit(s) ahead of DCC-EX/dcc-ex.github.io:sphinx."

3. Click on the `x commit(s) ahead of` hyperlink
4. Confirm or add to the title and documentation fields
5. Click on the :guilabel:`Create pull request` button

This creates a pull request to be reviewed by the documentation team

----

### Periodic

To see the changes that other people have made to the original repository you need to periodically refresh your repository on both GitHub website and locally.

#### a. Get any changes to your repository on GitHub website

1. Open the **GitHub website**  
2. open/select your repository ``https://github.com/<your_account_name>/mkdocs-test``

On the 'code' page you should see "This branch is *x* commit(s) behind DCC-EX/mkdocs-test."

If does not say you are 'behind' there is nothing to do.  Stop here.

If you are behind...

3. Click on the `x commit(s) behind` hyperlink  
5. Add to the title and/or documentation fields.  This does not matter so entering just ``Catchup`` is fine.  
6. Click on the `Create pull request` button  
7. Click on the `Merge pull request` button  
8. Click on the `Confirm merge` button

Any changes are now also in your repository on the GitHub website.

#### b. Pull the changes to your repository on your PC

In **GitHub Desktop**:

1. Click on the `Fetch origin` button`

Any changes are now also in your repository on PC.

----

## Additional

### Your own github pages

You can, optionally, setup *github pages* from you own repository on the GitHub website.  This allows you to make changes that *other people* can view before creating a pull request.

1. Fork the "mkdocs-test" repository, ensure the ``Copy the main branch only`` box is selected.  
2. In your forked repository settings, navigate to Settings -> Actions -> General and ensure ``Allow all actions and reusable workflows`` is selected.  
3. Set up VSCode for your forked repository as outlined above.  
4. Create a new, orphaned branch called ``gh-pages`` using the command line; **you cannot do this in VSCode or in your browser**. Open a command prompt (or bash shell) and change into the directory containing your cloned fork then run the following commands:

```
  git checkout --orphan gh-pages
  # Use Windows Explorer, macOS Finder, or whatever method you prefer and delete all files and folders within the directory.
  # It must be completely empty aside from the hidden .git folder before proceeding.
  echo "My DCC-EX Documentation Fork" > index.html
  git add .
  git commit -a -m "First commit"
  git push origin gh-pages
```

5. At this point, review "Actions" in your forked repository and you should see the ``pages build and deployment`` job run, allowing you to preview the temporary "index.html" once complete.  
6. Review the Settings -> Pages tab and click the ``Visit site`` button to open your GitHub Pages generated content in a new browser tab, and you should see the basic "My DCC-EX Documentation Fork".  
7. If at this point in time the only action in the "Actions" tab is "pages-build-deployment", click the "..." beside the latest run and select ``Delete workflow run``.  
8. You should now see a big green button ``I understand my workflows, go ahead and enable them``. Click this button, which will show all the available actions as forked from the DCC-EX repository.  
9. Now, each time you commit and push to your fork's sphinx branch or merge a pull request to it, it should automatically build a new pages deployment and publish it.

Building the pages and deploying takes time, every time you push any changes, but you will eventually be able to see your own version of the website at ``https://<your_account_name>.github.io/makdocs-test/``.

You can see the state of the processing of your changes by looking at the ``Actions`` page.  It will also tell you there if there are any errors.
