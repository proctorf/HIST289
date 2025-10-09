# Visualizing HOLC Redlining Data in QGIS - Columbus

## Lab Instructions: Creating a Redlining Map

This exercise will guide you through downloading HOLC redlining data and creating a professional map using QGIS. You'll work with both vector data (boundaries) and raster data (historical maps).

## Step 0: Download and Organize Data

## Download Data from Mapping Inequality

1. Go to [Mapping Inequality](https://dsl.richmond.edu/panorama/redlining/)
2. Navigate to the Columbus, Ohio map
3. **Important**: Scroll down past the initial download buttons at the top of the page
   - The buttons at the top download the **entire national dataset** (all cities)
   - You need the **individual city data** shown as thumbnails below
4. Find the Columbus, Ohio thumbnails showing both vector and raster data previews
5. Download the **Geopackage** format for vector data (recommended for beginners)
6. Download the **GeoTIFF** raster file for the historical map background
7. Rename the files to `columbus.gpkg` and `OH_Columbus_1936.tif` respectively

### Why Geopackage vs GeoJSON?
- **Geopackage (.gpkg)**: Single file, handles complex data better, industry standard, works perfectly in QGIS
- **GeoJSON (.json)**: Text-based, web-friendly, but can be larger and slower for complex datasets
- **Shapefile (.shp)**: Legacy format that requires multiple files (.shp, .shx, .dbf, .prj) - you'll likely encounter these in other courses or professional work, but they're more complicated for beginners
- **For beginners: Use Geopackage** - it's more reliable and faster in QGIS

### Files You Should Have:
- `[cityname]_boundaries.gpkg` - Vector file containing HOLC redlining boundaries with grade classifications  
- `[cityname]_1936.tif` - Historical raster map from 1936

### Understanding HOLC Grades:
- **Grade A** (Best/Green): Lowest risk areas for lending
- **Grade B** (Still Desirable/Blue): Moderate risk areas  
- **Grade C** (Declining/Yellow): Higher risk areas
- **Grade D** (Hazardous/Red): Highest risk, often minority neighborhoods

## Step-by-Step Instructions

### Step 1: Load Data into QGIS

1. **Open QGIS** and create a new project
2. **Add the raster layer:**
   - Go to `Layer` → `Add Layer` → `Add Raster Layer`
   - Browse and select your `[cityname]_1936.tif` file
   - Click `Add` and `Close`
3. **Add the vector layer:**
   - Go to `Layer` → `Add Layer` → `Add Vector Layer`
   - Browse and select your `[cityname]_boundaries.gpkg` file
   - Click `Add` and `Close`

### Step 2: Add a Base Map

1. **Install QuickMapServices plugin** (if not already installed):
   - Go to `Plugins` → `Manage and Install Plugins`
   - Search for "QuickMapServices" and install
2. **Add base map:**
   - Go to `Web` → `QuickMapServices` → `OpenStreetMap` → `OSM Standard`
   - Or try `Google` → `Google Satellite` for aerial imagery

### Step 3: Style the HOLC Boundaries by Grade

1. **Right-click** on your boundaries layer (e.g., `columbus_boundaries`) → `Properties`
2. **Go to Symbology tab**
3. **Change from "Single Symbol" to "Categorized"**
4. **Set Value to "grade"** (this is the field containing A, B, C, D classifications)
5. **Click "Classify"** to automatically create categories
6. **Customize colors** for each grade:
   - **Grade A**: Green (`#228B22` or similar)
   - **Grade B**: Blue (`#4682B4` or similar)
   - **Grade C**: Yellow (`#FFD700` or similar)
   - **Grade D**: Red (`#DC143C` or similar)
7. **Adjust transparency** to ~30-50% so you can see the base map underneath
8. **Click OK** to apply

### Step 4: Add Labels to Show Area Names

1. **Right-click** on your boundaries layer → `Properties`
2. **Go to Labels tab**
3. **Change from "No Labels" to "Single Labels"**
4. **Set Value to "label"** (this contains A1, A2, B1, etc.)
5. **Customize label appearance:**
   - Increase font size (12-14pt recommended)
   - Choose a contrasting color (black or white)
   - Add a white halo or buffer for better readability
6. **Click OK** to apply

### Step 5: Organize Layer Order

1. **In the Layers panel**, drag layers to organize:
   - Boundaries layer (vector) - on top
   - Base map (web layer) - middle
   - Historical map (raster) - bottom (optional, can turn off)

### Step 6: Save Your Work

1. **Save the project:**
   - `Project` → `Save As`
   - Choose a location and filename (e.g., "[CityName]_Redlining_Map.qgz")
2. **Export a map image:**
   - `Project` → `Import/Export` → `Export Map to Image`
   - Choose PNG or JPEG format
   - Set resolution (300 DPI for high quality)
   - Click `Save`

## Recommended Color Schemes

**Traditional HOLC Colors:**
- A: `#76a865` (green)
- B: `#7cb5bd` (blue)
- C: `#ffff00` (yellow)
- D: `#d9838d` (red/pink)

**High Contrast:**
- A: `#228B22` (forest green)
- B: `#4682B4` (steel blue)
- C: `#FFD700` (gold)
- D: `#DC143C` (crimson)

**Colorblind Friendly:**
- A: `#2E8B57` (sea green)
- B: `#4682B4` (steel blue)
- C: `#DAA520` (goldenrod)
- D: `#B22222` (fire brick)

---

## GeoJSON vs Geopackage vs Shapefile: Key Differences

### Geopackage (.gpkg) - **RECOMMENDED**
- **Single file** format (easy to share and manage)
- **Industry standard** for modern GIS workflows
- **Excellent performance** with large datasets
- **Supports complex data** types and relationships
- **Cross-platform** compatibility

### GeoJSON (.json)
- **Human-readable** text format
- **Web-friendly** - works directly in web browsers
- **Good for simple datasets** and web mapping
- **Can be large** for complex geometries

### Shapefile (.shp)
- **Legacy format** - still widely used
- **Multiple files** required (.shp, .shx, .dbf, .prj minimum)
- **Performance issues** with large datasets
- **Limited data types** and field name restrictions

### When to Use Each:
- **Use Geopackage** for most GIS work, especially as a beginner
- **Use GeoJSON** for web mapping and simple data sharing
- **Use Shapefile** only when required by older software or specific workflows