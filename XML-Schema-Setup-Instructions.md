# XML Schema Validation Setup Instructions

## What is a Schema?
A schema is like a set of rules that tells your XML file what elements and attributes are allowed. It helps catch errors and ensures consistency across all student projects. Our schema (DH289schema.rnc) is specifically designed for encoding runaway slave advertisements.

## Step 1: Download the Schema File

1. **Download the schema file**: Your instructor will provide you with the `DH289schema.rnc` file
2. **Save it in your project folder**: Place it in the same folder where you'll be creating your XML files
3. **Note the file location**: Remember where you saved it - you'll need this path

## Step 2: Verify XML Extension is Installed

1. Open VS Code
2. Go to Extensions (Cmd+Shift+X on Mac, Ctrl+Shift+X on Windows)
3. Search for "XML" 
4. Make sure the "XML" extension by Red Hat is installed (it should already be installed from your setup)

## Step 3: Create Your XML File with Schema Validation

When you create a new XML file for your assignment, start it like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="DH289schema.rnc" type="application/relax-ng-compact-syntax"?>
<xml>
  <header>
    <!-- Your header content will go here -->
  </header>
  
  <transcript>
    <!-- Your advertisement transcription will go here -->
  </transcript>
  
  <footer>
    <!-- Your structured data will go here -->
  </footer>
</xml>
```

**Important Notes:**
- The second line (`<?xml-model href="DH289schema.rnc"...`) tells VS Code to use our schema
- Make sure the schema file (`DH289schema.rnc`) is in the same folder as your XML file
- If you put the schema file somewhere else, update the `href="DH289schema.rnc"` to point to the correct location

## Step 4: How to Know It's Working

When the schema validation is working properly, you'll see:

✅ **Green indicators**: 
- VS Code will show green squiggly lines under valid elements
- No red error markers for correctly structured content

❌ **Red error indicators**:
- Red squiggly lines under invalid elements or attributes
- Error messages in the "Problems" panel (View → Problems)
- Helpful error messages like "Element 'badname' not allowed here"

## Step 5: Using the Schema While You Work

As you type your XML:
- VS Code will suggest valid element names when you type `<`
- It will warn you if you use elements that don't exist in our schema
- It will check that required elements are present
- It will validate attribute values

## Common Issues and Solutions

**Problem**: "Cannot find schema file"
- **Solution**: Make sure `DH289schema.rnc` is in the same folder as your XML file

**Problem**: No validation happening
- **Solution**: Check that the `<?xml-model...?>` line is exactly as shown above

**Problem**: Everything shows as an error
- **Solution**: Make sure you're using `<xml>` as your root element (not `<document>`)

## Getting Help

If validation isn't working:
1. Check the "Problems" panel (View → Problems) for specific error messages
2. Make sure your file is saved with a `.xml` extension
3. Ask for help in class or during office hours

Remember: The schema is there to help you create valid, consistent XML. Don't ignore the red squiggly lines - they're pointing out real issues that need to be fixed!

---

# Schema Cheat Sheet: Understanding DH289schema.rnc

## Punctuation Marks in Schema (Combination & Repetition Indicators)

### **Combination Indicators:**
- **`,` (comma)** = elements must appear in exact, particular order
- **`|` (pipe)** = indicates a choice, you can pick one or the other

### **Repetition Indicators:** (number of times an element can or must be used)
- **`?` (question mark)** = 0 or 1 (not required, but can only be used once)
- **`+` (plus sign)** = 1 or more (MUST be one, can be more)
- **`*` (asterisk)** = 0 or more (not required, can be used multiple times)
- **No mark** = must appear exactly 1 time

## Color Codes in VS Code

| Color | Meaning | Example in Schema | Example in XML |
|-------|---------|-------------------|----------------|
| <span style="color:blue">**Blue**</span> | Elements (allow text inside tags) | <span style="color:blue">`name = element name {...}`</span> | `<name>Mothra</name>` |
| <span style="color:orange">**Orange**</span> | Attributes (listed inside parent element tag) | <span style="color:orange">`sex = attribute sex {...}`</span> | `<name sex="unk">Godzilla</name>` |
| <span style="color:red">**Red**</span> | Potential responses in elements/attributes | <span style="color:red">`sex = attribute sex {"m", "f", "unk"}`</span> | `<name sex="unk">Godzilla</name>` |
| <span style="color:green">**Green**</span> | Comments (info to help understand usage) | <span style="color:green">`# fun`</span> | `<name sex="unk">Godzilla</name> # fun` |

