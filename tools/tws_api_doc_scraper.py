import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import os
import re

BASE_URL = "https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/"
HEADERS = {"User-Agent": "Mozilla/5.0"}  # Polite scraping!
OUTPUT_DIR = "../docs/tws_api_docs"

def create_safe_filename(url, base_url):
    """Create a safe filename from URL"""
    # Remove the base URL to get the relative path
    if url.startswith(base_url):
        relative_path = url[len(base_url):].strip('/')
    else:
        relative_path = urlparse(url).path.strip('/')
    
    # Replace special characters with underscores
    safe_name = re.sub(r'[^\w\-_./]', '_', relative_path)
    # Replace multiple underscores with single ones
    safe_name = re.sub(r'_+', '_', safe_name)
    # Remove leading/trailing underscores
    safe_name = safe_name.strip('_')
    
    # If empty or just slashes, use index
    if not safe_name or safe_name == '/':
        safe_name = 'index'
    
    # Add .txt extension if not present
    if not safe_name.endswith('.txt'):
        safe_name += '.txt'
    
    return safe_name

def save_page_content(content_data, base_url, output_dir):
    """Save scraped content to file"""
    url = content_data['url']
    content = content_data['content']
    
    # Create safe filename
    filename = create_safe_filename(url, base_url)
    filepath = os.path.join(output_dir, filename)
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # If the filename contains subdirectories, create them too
    file_dir = os.path.dirname(filepath)
    if file_dir and file_dir != output_dir:
        os.makedirs(file_dir, exist_ok=True)
    
    # Write content to file (overwrites if exists)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Scraped on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(content)
        print(f"Saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"Failed to save {filepath}: {e}")
        return None

def extract_sections_from_page(soup, base_url):
    """Extract individual sections from a single-page documentation site"""
    sections = []
    
    # Find all elements with IDs that match the navigation anchors
    nav = soup.select_one('nav')
    if nav:
        anchor_links = [a['href'][1:] for a in nav.find_all('a', href=True) 
                       if a['href'].startswith('#')]
        print(f"Found {len(anchor_links)} sections to extract")
        
        for anchor_id in anchor_links:  # Process all sections
            # Find the element with this ID
            section_element = soup.find(id=anchor_id)
            if section_element:
                # Extract content from this section
                section_content = extract_section_content(section_element, soup)
                if section_content:
                    sections.append({
                        'id': anchor_id,
                        'url': f"{base_url}#{anchor_id}",
                        'content': section_content
                    })
                    print(f"Extracted section: {anchor_id}")
    
    return sections

def extract_section_content(start_element, soup):
    """Extract content from a section starting at the given element"""
    content = []
    
    # Get the section title
    if start_element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        content.append(f"\n--- {start_element.get_text(strip=True)} ---\n")
        current = start_element.next_sibling
    else:
        content.append(f"\n--- {start_element.get('id', 'Section')} ---\n")
        current = start_element
    
    # Collect content until we hit the next section heading or run out
    while current:
        if hasattr(current, 'name'):
            if current.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] and current != start_element:
                # Stop at next heading
                break
            elif current.name == 'p':
                text = current.get_text(separator=' ', strip=True)
                if text:
                    content.append(text)
            elif current.name in ['pre', 'code']:
                code_text = current.get_text(strip=True)
                if code_text:
                    content.append(f"\n```\n{code_text}\n```\n")
            elif current.name in ['ul', 'ol']:
                # Extract list items
                for li in current.find_all('li'):
                    item_text = li.get_text(strip=True)
                    if item_text:
                        content.append(f"• {item_text}")
        
        current = current.next_sibling
    
    return '\n'.join(content) if content else None

def save_section_content(section_data, output_dir):
    """Save section content to file"""
    section_id = section_data['id']
    url = section_data['url']
    content = section_data['content']
    
    # Create safe filename from section ID
    safe_name = re.sub(r'[^\w\-_]', '_', section_id)
    safe_name = re.sub(r'_+', '_', safe_name).strip('_')
    filename = f"{safe_name}.txt"
    filepath = os.path.join(output_dir, filename)
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Write content to file (overwrites if exists)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Section ID: {section_id}\n")
            f.write(f"Scraped on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(content)
        print(f"Saved section: {filepath}")
        return filepath
    except Exception as e:
        print(f"Failed to save {filepath}: {e}")
        return None

def scrape_page(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # Main content preference, fallback to body
        main = soup.find('main') or soup.body
        # Extract headings, text, code blocks
        result = []
        if main:
            for heading in main.find_all(['h1', 'h2', 'h3', 'h4']):
                result.append(f"\n--- {heading.get_text(strip=True)} ---\n")
            for para in main.find_all('p'):
                result.append(para.get_text(separator=' ', strip=True))
            for code in main.find_all(['pre', 'code']):
                code_text = code.get_text(strip=True)
                if code_text:
                    result.append(f"\n```\n{code_text}\n```\n")
        return {'url': url, 'content': '\n'.join(result)}
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return {'url': url, 'content': ''}

def main():
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {os.path.abspath(OUTPUT_DIR)}")
    
    print("Fetching main documentation page...")
    # Get the main page
    base_resp = requests.get(BASE_URL, headers=HEADERS, timeout=15)
    base_resp.raise_for_status()
    base_soup = BeautifulSoup(base_resp.text, "html.parser")

    # First, save the complete page as index.txt
    main_page_result = scrape_page(BASE_URL)
    if main_page_result['content']:
        save_page_content(main_page_result, BASE_URL, OUTPUT_DIR)
    
    # Then extract individual sections
    print("Extracting individual sections...")
    sections = extract_sections_from_page(base_soup, BASE_URL)
    print(f"Found {len(sections)} sections to save.")
    
    # Save each section to its own file
    saved_files = [os.path.join(OUTPUT_DIR, "index.txt")]  # Include the main page
    for section in sections:
        filepath = save_section_content(section, OUTPUT_DIR)
        if filepath:
            saved_files.append(filepath)
        time.sleep(0.1)  # Small delay between saves
    
    print(f"\n--- Scraping Complete ---")
    print(f"Total files saved: {len(saved_files)}")
    print(f"Files saved to: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == '__main__':
    main()
