# Working with XML in VS Code

These instructions assume you’ve already installed the following extensions:  

- **XML Language Support by Red Hat**  
- **XML Tools**  
- **XML Complete**  

Together, these extensions provide syntax highlighting, validation, formatting, autocompletion, and tag helpers for working with XML.

---

## 1. Core Features of the Extensions

- **XML Language Support by Red Hat**  
  - Real-time validation: highlights mismatched or missing tags.  
  - Auto-completion for closing tags.  
  - Hover support: shows documentation for elements when available.  

- **XML Tools**  
  - Pretty-print / format XML (<kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd> on Windows/Linux, <kbd>Shift</kbd> + <kbd>Option</kbd> + <kbd>F</kbd> on Mac).  
  - XPath evaluation and XML-to-JSON tools (more advanced).  

- **XML Complete**  
  - Helps generate matching end tags as soon as you type a start tag.  
  - Adds convenience commands for wrapping selections with tags.  

---

## 2. Useful Shortcuts

- **Wrap selection with a tag (Emmet)**  
  1. Select the text.  
  2. Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (Windows/Linux) or <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (Mac).  
  3. Choose **Emmet: Wrap with Abbreviation**.  
  4. Type the tag name (e.g. `p`, `item`) and press <kbd>Enter</kbd>.  

  *Tip:* Bind **Emmet: Wrap with Abbreviation** to a direct shortcut for faster use.  

- **Format the entire document**  
  - Windows/Linux: <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd>  
  - Mac: <kbd>Shift</kbd> + <kbd>Option</kbd> + <kbd>F</kbd>  

- **Auto-close tags**  
  - Just type `<tagname>` and the closing `</tagname>` will appear automatically.  

---

## 3. Turning Off Code Suggestions

By default, VS Code may suggest completions that feel overwhelming to new users. To reduce this:

1. Open **Settings** (<kbd>Ctrl</kbd> + <kbd>,</kbd> or <kbd>Cmd</kbd> + <kbd>,</kbd> on Mac).  
2. Search for **“suggestions”**.  
3. Toggle off:  
   - `Editor › Quick Suggestions` (set to `false`)  
   - Or limit them by language: add to `settings.json`:

   ```json
   "[xml]": {
       "editor.quickSuggestions": false
   }

## 4. Soft Wrapping (No Horizontal Scrolling)

To make long XML lines wrap at the edge now of the editor window:

1. Open **Settings** (<kbd>Ctrl</kbd> + <kbd>,</kbd> on Windows/Linux, <kbd>Cmd</kbd> + <kbd>,</kbd> on Mac).
2. Search for **“word wrap.”**
3. Set **Editor: Word Wrap** to **on**.  
   *Optional:* Set **Editor: Word Wrap Column** (e.g., 100–120) if you want a fixed wrap width.

## 5. General Ease-of-Use Tips

- **Indentation:** Set a consistent indent size in **Editor: Tab Size** (2 or 4). Turn on **Editor: Insert Spaces** to avoid tab/space mix-ups.  
- **Format on Save:** Enable **Editor: Format On Save** so XML is auto-formatted every time you save.  
- **Default Formatter:** In **Settings**, search for **“default formatter”** and set your preferred XML formatter if needed.  
- **Minimap:** If distracting, disable via **View → Appearance → Show Minimap**.  
- **Auto Save:** Turn on via **File → Auto Save** (or configure a delay in **Settings**).  
- **Problems Panel:** Keep an eye on the **Problems** panel (bottom bar) for XML validation errors flagged by the Red Hat extension.  
- **Whitespace/Guides:** Enable **Editor: Render Whitespace** (to see stray spaces) and **Editor: Rulers** (e.g., `80, 100, 120`) to guide line length.  
- **Language Mode:** Ensure the status bar shows **XML** (click it to switch if VS Code didn’t detect the file type).  
- **Suggestions Noise:** If completions feel overwhelming while learning, temporarily disable them for XML in **settings.json**:  

  ```json
  "[xml]": {
    "editor.quickSuggestions": false
  }