## Schema Syntax

### Basic Format
The schema defines elements and attributes using this format:
```
data = element data {...}
metadata = attribute metadata {...}
```

The names **inside** the `{...}` curly brackets represent the <span style="color:blue">**elements**</span> and <span style="color:orange">**attributes**</span> that **can** or **must** be nested within the element being defined.

### Example: <span style="color:blue">`data = element data {metadata}`</span>
This names an <span style="color:blue">**element**</span> "data" and says that "metadata" will be nested within it.

**If "metadata" is an <span style="color:blue">element</span>:**
```xml
<data>
    <metadata>...</metadata>
</data>
```

**If "metadata" is an <span style="color:orange">attribute</span>:**
```xml
<data metadata="..."></data>
```

*Note: Quotation marks are required for <span style="color:orange">attributes</span> (single or double, but be consistent)*

## Important Rules

### 1. **Spelling Matters**
Element and attribute names must be spelled **exactly** as in the schema, including case, or VS Code will mark an error.

### 2. **Attribute Syntax**
The schema can control attribute content. For example:
```
proctor = element proctor {sucks}
sucks = attribute sucks {"y" | "n"}
```

**Valid XML:**
```xml
<proctor sucks="y"></proctor>
<proctor sucks="n"></proctor>
```

**Invalid XML** (will show error):
```xml
<proctor sucks="maybe"></proctor>
```

### 3. **Data Within Element Tags**

#### **"text"** - Allows text between element tags
```
proctor = element proctor {sucks, text}
sucks = attribute sucks {"y" | "n"}
```

**XML example:**
```xml
<proctor sucks="y">he really sucks!</proctor>
```

#### **"mixed"** - Allows mixture of text and element tags
```
proctor = element proctor {mixed{sucks, name}}
name = element name {text}
sucks = attribute sucks {"y" | "n"}
```

**XML example:**
```xml
<proctor sucks="y">That lame-o <name>Proctor</name> is really lame</proctor>
```

## Quick Reference for Your Assignment

### Required Root Structure:
```xml
<xml>
    <header>...</header>
    <transcript>...</transcript>
    <footer>...</footer>
</xml>
```

### Common Elements You'll Use:
- **People:** `<name>`, `<persName>` with attributes like `role="enslaved"`
- **Places:** `<place>`, `<placeName>` with `placeType="origin"`
- **Dates:** `<date>` with `when="1853-07-14"` and `dateType="lastSeen"`
- **Structure:** `<p>`, `<lb/>` for line breaks
- **Highlighting:** `<hi rend="bold">` for emphasis

### Remember:
- Check the schema comments (in green) for guidance on how to use elements
- Required attributes will cause errors if missing
- The schema is designed specifically for runaway slave advertisements

---

## Complete Schema Structure Reference

### Main Document Structure
```xml
<xml>
    <header>
        <citationInfo>...</citationInfo>
        <respDesc>...</respDesc>
        <revisionDesc>...</revisionDesc> <!-- optional -->
    </header>
    
    <transcript>
        <!-- Your advertisement transcription goes here -->
    </transcript>
    
    <footer>
        <adType type="enslaver">...</adType>
        <rewardInfo>...</rewardInfo>
        <listPerson>...</listPerson>
        <listPlace>...</listPlace>
    </footer>
</xml>
```

### Header Section Details

#### Citation Information
```xml
<citationInfo>
    <articleTitle>Optional article title</articleTitle>
    <journalTitle>Newspaper Name</journalTitle>
    <publicationDate when="1853-07-14">July 14, 1853</publicationDate>
    <publicationPlace>
        <settlement>City</settlement>
        <state>Ohio</state>
        Granville, Ohio
    </publicationPlace>
    <page>3</page>
    <url>http://example.com</url> <!-- optional -->
    <adUrl>relative/path/to/ad</adUrl> <!-- optional -->
</citationInfo>
```

