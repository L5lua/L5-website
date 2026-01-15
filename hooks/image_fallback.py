import re
from pathlib import Path

def on_page_markdown(markdown, page, **kwargs):
    # Match markdown image syntax
    pattern = r'!\[(.*?)\]\((.*?\.webp)(?:\s+"(.*?)")?\)'
    
    def replace_with_picture(match):
        alt_text = match.group(1)
        webp_path = match.group(2)
        title = match.group(3) or ""
        
        # If it's already absolute or a URL, leave it alone
        if not webp_path.startswith('/') and not webp_path.startswith('http'):
            # Get the directory of the current page
            page_dir = Path(page.file.src_uri).parent
            # Make path absolute from site root
            webp_path = '/' + str(Path(page_dir) / webp_path)
        
        jpg_path = webp_path.replace('.webp', '.jpg')
        
        title_attr = f' title="{title}"' if title else ''
        
        return f'''<picture>
  <source srcset="{webp_path}" type="image/webp">
  <img src="{jpg_path}" alt="{alt_text}"{title_attr}>
</picture>'''
    
    return re.sub(pattern, replace_with_picture, markdown)
