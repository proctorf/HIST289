# Two-File XML Encoding Workflow

This document outlines an alternative approach to XML encoding that separates transcription from data analysis into two focused files.

## Overview: Why Two Files?

### **Approach A: Single File** (DH289schema.rnc)
- Everything in one document
- More complex but shows connections
- Good for experienced students

### **Approach B: Two Files** (This approach)
- **File 1:** Focus on faithful transcription
- **File 2:** Focus on structured data analysis
- Easier for beginners, clearer separation of tasks

---

## File 1: Transcript File (`your-ad-transcript.xml`)

### Purpose
Focus entirely on **faithful transcription** of the advertisement text with basic markup.

### Schema: `transcript-schema.rnc`

### Basic Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="transcript-schema.rnc" type="application/relax-ng-compact-syntax"?>
<advertisement>
    <header>
        <citationInfo>
            <journalTitle>Daily Ohio Statesman</journalTitle>
            <publicationDate when="1853-07-14">July 14, 1853</publicationDate>
            <publicationPlace>
                <settlement>Columbus</settlement>
                <state>Ohio</state>
                Columbus, Ohio
            </publicationPlace>
            <page>3</page>
            <adUrl>link/to/your/data/file.xml</adUrl>
        </citationInfo>
        
        <respDesc>
            <created resp="#abc" when="2025-09-30">
                <notes>First attempt at transcription</notes>
                Created by Student Name
            </created>
        </respDesc>
    </header>
    
    <transcript>
        <hi rend="bold">$50 REWARD</hi>
        <lb/>
        <p>
            Ran away from <place ref="granville">Granville</place> on 
            <date when="1853-07-10">July 10th</date>, a 
            <name xml:id="tom1">negro man named Tom</name>, about 25 years old...
        </p>
        <p>Said <name xml:id="tom1">Tom</name> is well known in 
        <place ref="newark">Newark</place> and may attempt to reach 
        <place ref="cleveland">Cleveland</place>.</p>
    </transcript>
</advertisement>
```

### Key Features of Transcript File:
- **Simple markup:** `<name>`, `<place>`, `<date>` with basic attributes
- **Focus on transcription accuracy**
- **Links to data file** via `adUrl`
- **ID references** that will connect to detailed analysis

---

## File 2: Data Analysis File (`your-ad-data.xml`)

### Purpose
Extract and structure **detailed information** about people and places mentioned in the advertisement.

### Schema: `data-analysis-schema.rnc`

### Basic Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="data-analysis-schema.rnc" type="application/relax-ng-compact-syntax"?>
<peopleAndPlaces>
    <header>
        <linkedTranscript transcriptFile="your-ad-transcript.xml">
            <transcriptTitle>$50 Reward Advertisement</transcriptTitle>
        </linkedTranscript>
        
        <respDesc>
            <created resp="#abc" when="2025-09-30">
                <notes>People and places analysis</notes>
                Created by Student Name
            </created>
        </respDesc>
    </header>
    
    <analysis>
        
        <listPerson>
            <persName xml:id="tom1" role="enslaved" sex="m" 
                      foreName="Tom" surName="Johnson">
                Tom Johnson
                <characteristics>
                    <physical>
                        <phenotype>described as negro</phenotype>
                        <minAge years="25">about 25 years old</minAge>
                        <build>stout built</build>
                        <clothing>blue jacket and cotton pants</clothing>
                    </physical>
                    <countenance>
                        <speech>speaks well for his situation</speech>
                        <previousRunaway ran="y">has run away before</previousRunaway>
                    </countenance>
                    <otherFeatures>
                        <skills>carpenter and cooper</skills>
                    </otherFeatures>
                </characteristics>
            </persName>
        </listPerson>
        
        <listPlace>
            <placeName xml:id="granville" placeType="origin" 
                       settlement="Granville" county="Licking" state="Ohio">
                Granville, Licking County, Ohio
            </placeName>
            <placeName xml:id="cleveland" placeType="potential destination" 
                       settlement="Cleveland" state="Ohio">
                Cleveland, Ohio
            </placeName>
        </listPlace>
    </analysis>
</data>
```

---

## Workflow for Students

### **Step 1: Create Transcript File**
1. Focus on **faithful transcription**
2. Mark up basic elements: names, places, dates
3. Use simple attributes: `xml:id`, `ref`, `when`
4. **Don't worry about** detailed analysis yet

### **Step 2: Create People and Places Analysis File**
1. **Extract detailed information** about people and places only
2. Use the **same IDs** to link back to transcript
3. Add **structured data**: physical descriptions, place types, etc.
4. **Focus purely on** people and geographic information

### **Step 3: Link the Files**
- Use `adUrl` in both files to reference each other
- Use matching `xml:id` and `ref` attributes to connect elements
- Ensure citation information is consistent

---

## Advantages of Two-File Approach

### **For Students:**
- **Less overwhelming** - focus on one task at a time
- **Clearer learning objectives** - transcription vs. analysis skills
- **Easier debugging** - smaller, focused files
- **Sequential workflow** - natural progression from transcription to analysis

### **For Instructors:**
- **Easier to grade** different skills separately
- **Flexible assignment structure** - could assign just transcription first
- **Clear assessment** of different competencies
- **Scalable** - could add more analysis files later

### **For Projects:**
- **More realistic workflow** - mirrors professional digital humanities projects
- **Reusable components** - transcripts could be used for multiple analyses
- **Collaborative friendly** - different team members could work on different files

---

## Comparison with Single-File Approach

| Aspect | Single File | Two Files |
|--------|-------------|-----------|
| **Complexity** | High | Moderate |
| **Learning curve** | Steep | Gradual |
| **File management** | Simple | Moderate |
| **Task focus** | Mixed | Clear |
| **Beginner friendly** | No | Yes |
| **Professional workflow** | Less realistic | More realistic |
| **Grading clarity** | Mixed | Clear |

---

## Getting Started

1. **Download both schema files:**
   - `transcript-schema.rnc`
   - `data-analysis-schema.rnc`

2. **Create your first file:** Start with the transcript
   - Name it: `[yourname]-ad-transcript.xml`
   - Focus on accurate transcription with basic markup

3. **Create your second file:** Move to data analysis
   - Name it: `[yourname]-ad-data.xml`
   - Extract and structure the detailed information

4. **Link the files:** Use consistent IDs and reference the files in each other's headers