import os
import re
from mkdocs.structure.nav import Navigation, Section, Page

def on_nav(nav: Navigation, config, files) -> Navigation:
    docs_dir = config["docs_dir"]
    output_dir = os.path.join(docs_dir, "reference")
    os.makedirs(output_dir, exist_ok=True)
    toc_path = os.path.join(output_dir, "toc.md")
    toc_src_path = os.path.relpath(toc_path, docs_dir).replace(os.path.sep, "/")
    
    toc_lines = ["# Full Site Table of Contents\n\n" + 
"<style>\n" +
"li:not(.md-nav__item, .md-tabs__item) {\n" +
"    margin: 0px;\n" +
"    border: 0px;\n" +
"    line-height: 100%;\n" +
"    margin-bottom: 4px !important;\n" +
"}\n" +
"li:not(.md-nav__item, .md-tabs__item) a {\n" +
"    font-weight: 500;\n" +
"    font-size: 85%;\n" +
"}\n" +
"</style>\n\n" +
"## Indexed Pages\n\n"]

    # Helper function to find the first H1 in a markdown file
    def get_h1_title(file_path):
        if not os.path.exists(file_path):
            return None
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    # Strip whitespace and check if it starts with a single '#'
                    cleaned = line.strip()
                    if cleaned.startswith("#") and not cleaned.startswith("##"):
                        # Extract the text and remove any trailing '#' or spaces
                        h1_text = cleaned.lstrip("#").strip()
                        return h1_text
        except Exception:
            pass
        return None

    def build_relative_link(src_path):
        target_path = os.path.join(docs_dir, src_path)
        return os.path.relpath(target_path, start=output_dir).replace(os.path.sep, "/")

    # Define a recursive loop to travel through awesome-nav's compiled classes
    def parse_nav_object(nav_item, depth=0):
        indent = "    " * depth
        
        # Case A: It's a Section (a folder / dropdown category compiled by awesome-nav)
        if isinstance(nav_item, Section):
            # Skip compiling this section if it belongs to your _static folder
            if nav_item.title and "_static" in nav_item.title.lower():
                return
                
            if nav_item.title:
                toc_lines.append(f"{indent}- **{nav_item.title}**")
                
            # Dive down sequentially into this section's children items
            for child in nav_item.children:
                parse_nav_object(child, depth + 1)
                
        # Case B: It's a concrete Markdown Page
        elif isinstance(nav_item, Page):
            # Explicitly exclude the generated TOC from its own listings
            if nav_item.file.src_path in {"toc.md", toc_src_path}:
                return
                
            # awesome-nav automatically resolves the cleanest title 
            title = nav_item.title or "Untitled"
            
            # Extract standard, web-safe relative URLs for proper rendering links
            url_path = nav_item.file.src_path
            
            # Look up the actual H1 heading inside the file
            full_file_path = os.path.join(docs_dir, url_path)
            h1_heading = get_h1_title(full_file_path)
            
            # Append H1 title if it exists and differs from the nav link title
            if h1_heading and h1_heading.lower() != title.lower():
                if title != "Untitled":
                    # display_title = f"{title} — *{h1_heading}*"
                    display_title = f"{h1_heading} <small>({title})</small>"
                else:
                    # display_title = f"*{h1_heading}*"
                    display_title = f"{h1_heading}"
            else:
                display_title = title

            toc_lines.append(f"{indent}- [{display_title}]({build_relative_link(url_path)})")

    # Cycle sequentially through awesome-nav's resolved root order
    for item in nav.items:
        parse_nav_object(item)
        
    # Add a separate section for files that are intentionally not in nav
    non_nav_files = []
    for root, _, filenames in os.walk(docs_dir):
        for filename in filenames:
            if filename.endswith("_not_in_nav.md"):
                file_path = os.path.join(root, filename)
                rel_path = os.path.relpath(file_path, docs_dir).replace(os.path.sep, "/")
                non_nav_files.append(rel_path)

    if non_nav_files:
        toc_lines.append("\n## Pages Not In Navigation\n")
        non_nav_items = []
        for rel_path in non_nav_files:
            full_file_path = os.path.join(docs_dir, rel_path)
            title = get_h1_title(full_file_path) or os.path.basename(rel_path)
            non_nav_items.append((title.lower(), title, rel_path))

        for _, title, rel_path in sorted(non_nav_items, key=lambda item: item[0]):
            toc_lines.append(f"- [{title}]({build_relative_link(rel_path)})")

    # Physically save the table of contents 
    with open(toc_path, "w", encoding="utf-8") as f:
        f.write("\n".join(toc_lines))
        
    return nav