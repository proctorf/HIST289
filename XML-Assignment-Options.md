# XML Encoding Assignment - Approach Options

You have **two options** for completing this XML encoding assignment. Your instructor will discuss both approaches with the class before you choose which to use.

## Option A: Single Comprehensive File
- **File to use:** `DH289schema.rnc`
- **Reference:** `XML-Schema-Setup-Instructions.md`
- **Approach:** All transcription and analysis in one XML file
- **Best for:** Students comfortable with complexity, want to see connections

## Option B: Two Focused Files  
- **Files to use:** `transcript-schema.rnc` + `data-analysis-schema.rnc`
- **Reference:** `Two-File-Workflow.md`
- **Approach:** Separate transcription and data analysis files
- **Best for:** Students preferring step-by-step approach, clearer task separation

---

## Assignment Steps (Regardless of Option)

### Part 1: Framing the Work  
Before you begin encoding:  
- As a team, write a **short statement (3–4 sentences)** answering:  
  - *What do you want your encoded product to be/do?*  
  - *What kinds of questions could encoding help you ask about this document?*  

### Part 2: Locate Metadata  
Follow this guide to identify citation details for your assigned document:  
👉 **[How to locate the document in the newspaper database →](https://docs.google.com/document/d/1AsYwC4bY28roUFU49bxe6uIJ2Sh9iUtiIFb1DPpXgA4/edit?usp=sharing)**  

### Part 3: Analyze Your Document
Before exploring encoding conventions, **examine your assigned document carefully** as a team and create a list:

- What are the **different types of content** you see in the document? (e.g., headlines, body text, advertisements, dates, names, places, etc.)
- What **structural elements** do you notice? (e.g., paragraphs, line breaks, sections, columns)
- What **specific information** would you want to mark up for future analysis? (e.g., people's names, locations, monetary amounts, dates, occupations)
- Are there any **relationships or patterns** you'd want to capture? (e.g., connections between people and places, repeated phrases, editorial commentary)

Write down your observations before moving to Part 4.

### Part 4: Explore TEI  
Go to **[tei.org](https://tei.org)**. Now that you've identified the elements you want to encode, investigate TEI best practices for these categories:  

- **Structural:** `<p>`, `<div>`, `<lb/>`, `<note>`, `<quote>`  
- **Entities:** `<name>`, `<place>`, `<date>`  
- **Citation:** `<bibl>`, `<title>`, `<author>`, `<publisher>`

As a team, make a **bullet list of what you learn** about these tags and attributes (e.g., `@type`, `@when`).  

### Part 5: Download Schema Files

**For Option A (Single File):**
- Download: `DH289schema.rnc`
- Reference: `XML-Schema-Setup-Instructions.md`

**For Option B (Two Files):**
- Download: `transcript-schema.rnc` AND `data-analysis-schema.rnc`  
- Reference: `Two-File-Workflow.md`

### Part 6: Encode in XML

**For Option A:** Create one XML file following the comprehensive schema

**For Option B:** Create two XML files:
1. **Transcript file** - Focus on faithful transcription with basic markup
2. **Data analysis file** - Extract and structure detailed information

### Part 7: Reflection  
Each team should submit a **short reflection (about 1 page, shared voice)** including:  
- What you wanted your product to be/do, and how close you came.  
- What you learned about the process of encoding.  
- What worked smoothly, what was frustrating.  
- **If you chose Option B:** How did separating transcription from analysis affect your work?
- **Optional but encouraged:**  
  - Try asking GitHub Copilot (in VS Code) to encode your document.  
  - Compare Copilot's output with your team's encoding.  
  - Reflect on differences — structure, accuracy, choices — and what that tells you about human vs. AI encoding.

---

## Files You'll Need

### Option A Files:
- `DH289schema.rnc` - Comprehensive schema
- `XML-Schema-Setup-Instructions.md` - Complete reference guide

### Option B Files:
- `transcript-schema.rnc` - Schema for transcription
- `data-analysis-schema.rnc` - Schema for data analysis
- `Two-File-Workflow.md` - Step-by-step workflow guide

### Both Options:
- Your instructor will provide the schema files
- Save them in the same folder as your XML files
- Follow the setup instructions for schema validation in VS Code