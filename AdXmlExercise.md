# Fugative Ad Encoding Assignment  

You will work in **teams of 2** (with one team of 3). Each team will receive a document to encode. 

Assignment: Encode an ad in XML (not looking for perfection, but for you to work through the experience), and submit a group reflection that includes your responses to Part 1 and Part 6 below.

Due: [Thurs, Oct. 2, 10am](https://denison.instructure.com/courses/16395/assignments/162385)

---

## Part 1: Framing the Work  
Before you begin encoding:  
- As a team, write a **short statement (3–4 sentences)** answering:  
  - *What do you want your encoded product to be/do?*  
  - *What kinds of questions could encoding help you ask about this document?*  

---

## Part 2: Locate Metadata  
Follow this guide to identify citation details for your assigned document:  
👉 **[How to locate the document in the newspaper database →](https://docs.google.com/document/d/1AsYwC4bY28roUFU49bxe6uIJ2Sh9iUtiIFb1DPpXgA4/edit?usp=sharing)**  

---

## Part 3: Analyze Your Document
Before exploring encoding conventions, **examine your assigned document carefully** as a team and create a list:

- What are the **different types of content** you see in the document? (e.g., headlines, body text, advertisements, dates, names, places, etc.)
- What **structural elements** do you notice? (e.g., paragraphs, line breaks, sections, columns)
- What **specific information** would you want to mark up for future analysis? (e.g., people's names, locations, monetary amounts, dates, occupations)
- Are there any **relationships or patterns** you'd want to capture? (e.g., connections between people and places, repeated phrases, editorial commentary)

Write down your observations before moving to Part 4.

---

## Part 4: Explore TEI  
Go to **[tei.org](https://tei.org)**. Now that you've identified the elements you want to encode, investigate TEI best practices for these categories:  

- **Structural:** `<p>`, `<div>`, `<lb/>`, `<note>`, `<quote>`  
- **Entities:** `<name>`, `<place>`, `<date>`  
- **Citation:** `<bibl>`, `<title>`, `<author>`, `<publisher>`

As a team, make a **bullet list of what you learn** about these tags and attributes (e.g., `@type`, `@when`).  

---

## Part 5: Encode in XML  
Open a new XML file in VS Code. Use this **starter structure**:  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<document xml:lang="en">
  <header>
    <!-- This is where you can encode your citation information -->
  </header>

  <body>
    <div type="article" n="1">
      <p>Transcribe the article text here…</p>
      <!-- examples -->
      <!-- <p>Another paragraph…</p> -->
      <!-- <div type="ad">Advertisement text…</div> -->
      <!-- <lb/> for a line break -->
      <!-- <quote>Quoted text</quote> -->
      <!-- <note type="editorial">Your note here</note> -->

       <!-- **FOR SOME TAGS, EXPLORE TEI FOR ELEMENT AND ATTRIBUTE NAMING CONVENTIONS** -->
      <!-- NAME -->
      <!-- PLACE -->
      <!-- <DATE> -->
    </div>
  </body>

  <footer>
    <respStmt>
      <resp>Transcription</resp>
      <name>Team Members’ Names</name>
    </respStmt>
  </footer>
</document>
```

**Conventions:**

One root element `<document>`.

Indent consistently.

Keep original spelling and punctuation.

`<lb/>` for meaningful line breaks; `<pb n="X"/>` if the article spans pages.

`<note>` for your editorial clarifications.

---

## Part 6: Reflection  
Each team should submit a **short reflection (about 1 page, shared voice)** including:  
- What you wanted your product to be/do, and how close you came.  
- What you learned about the process of encoding.  
- What worked smoothly, what was frustrating.  
- **Optional but encouraged:**  
  - Try asking GitHub Copilot (in VS Code) to encode your document.  
  - Compare Copilot’s output with your team’s encoding.  
  - Reflect on differences — structure, accuracy, choices — and what that tells you about human vs. AI encoding.  
