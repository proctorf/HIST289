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