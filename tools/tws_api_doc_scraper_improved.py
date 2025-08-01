#!/usr/bin/env python3
"""
Improved TWS API Documentation Scraper
Properly extracts all sections, subsections, and code samples for each H2
"""

import requests
import os
import time
from datetime import datetime
from bs4 import BeautifulSoup
import re

class ImprovedTWSScraper:
    def __init__(self, base_url="https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/"):
        self.base_url = base_url
        self.output_dir = "../docs/tws_api_docs"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Sec-CH-UA': '"Google Chrome";v="137", "Chromium";v="137", "Not;A=Brand";v="99"',
            'Sec-CH-UA-Mobile': '?0',
            'Sec-CH-UA-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'Priority': 'u=0, i'
        }
        
    def download_page(self):
        """Download the main documentation page"""
        print(f"Downloading page from {self.base_url}...")
        try:
            response = requests.get(self.base_url, headers=self.headers, timeout=30)
            response.raise_for_status()
            print(f"Page downloaded successfully ({len(response.content):,} bytes)")
            return response.text
        except Exception as e:
            print(f"Error downloading page: {e}")
            return None
    
    def get_section_mapping(self, soup):
        """Map section elements to their H2 parents"""
        content_div = soup.find('div', id='sidemenu-content')
        if not content_div:
            print("Could not find div#sidemenu-content")
            return {}
        
        # Get all H2 elements and section elements
        h2_elements = content_div.find_all('h2')
        all_sections = content_div.find_all('section')
        
        print(f"Found {len(h2_elements)} H2 elements and {len(all_sections)} section elements")
        
        # Create mapping from navigation to understand relationships
        nav = soup.find('nav', id='sidemenu-nav')
        level1_nav_ids = []
        if nav:
            navbar_side = nav.find('ul', id='navbar-side')
            if navbar_side:
                for li in navbar_side.find_all('li', class_='nav-item-side', recursive=False):
                    if 'menu-level-1' in li.get('class', []):
                        link = li.find('a')
                        if link and link.get('href'):
                            section_id = link['href'].lstrip('#')
                            level1_nav_ids.append(section_id)
        
        # Map sections to H2s
        section_mapping = {}
        
        for i, h2 in enumerate(h2_elements):
            h2_title = h2.get_text(strip=True)
            h2_title = re.sub(r'Copy Location$', '', h2_title).strip()
            
            # Find the corresponding level 1 nav ID
            h2_nav_id = level1_nav_ids[i] if i < len(level1_nav_ids) else None
            
            # Collect all sections that belong to this H2
            related_sections = []
            
            if h2_nav_id:
                # Find sections that belong to this level 1 section
                capturing = False
                for section in all_sections:
                    section_id = section.get('id', '')
                    
                    # Start capturing when we hit the main section
                    if section_id == h2_nav_id:
                        capturing = True
                        related_sections.append(section)
                        continue
                    
                    # Stop capturing when we hit the next level 1 section
                    if capturing and section_id in level1_nav_ids and section_id != h2_nav_id:
                        break
                    
                    # Capture sections while we're in the right region
                    if capturing:
                        related_sections.append(section)
            
            section_mapping[h2] = {
                'title': h2_title,
                'nav_id': h2_nav_id,
                'sections': related_sections
            }
            
            print(f"  {i+1}. {h2_title} -> {len(related_sections)} sections")
        
        return section_mapping
    
    def extract_code_samples(self, element):
        """Extract Python code samples from various code structures"""
        code_samples = []
        
        # 1. Look for EnlighterJSRAW pre elements (most common)
        enlighter_pres = element.find_all('pre', class_='EnlighterJSRAW')
        for pre in enlighter_pres:
            code_text = pre.get_text()
            if code_text.strip():
                # Filter for Python code only
                if ('def ' in code_text or 'self.' in code_text or 'import ' in code_text or 
                    code_text.strip().startswith('self.') or
                    ('print(' in code_text and not 'System.out.println' in code_text and not 'Console.WriteLine' in code_text)):
                    code_samples.append(f"```python\n{code_text.strip()}\n```")
        
        # 2. Look for enlighter-code divs (backup)
        code_blocks = element.find_all('div', class_='enlighter-code')
        for code_block in code_blocks:
            raw_div = code_block.find('div', class_='enlighter-raw')
            if raw_div:
                code_text = raw_div.get_text()
                if code_text.strip() and ('def ' in code_text or 'self.' in code_text):
                    code_samples.append(f"```python\n{code_text.strip()}\n```")
        
        # 3. Look for table cells that contain Python code (backup)
        tables = element.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for i, row in enumerate(rows):
                cells = row.find_all(['td', 'th'])
                if len(cells) > 1:
                    for cell in cells:
                        cell_text = cell.get_text()
                        if (('def ' in cell_text or cell_text.strip().startswith('self.')) and 
                            'self' in cell_text and not 'System.out' in cell_text):
                            # This looks like Python code
                            code_samples.append(f"```python\n{cell_text.strip()}\n```")
                            break
        
        return code_samples
    
    def convert_section_to_markdown(self, section):
        """Convert a section element to clean markdown"""
        if not section:
            return ""
        
        # Make a copy to avoid modifying the original
        section_copy = BeautifulSoup(str(section), 'html.parser')
        
        # Extract code samples first (and remove them from processing)
        code_samples = self.extract_code_samples(section_copy)
        
        # Remove code elements so they don't interfere with text processing
        for pre in section_copy.find_all('pre', class_='EnlighterJSRAW'):
            pre.decompose()
        
        # Remove script, style, nav elements
        for unwanted in section_copy(['script', 'style', 'nav']):
            unwanted.decompose()
        
        # Process the structured content
        content_parts = []
        
        # Look for h2, h3, h4 headers and their associated content
        for header in section_copy.find_all(['h2', 'h3', 'h4']):
            header_text = header.get_text(strip=True)
            header_text = re.sub(r'Copy Location$', '', header_text).strip()
            
            if header_text:
                # Add the header with appropriate markdown level
                level = int(header.name[1])
                if level == 2:
                    content_parts.append(f"## {header_text}")
                elif level == 3:
                    content_parts.append(f"### {header_text}")
                else:
                    content_parts.append(f"#### {header_text}")
                
                # Find the content that follows this header
                # Look for the parent section's content
                parent_section = header.find_parent('section')
                if parent_section:
                    # Find all content divs within this section
                    content_divs = parent_section.find_all('div', class_=['row', 'entry-content', 'col-12'])
                    
                    for content_div in content_divs:
                        # Skip if this div contains the header we just processed
                        if header in content_div.find_all(['h2', 'h3', 'h4']):
                            continue
                            
                        # Extract text content, focusing on paragraphs
                        content_text = ""
                        
                        # Process paragraphs, lists, and other content elements
                        for element in content_div.find_all(['p', 'h4', 'h5', 'ul', 'ol', 'div']):
                            # Skip divs that contain code tabs
                            if element.name == 'div' and any(tab_class in element.get('class', []) for tab_class in ['tab-content', 'nav-tabs', 'tab-pane']):
                                continue
                                
                            elem_text = element.get_text(strip=True)
                            elem_text = re.sub(r'Copy Location$', '', elem_text).strip()
                            
                            # Skip language selection text
                            if re.match(r'^Python\s*Java\s*C\+\+\s*C#\s*VB\.NET', elem_text):
                                continue
                            
                            if elem_text and len(elem_text) > 5:  # Only substantial content
                                if element.name in ['h4', 'h5']:
                                    content_text += f"\n\n#### {elem_text}\n"
                                elif element.name == 'p':
                                    content_text += f"\n{elem_text}"
                                elif element.name in ['ul', 'ol']:
                                    content_text += f"\n{elem_text}"
                                elif element.name == 'div' and not element.find(['p', 'h4', 'h5']):
                                    # Simple div with just text
                                    content_text += f"\n{elem_text}"
                        
                        if content_text.strip():
                            content_parts.append(content_text.strip())
        
        # If no structured content found, fall back to simple text extraction
        if len(content_parts) <= 1:  # Only headers, no content
            text = section_copy.get_text()
            text = re.sub(r'Copy Location', '', text)
            text = re.sub(r'Python\s*Java\s*C\+\+\s*C#\s*VB\.NET.*?(?=\n|$)', '', text, flags=re.MULTILINE | re.DOTALL)
            text = re.sub(r'PythonJavaC\+\+C#VB\.NET.*?(?=\n|$)', '', text, flags=re.MULTILINE | re.DOTALL)
            
            # Clean up and structure the text
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            if lines:
                # Group lines into paragraphs
                paragraphs = []
                current_para = []
                
                for line in lines:
                    if (line.startswith('#') or line.isupper() or line.endswith(':') or 
                        line.startswith('Note:') or line.startswith('Important:')):
                        if current_para:
                            paragraphs.append(' '.join(current_para))
                            current_para = []
                        paragraphs.append(line)
                    else:
                        current_para.append(line)
                
                if current_para:
                    paragraphs.append(' '.join(current_para))
                
                content_parts.extend(paragraphs)
        
        # Join all content parts
        markdown_text = '\n\n'.join(part for part in content_parts if part.strip())
        
        # Clean up whitespace
        markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
        markdown_text = re.sub(r'[ \t]+', ' ', markdown_text)  # Clean up spaces
        
        # Add code samples at the end if any were found
        if code_samples:
            markdown_text += '\n\n' + '\n\n'.join(code_samples)
        
        return markdown_text.strip()
    
    def create_section_markdown(self, h2, section_data):
        """Create complete markdown for a section"""
        content_parts = []
        
        # Process each section element
        for section in section_data['sections']:
            section_markdown = self.convert_section_to_markdown(section)
            if section_markdown.strip():
                content_parts.append(section_markdown)
        
        return '\n\n'.join(content_parts)
    
    def save_section(self, h2, section_data, content):
        """Save a section to a markdown file"""
        if not content.strip():
            print(f"Skipping empty section: {section_data['title']}")
            return False
        
        # Create safe filename
        safe_title = re.sub(r'[^\w\s-]', '', section_data['title'])
        safe_title = re.sub(r'[-\s]+', '_', safe_title).lower()
        safe_title = safe_title[:50]
        filename = f"{safe_title}.md"
        filepath = os.path.join(self.output_dir, filename)
        
        # Count content metrics
        word_count = len(content.split())
        para_count = content.count('\n\n') + 1
        subsection_count = len(section_data['sections'])
        code_block_count = content.count('```python')
        
        # Create YAML frontmatter
        frontmatter = f"""---
title: "{section_data['title']}"
description: "TWS API Documentation - {section_data['title']}"
source: "Interactive Brokers TWS API Documentation"
nav_id: "{section_data['nav_id']}"
scraped_at: "{datetime.now().isoformat()}"
word_count: {word_count}
paragraph_count: {para_count}
subsection_count: {subsection_count}
code_block_count: {code_block_count}
format: "markdown"
---

"""
        
        # Write the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write(f"# {section_data['title']}\n\n")
            f.write(content)
        
        print(f"Saved: {filename} ({word_count:,} words, {subsection_count} subsections, {code_block_count} code blocks)")
        return True
    
    def create_readme(self, sections_created):
        """Create a README file with the section listing"""
        readme_path = os.path.join(self.output_dir, "README.md")
        
        total_words = sum(s['word_count'] for s in sections_created)
        total_subsections = sum(s['subsection_count'] for s in sections_created)
        total_code_blocks = sum(s['code_block_count'] for s in sections_created)
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# TWS API Documentation - Improved Structure\n\n")
            f.write(f"Documentation scraped from Interactive Brokers TWS API on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Total Level 1 sections:** {len(sections_created)}\n")
            f.write(f"**Total subsections:** {total_subsections}\n")
            f.write(f"**Total words:** {total_words:,}\n")
            f.write(f"**Total code blocks:** {total_code_blocks}\n\n")
            f.write("## Level 1 Sections\n\n")
            
            for i, section in enumerate(sections_created, 1):
                f.write(f"{i}. **{section['title']}** (`{section['filename']}`)\n")
                f.write(f"   - Word count: {section['word_count']:,}\n")
                f.write(f"   - Subsections: {section['subsection_count']}\n")
                f.write(f"   - Code blocks: {section['code_block_count']}\n\n")
    
    def scrape(self):
        """Main scraping method"""
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Download the page
        html_content = self.download_page()
        if not html_content:
            return
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Get section mapping
        section_mapping = self.get_section_mapping(soup)
        if not section_mapping:
            print("No sections found!")
            return
        
        sections_created = []
        
        # Process each H2 section
        for i, (h2, section_data) in enumerate(section_mapping.items()):
            print(f"\nProcessing section {i+1}/{len(section_mapping)}: {section_data['title']}")
            
            # Create markdown content
            content = self.create_section_markdown(h2, section_data)
            
            # Save the section
            if self.save_section(h2, section_data, content):
                # Track for README
                safe_title = re.sub(r'[^\w\s-]', '', section_data['title'])
                safe_title = re.sub(r'[-\s]+', '_', safe_title).lower()
                safe_title = safe_title[:50]
                filename = f"{safe_title}.md"
                
                word_count = len(content.split())
                subsection_count = len(section_data['sections'])
                code_block_count = content.count('```python')
                
                sections_created.append({
                    'title': section_data['title'],
                    'filename': filename,
                    'word_count': word_count,
                    'subsection_count': subsection_count,
                    'code_block_count': code_block_count
                })
            
            # Small delay
            time.sleep(0.1)
        
        # Create README
        self.create_readme(sections_created)
        
        print(f"\nScraping completed!")
        print(f"Created {len(sections_created)} section files in '{self.output_dir}' directory")
        print(f"Total words scraped: {sum(s['word_count'] for s in sections_created):,}")
        print(f"Total subsections: {sum(s['subsection_count'] for s in sections_created)}")
        print(f"Total code blocks: {sum(s['code_block_count'] for s in sections_created)}")

if __name__ == "__main__":
    scraper = ImprovedTWSScraper()
    scraper.scrape()