#### Responsibility Description (Who created this)
```xml
<respDesc>
    <created resp="#ftp" when="2025-09-30">
        <notes>Any notes about the document</notes>
        Created by Your Name
    </created>
</respDesc>
```

### Transcript Section - Encoding the Advertisement Text

#### Basic Paragraph Structure
```xml
<transcript>
    <p>
        Ran away from <place placeType="origin">Granville</place> on 
        <date when="1853-07-10" dateType="departure">July 10th</date>, 
        a <name xml:id="person1">negro man named Tom</name>...
    </p>
    <lb/> <!-- line break if needed -->
    <hi rend="bold">$50 REWARD</hi>
</transcript>
```

#### Special Elements in Transcript:
- **`<graphic>`** - For images in the ad with attributes like `rend="left"`, `height`, `width`
- **`<hi rend="...">`** - For highlighting: `"bold"`, `"italics"`, `"allCaps"`, `"long s"`
- **`<lb/>`** - Line breaks (empty element)

### Footer Section - Structured Data Extraction

#### Ad Type
```xml
<adType type="enslaver"/> <!-- or "jailer" -->
```

#### Reward Information
```xml
<rewardInfo>
    <amount minAmount="50.00" maxAmount="100.00">
        $50 if taken in state, $100 if taken out of state
    </amount>
    <criteria>if delivered to owner</criteria>
</rewardInfo>
```

#### People (Most Complex Section)
```xml
<listPerson>
    <persName xml:id="tom1" role="enslaved" sex="m" 
              foreName="Tom" surName="Johnson" alias="Thomas">
        Tom Johnson, also known as Thomas
        
        <characteristics>
            <physical>
                <phenotype>mulatto</phenotype>
                <build>stout</build>
                <minHeight inches="68.0">5 feet 8 inches</minHeight>
                <minAge years="25">about 25 years old</minAge>
                <eyes>dark eyes</eyes>
                <scars>scar on left hand</scars>
                <clothing>blue jacket and cotton pants</clothing>
            </physical>
            
            <countenance>
                <speech>speaks well</speech>
                <behavior>intelligent and cunning</behavior>
                <previousRunaway ran="y">has run away before</previousRunaway>
                <passAsFree pass="y">will try to pass as free</passAsFree>
            </countenance>
            
            <otherFeatures>
                <literate canRead="y">can read</literate>
                <skills>carpenter and cooper</skills>
                <papersDesc papers="y">may have false papers</papersDesc>
                <horse hadHorse="y">took a bay horse</horse>
            </otherFeatures>
        </characteristics>
    </persName>
</listPerson>
```

#### Places
```xml
<listPlace>
    <placeName placeType="origin" settlement="Granville" 
               county="Licking" state="Ohio" geo="40.068,-82.519">
        Granville, Licking County, Ohio
    </placeName>
</listPlace>
```

### Important Data Types and Formats

#### Dates (`when` attribute)
- **Full date:** `when="1853-07-14"` 
- **Month/Year:** `when="1853-07"`
- **Year only:** `when="1853"`

#### Required vs Optional Elements
- **`+`** = One or more required (e.g., `publicationDate+`)
- **`?`** = Optional (e.g., `articleTitle?`)
- **`*`** = Zero or more (e.g., `notes*`)

#### Controlled Vocabularies (Must use exact values)
- **`placeType`:** `"origin"`, `"potential destination"`, `"location last seen"`, `"pubPlace"`
- **`dateType`:** `"lastSeen"`, `"departure"`, `"dateOfSubmission"`, `"publicationDate"`
- **`role`:** `"enslaved"`, `"enslaver"`, `"collaborator"`, `"other"`
- **`sex`:** `"m"`, `"f"`
- **`type`:** `"jailer"`, `"enslaver"`

### Tips for Success
1. **Start simple** - Get the basic structure working first
2. **Use schema comments** - They explain what each element is for
3. **Follow the data types** - Numbers need `.00` format, dates need `yyyy-mm-dd`
4. **Check controlled vocabularies** - Use exact spelling for predefined values
5. **Build incrementally** - Add complexity as you go