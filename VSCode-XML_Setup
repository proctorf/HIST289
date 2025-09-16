# XML in VSCode — Quick, Free, Beginner-Friendly Setup

Use this one-pager to get students writing well-formed XML in Visual Studio Code, with instant error catching — no paid tools required. (When you’re ready to add schemas, see the bottom.)

---

## Step 1 - Install & Minimal Setup (5 minutes)

### Step A: Install VSCode
1. Go to [https://code.visualstudio.com](https://code.visualstudio.com).  
2. Click **Download** (choose Windows, macOS, or Linux).  
3. Run the installer with default options.  

### Step B: Install Extensions
Open VSCode, then:
1. Click the **Extensions** icon on the left toolbar (four squares).  
2. In the search bar, type each name and click **Install**:
   - **XML Language Support by Red Hat** (core features: error squiggles, tag auto-close/rename, formatting, validation)  
   - **XML Tools** (formatting, XML tree view, quick XPath, pretty-print)  
   - *(Optional, later)* **Xml Complete** (schema-aware completion from XSD)  

### Step C: Add Recommended Settings
1. In VSCode, press **Ctrl + ,** (Windows) or **Cmd + ,** (Mac).  
2. Click the small **document icon with arrow** (top-right corner) to open *Settings (JSON)*.  
3. Paste the following inside the curly braces `{ }`:

```json
{
  "xml.server.binary.preferBinary": true,
  "xml.format.enable": true,
  "xml.format.indentSpaces": 2,
  "xml.format.lineWidth": 80,
  "xml.preferences.quoteStyle": "double",
  "xml.autoCloseTags.enabled": true,
  "editor.linkedEditing": true,
  "xml.validation.enabled": true,
  "xml.validation.schema.enabled": true,
  "xmlTools.enableXmlTreeView": true
}
```

## Step 2: Create a Folder and a New XML File

### Option A — Create a folder on the Desktop (Windows/macOS)
1. **Right-click** your **Desktop** → choose **New → Folder** (macOS: **New Folder**).
2. Name the folder `xml-basics`.

### Option B — Create a folder in Google Drive (with local sync)
> Requires **Google Drive for Desktop** so your Drive appears as a local folder.
1. Open your **Google Drive** folder on your computer.
2. **Right-click** inside it → **New → Folder** (macOS: **New Folder**).
3. Name the folder `xml-basics`.

### Open the folder in VSCode and add a file
1. In VSCode, go to **File → Open Folder…** and select the `xml-basics` folder you just created.  
   - *Tip:* You can also **drag the `xml-basics` folder** onto the VSCode window to open it.
2. In the **Explorer** panel (left sidebar), click **New File** (page icon).
3. Name the file **`example.xml`** (press **Enter** to create it).

## Step 3: Paste a Minimal XML Template

1. Open the file you just created: `example.xml`.  
2. Copy and paste the following template into the file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<document>
  <title>Sample</title>
  <body>
    <p>Hello, XML!</p>
  </body>
</document>
```
3. Save the file (Ctrl + S on Windows / Cmd + S on Mac).

## What happens next

- If your XML is correct, no errors will appear.

- If you make a mistake (e.g., delete a closing tag), you’ll see:

    - Red squiggles under the problematic part.

    - An entry in the Problems panel at the bottom of VSCode.

- Click on a problem entry to jump directly to the error in your file.


## Step 4: Well-Formedness Rules

These are the basic rules your XML must follow. VSCode (with the XML extension) will check them automatically.

- **One root element** wrapping everything  
  Example: `<document> ... </document>`

- **Proper nesting** (no overlaps)  
  ✅ `<a><b></b></a>`  
  ❌ `<a><b></a></b>`

- **Every start tag has an end tag**  
  Example: `<title>Sample</title>` or self-closing `<line/>`

- **Attributes in quotes**  
  Example: `<person role="author">`

- **Case-sensitive tags and attributes**  
  `<Item>` ≠ `<item>`

- **Escape special characters** in text  
  Use `&amp;` for `&`, `&lt;` for `<`, and `&gt;` for `>`

> **Tip:** Right-click → **Format Document**, or press **Alt/Option + Shift + F** to re-indent and make the structure easier to read.

## Step 5: Common Errors & Quick Fixes

Here are some frequent mistakes beginners make, and how to fix them:

- **Mismatched tag**  
  Example: `<titel>` vs `<title>`  
  *Fix:* Place your cursor in the tag name and retype it. With **linked editing** enabled, both opening and closing tags will update.

- **Missing close tag**  
  Example: `<body>` without `</body>`  
  *Fix:* Type `</` and VSCode will suggest the correct closing tag.

- **Overlapping elements**  
  ❌ `<a><b></a></b>`  
  ✅ `<a><b></b></a>`  
  *Fix:* Make sure tags close in the order they were opened.

- **Unescaped ampersand**  
  ❌ `<p>Fish & Chips</p>`  
  ✅ `<p>Fish &amp; Chips</p>`  
  *Fix:* Replace `&` with `&amp;` in text nodes.

- **Multiple roots**  
  ❌ `<title>One</title><title>Two</title>`  
  ✅ `<document><title>One</title><title>Two</title></document>`  
  *Fix:* Wrap everything in a single parent (root) element.

---

### How to spot and fix errors
- Errors will appear as **red squiggles** in your XML file.  
- Open the **Problems panel** (`View → Problems`) to see a list of issues.  
- Click an error message to jump directly to the problem in your code.
