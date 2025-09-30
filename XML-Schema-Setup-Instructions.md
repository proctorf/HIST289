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