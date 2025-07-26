"""
This plugin is used to grab the latest DCC-EX news article titles to be displayed.

These are used to create an unordered list which can be used in markdown files.

To include it in a file, include this text on its own line with a blank line above and below:

<!-- LATEST-NEWS -->

NOTE: You may need to indent this line to suit the nesting of lists etc.

This is included as a plugin in mkdocs.yml:

plugins:
  - latest-news

By default, the latest 2 articles are included, this can be changed with:

plugins:
  - latest-news:
      count: 3

To customise the list styling, either create the default class "news-list" or define your own:

plugins:
  - latest-news:
      list-class: my-list-class


To ensure your CSS class correctly overrides MkDocs Material classes, make it specific, eg:

.md-typeset li.news-headline-list {
  font-family: Audiowide,Helvetica,Arial,sans-serif;
  list-style: none;
  padding-left: 0;
  margin-left: 0 !important;
}
"""

from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from mkdocs.config import Config, config_options
import frontmatter
from datetime import datetime
import os


class LatestNewsPlugin(BasePlugin):
    """
    Extends the MkDocs BasePlugin to created the LatestNewsPlugin.

    Include as a plugin in mkdocs.yml:

    plugins:
      - latest-news

    By default, the latest 2 articles are included, this can be changed with:

    plugins:
      - latest-news:
          count: 3

    To customise the list styling, either create the default class "news-list" or define your own:

    plugins:
      - latest-news:
          list-class: my-list-class
    """
    # Allow mkdocs.yml configuration of the number of articles, default is 2
    config_scheme = (
        ('count', config_options.Type(int, default=2)),
        ('list-class', config_options.Type(str, default='news-list')),
    )

    def on_page_markdown(self, markdown: str, page: Page, config: Config, files: Files) -> str:
        """
        Modifies the markdown of the provided page to replace it with the latest news article titles.

        The latest articles are determined from the timestamp in the article's front matter.

        This looks for the comment <!-- LATEST-NEWS --> and replaces it with the article titles as an unordered list.

        Parameters:
            markdown (str): Source page's markdown as a string.
            page (Page): Source page object.
            config (Config): MkDocs global configuration.
            files (Files): MkDocs global files collection.

        Returns:
            markdown (str): The modified markdown as a string.
        """
        # If <!-- LATEST-NEWS --> not in markdown, skip it
        if "<!-- LATEST-NEWS -->" not in markdown:
            return markdown

        # Set up local variables from the global config and plugin config
        news_dir = os.path.join(config["docs_dir"], "news", "articles")
        article_count = self.config.get('count')
        list_class = self.config.get('list-class')
        posts = []

        # Iterate through the files in the news directory
        for filename in os.listdir(news_dir):
            if filename.endswith(".md"):
                with open(os.path.join(news_dir, filename), encoding="utf-8") as f:
                    post = frontmatter.load(f)
                    content = post.content
                    metadata = post.metadata
                    # print(metadata)

                    title = self.extract_title(content)
                    excerpt = self.extract_excerpt(content)
                    date = metadata.get('date')
                    draft = metadata.get('draft')
                    # Don't include drafts
                    if draft is True:
                        continue

                    if date:
                        posts.append({
                            "title": title,
                            "excerpt": excerpt,
                            "date": date if isinstance(date, datetime) else datetime.combine(date, datetime.min.time())
                        })
                        # print(title)

        # Sort by date, latest first
        posts.sort(key=lambda x: x["date"], reverse=True)
        latest_posts = posts[:article_count]

        # Build Markdown block
        news_block = ""
        for post in latest_posts:
            news_block += f"- :material-newspaper: {post['title']}\n"
            news_block += f"{{ .{list_class} }}\n"
        # print(news_block)

        # Inject at placeholder
        return markdown.replace("<!-- LATEST-NEWS -->", news_block)

    def extract_title(self, content: str) -> str:
        """
        Extract the title from the provided string using the page's top level heading.

        Parameters:
            content (str): The content to extract the title from.

        Returns:
            str: The extracted title as a string.
        """
        for line in content.splitlines():
            if line.startswith('# '):
                return line.lstrip('# ').strip()
        return "Untitled"

    def extract_excerpt(self, content: str) -> str:
        """
        Extracts the excerpt to use for the news article.

        If present, everything before <!-- more --> is returned.

        Alternatively, the first paragraph is returned.

        Parameters:
            content (str): The content to extract the excerpt from.

        Returns:
            str: The extracted excerpt.
        """
        if ('<!-- more -->') in content:
            return content.split('<!-- more -->')[0].strip()

        lines = content.splitlines()
        paragraph = []
        for line in lines:
            if line.strip() == "":
                if paragraph:
                    break
                continue
            if line.startswith("#") or line.startswith(":::") or line.startswith("```"):
                continue
            paragraph.append(line.strip())
        return " ".join(paragraph)
