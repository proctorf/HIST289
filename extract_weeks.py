#!/usr/bin/env python3
"""
Extract individual week files from index.md
Usage: python extract_weeks.py
"""

import re
import os
from pathlib import Path

def extract_weeks_from_index():
    """Extract week sections from index.md and create individual week files."""
    
    # Read index.md
    try:
        with open('index.md', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: index.md not found")
        return
    
    # Find all week sections using regex
    # Matches "## Week N - Title" through to next "## Week" or end of file
    week_pattern = r'## (Week \d+[^\n]*)(.*?)(?=## Week \d+|## Thanksgiving|$)'
    weeks = re.findall(week_pattern, content, re.DOTALL)
    
    created_files = []
    
    for week_title, week_content in weeks:
        # Extract week number
        week_num_match = re.search(r'Week (\d+)', week_title)
        if not week_num_match:
            continue
            
        week_num = week_num_match.group(1)
        filename = f"week{week_num}.md"
        
        # Create the week file content
        file_content = f"""---
title: {week_title}
---

# {week_title}
{week_content.strip()}
"""
        
        # Write the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        created_files.append(filename)
        print(f"Created/updated {filename}")
    
    # Handle Thanksgiving section
    thanksgiving_pattern = r'## (Thanksgiving[^\n]*)(.*?)(?=## Week \d+|$)'
    thanksgiving_match = re.search(thanksgiving_pattern, content, re.DOTALL)
    
    if thanksgiving_match:
        title, content_section = thanksgiving_match.groups()
        file_content = f"""---
title: {title}
---

# {title}
{content_section.strip()}
"""
        with open('thanksgiving.md', 'w', encoding='utf-8') as f:
            f.write(file_content)
        created_files.append('thanksgiving.md')
        print("Created/updated thanksgiving.md")
    
    print(f"\nExtracted {len(created_files)} files: {', '.join(created_files)}")

if __name__ == "__main__":
    extract_weeks_from_index()
