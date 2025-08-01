#!/usr/bin/env python3
"""
Generic IBKR Campus Documentation Scraper
Handles any IBKR Campus page with the standard TOC + content structure
Enhanced with section ordering and navigation metadata
"""

import requests
from bs4 import BeautifulSoup
import os
import re
import time
import random
from datetime import datetime

# Simple inline configurations
CONFIGS = {
    'docs': {
        'url': 'https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/',
        'output_dir': '../docs/tws_api_docs',
        'page_name': 'TWS API Documentation'
    },
    'reference': {
        'url': 'https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-ref/',
        'output_dir': '../docs/tws_api_reference', 
        'page_name': 'TWS API Reference'
    }
}

class IBKRCampusScraper:
    """Generic scraper for IBKR Campus documentation with enhanced ordering"""
    
    def __init__(self, config_name):
        if config_name not in CONFIGS:
            raise ValueError(f"Unknown config: {config_name}. Available: {list(CONFIGS.keys())}")
        
        self.config = CONFIGS[config_name]
        self.base_url = self.config['url']
        self.output_dir = self.config['output_dir']
        self.page_name = self.config['page_name']
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
    def clean_filename(self, text):
        """Clean text for use as filename"""
        # Remove "Copy Location" and clean up
        text = re.sub(r'\s*copy\s*location\s*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'[^\w\s-]', '', text.strip())
        text = re.sub(r'\s+', '_', text)
        return text.lower()
    
    def convert_table_to_markdown(self, table):
        """Convert HTML table to markdown format"""
        rows = table.find_all('tr')
        if not rows:
            return ""
        
        markdown_lines = []
        
        # Process header row
        header_row = rows[0]
        headers = []
        for cell in header_row.find_all(['th', 'td']):
            headers.append(cell.get_text(strip=True))
        
        if headers:
            markdown_lines.append('| ' + ' | '.join(headers) + ' |')
            markdown_lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
        
        # Process data rows
        for row in rows[1:]:
            cells = []
            for cell in row.find_all(['th', 'td']):
                cell_text = cell.get_text(strip=True)
                # Escape markdown characters in cell content
                cell_text = cell_text.replace('|', '\\|')
                cells.append(cell_text)
            
            if cells:
                markdown_lines.append('| ' + ' | '.join(cells) + ' |')
        
        return '\n'.join(markdown_lines)
    
    def convert_section_to_markdown(self, section, section_title):
        """Convert a section to markdown with enhanced table support"""
        lines = []
        lines.append(f"# {section_title}\n")
        
        # Process all elements in the section
        for element in section.children:
            if element.name == 'h3':
                lines.append(f"## {element.get_text(strip=True)}\n")
            elif element.name == 'h4':
                lines.append(f"### {element.get_text(strip=True)}\n")
            elif element.name == 'h5':
                lines.append(f"#### {element.get_text(strip=True)}\n")
            elif element.name == 'p':
                text = element.get_text(strip=True)
                if text:
                    lines.append(f"{text}\n")
            elif element.name == 'ul':
                for li in element.find_all('li', recursive=False):
                    lines.append(f"- {li.get_text(strip=True)}")
                lines.append("")
            elif element.name == 'ol':
                for i, li in enumerate(element.find_all('li', recursive=False), 1):
                    lines.append(f"{i}. {li.get_text(strip=True)}")
                lines.append("")
            elif element.name == 'table':
                # Convert table to markdown
                table_markdown = self.convert_table_to_markdown(element)
                if table_markdown:
                    lines.append(table_markdown)
                    lines.append("")
            elif element.name == 'pre':
                # Code blocks
                code_text = element.get_text()
                lines.append("```")
                lines.append(code_text)
                lines.append("```\n")
            elif element.name == 'div' and 'code-sample' in element.get('class', []):
                # Handle code sample divs
                code_text = element.get_text(strip=True)
                if code_text:
                    lines.append("```")
                    lines.append(code_text)
                    lines.append("```\n")
        
        return '\n'.join(lines)
    
    def get_navigation_structure(self, soup):
        """Extract navigation structure for section ordering"""
        nav_structure = []
        
        # Look for navigation in sidemenu
        sidemenu = soup.find('div', id='sidemenu-content')
        if sidemenu:
            # Find all navigation links
            nav_links = sidemenu.find_all('a', href=True)
            for i, link in enumerate(nav_links, 1):
                href = link['href']
                title = link.get_text(strip=True)
                if href.startswith('#') and title:
                    nav_structure.append({
                        'order': i,
                        'href': href,
                        'title': title
                    })
        
        return nav_structure
    
    def scrape_documentation(self):
        """Main scraping method with enhanced ordering"""
        print(f"🔍 Scraping {self.page_name}...")
        print(f"📍 URL: {self.base_url}")
        print(f"📁 Output: {self.output_dir}")
        
        # Get the page
        response = requests.get(self.base_url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get navigation structure for ordering
        nav_structure = self.get_navigation_structure(soup)
        print(f"📋 Found {len(nav_structure)} sections in navigation")
        
        # Find main content area
        content_div = soup.find('div', id='sidemenu-content')
        if not content_div:
            raise ValueError("Could not find main content div")
        
        # Find all H2 sections
        h2_sections = content_div.find_all('h2')
        print(f"📄 Found {len(h2_sections)} H2 sections")
        
        # Create section mapping for ordering
        section_map = {}
        for nav_item in nav_structure:
            section_map[nav_item['href']] = nav_item
        
        processed_sections = []
        
        for h2 in h2_sections:
            section_title = h2.get_text(strip=True)
            
            # Find corresponding navigation item
            nav_item = None
            for item in nav_structure:
                if item['title'].lower() == section_title.lower():
                    nav_item = item
                    break
            
            if not nav_item:
                # Create a default nav item if not found
                nav_item = {
                    'order': len(processed_sections) + 1,
                    'title': section_title
                }
            
            # Collect section content
            section_content = []
            current = h2.next_sibling
            
            while current and (not current.name or current.name != 'h2'):
                if current.name:
                    section_content.append(current)
                current = current.next_sibling
            
            # Create a pseudo-section for processing
            section_div = soup.new_tag('div')
            for content in section_content:
                section_div.append(content.extract())
            
            # Convert to markdown
            markdown_content = self.convert_section_to_markdown(section_div, section_title)
            
            # Clean filename
            clean_title = self.clean_filename(section_title)
            filename = f"{nav_item['order']:02d}_{clean_title}.md"
            
            # Add frontmatter
            frontmatter = f"""---
order: {nav_item['order']}
title: "{section_title}"
section: "{clean_title}"
nav_title: "{nav_item['title']}"
scraped_at: "{datetime.now().isoformat()}"
---

"""
            
            full_content = frontmatter + markdown_content
            
            # Write file
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            processed_sections.append({
                'order': nav_item['order'],
                'title': section_title,
                'filename': filename,
                'word_count': len(markdown_content.split())
            })
            
            print(f"✅ {filename} ({len(markdown_content.split())} words)")
            
            # Be polite
            time.sleep(random.uniform(0.5, 1.5))
        
        # Sort by order for summary
        processed_sections.sort(key=lambda x: x['order'])
        
        # Create README with ordered index
        self.create_readme(processed_sections)
        
        total_words = sum(section['word_count'] for section in processed_sections)
        print(f"\n🎉 Completed! {len(processed_sections)} sections, {total_words:,} words total")
        
        return processed_sections
    
    def create_readme(self, sections):
        """Create README with ordered index"""
        readme_content = f"""# {self.page_name}

Scraped from: {self.base_url}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Table of Contents

"""
        
        for section in sections:
            readme_content += f"{section['order']:2d}. [{section['title']}]({section['filename']}) ({section['word_count']:,} words)\n"
        
        readme_content += f"\n**Total: {sum(s['word_count'] for s in sections):,} words across {len(sections)} sections**\n"
        
        readme_path = os.path.join(self.output_dir, 'README.md')
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"📄 Created {readme_path}")

def main():
    """Main function with config selection"""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python ibkr_campus_scraper.py <config_name>")
        print(f"Available configs: {list(CONFIGS.keys())}")
        sys.exit(1)
    
    config_name = sys.argv[1]
    
    try:
        scraper = IBKRCampusScraper(config_name)
        scraper.scrape_documentation()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
