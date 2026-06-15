import os
from mkdocs.structure.nav import Navigation, Section, Page

def on_nav(nav: Navigation, config, files) -> Navigation:
    docs_dir = config["docs_dir"]
    toc_path = os.path.join(docs_dir, "toc.md")
    
    toc_lines = ["# Table of Contents\n\n" + 
"<style>\n" +
"li {\n" +
"    margin: 0px;\n" +
"    border: 0px;\n" +
"    line-height: 100%;\n" +
"}\n" +
"li a {\n" +
"    font-weight: 300;\n" +
"}\n" +
"</style>\n\n"]


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
            if nav_item.file.src_path == "toc.md":
                return
                
            # awesome-nav automatically resolves the cleanest title 
            # (checks front-matter, file name, or custom nav overrides)
            title = nav_item.title or "Untitled"
            
            # Extract standard, web-safe relative URLs for proper rendering links
            url_path = nav_item.file.src_path
            
            toc_lines.append(f"{indent}- [{title}]({url_path})")

    # Cycle sequentially through awesome-nav's resolved root order
    for item in nav.items:
        parse_nav_object(item)
        
    # Physically save the table of contents 
    with open(toc_path, "w", encoding="utf-8") as f:
        f.write("\n".join(toc_lines))
        
    return nav
