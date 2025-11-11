# Tableau Power Start Workbook 2025
*Updated for Modern Tableau - A Hands-On Learning Experience*

## How This Tutorial Works

- **Instructor demonstrates** each module first
- **You practice** the exercises at your own pace
- **Raise your hand** if you need help
- **Stretch/Bonus sections** for those who finish early
- **Wait for instructor** before moving to next module

---

## Module 0: Connect to Data

### Drill 1: Connect to Your Dataset

1. **Open Tableau Public** (free download from tableau.com/public)

2. **Review the Start Screen**
   - Connect Panel (left): Data source options
   - Recent Work (center): Your previous projects  
   - Discover (right): Examples and tutorials

3. **Connect to Your Data**
   - Click **Text file** in the Connect panel
   - Navigate to your CSV file and open it
   - **View the data preview** below

4. **Notice Data Types**
   - Tableau automatically assigns data types
   - **Globe icon** = Geographic data (Country, State)
   - **Calendar icon** = Date data
   - **# symbol** = Number data
   - **Abc** = Text data

5. **Start Visualizing**
   - Click **Sheet 1** at the bottom to begin!

### Stretch Time / Bonus Work
- Why is this "Module 0" instead of "Module 1"?
- Explore **Help** → **Search for "Excel"** to learn about data connections
- Check out the **Discover** panel videos (mute audio for now)

---

## Module 1: Tableau Basics and Concepts

### Key Concepts to Remember

**1. Data Analysis Philosophy**
- Go beyond describing data to **analyzing** for insights
- Start by **asking questions** of your data
- Analysis is an **iterative journey**, not a destination

**2. Understanding Fields**
- **Dimensions (blue)**: Categories, labels, buckets (locations, names, ratings)
- **Measures (green)**: Numbers that can be analyzed (prices, counts, budgets)

**3. Generated Fields**
- **Geographic fields** → Tableau creates Latitude/Longitude for mapping
- **Count field** → Simple count of rows (named after your Excel sheet, like "Workshop Data 1 (Count)")

**4. Show Me Panel**
- Upper right corner of screen
- Select fields first, then **Show Me** suggests chart types
- One-click chart creation!

**5. The Tableau Workspace**
- **Data Panel (left)**: Drag fields from here
- **Shelves (blue areas)**: Control how fields appear (Rows, Columns, Filters)
- **Canvas (center)**: Where your visualization appears
- **Marks Card**: Controls colors, sizes, labels, tooltips

### Practice Time
**Explore the interface** for a few minutes:
- Drag fields from left panel to Rows and Columns
- Try different combinations
- Use **Show Me** with fields selected
- Practice **Undo** and **Redo** buttons
- Ask yourself questions and try to answer them!

---

## Module 2: Going to the Bar (Chart)

### Drill 2.1: Show Number of Movies by Rating

1. **Clear the sheet** (🗑️ in toolbar) or create **New Worksheet** (+)

2. **Create your first chart**
   - Double-click **"Workshop Data 1 (Count)"** (or similar name) from the data panel
   - Congratulations! You made your first chart!

3. **Rename for clarity**
   - Right-click **"Workshop Data 1 (Count)"** in the canvas panel
   - Rename it **"Number of Movies"** 
   - This makes it easier to understand what we're counting
   - You cannot rename a "generated" or "count" pill created by Tableau. But, you can create a new field, naming it whatever you want, and copy the information from the count or generated pill
    - To do so, click on the pill in question, select the down arrow, select "Create", select "Calculated Field"; rename the field whatever you want and use the formula Count[(FieldName)], in this instance use Count[(Workshop Data 1)]

4. **Understand what happened**
   - Tableau put the measure on the Rows shelf
   - Bottom left shows "Number of Marks" and the sum of your count field

5. **Add a breakdown**
   - Drag **Rating** to the Columns shelf
   - How did the chart change?
   - Hover over bars to see tooltips

6. **Try different orientations**
   - Click **Swap Rows and Columns** button (⇄) in the toolbar
   - See how the chart orientation changes
   - Click it again to return to the original view

7. **Name your sheet**
   - Right-click sheet tab → Rename → "Number of Movies by Rating"
   - Tableau uses this as the chart title!

### Drill 2.2: Show Average Budget by Rating

1. **New worksheet** (+)

2. **Build the chart**
   - Drag **Budget** to Rows shelf
   - Drag **Rating** to Columns shelf

3. **Change aggregation**
   - Right-click **SUM(Budget)** pill on Rows shelf
   - Select **Measure** from the dropdown menu
   - Choose **Average** from the submenu
   - Notice how the pill changes to **AVG(Budget)** and tooltips update!

4. **Think about the difference**
   - Compare this chart to your previous one (Number of Movies by Rating)
   - What story does SUM tell vs. AVERAGE?
   - Which rating category has the highest total spending vs. highest average spending?

5. **Rename sheet**: "Avg Budget by Rating"

### Drill 2.3: Show Average Gross by Rating

1. **New worksheet** (+)
2. **Drag Gross** to Rows, **Rating** to Columns
3. **Change aggregation** to AVERAGE
4. **Rename sheet**: "Avg Gross by Rating"

### Drill 2.4: Show Average Profit by Rating

1. **New worksheet** (+)
2. **Drag Profit** to Rows, **Rating** to Columns  
3. **Change aggregation** to AVERAGE
4. **Rename sheet**: "Avg Profit by Rating"

### Drill 2.5: Show Average Votes by Rating

1. **New worksheet** (+)
2. **Drag IMDB Votes** to Rows, **Rating** to Columns
3. **Change aggregation** to AVERAGE
4. **Rename sheet**: "Avg Votes by Rating"

### Drill 2.6: Show Bar Values and Format Numbers

1. **Using the chart from Drill 2.5**

2. **Method 1**: Click **Show Mark Labels** icon (Aa) in toolbar
   - Toggle on/off to see the difference

3. **Method 2**: Drag **IMDB Votes** to **Label** on Marks card
   - Problem: Bars show average, labels show sum!

4. **Fix the aggregation**
   - Right-click the label pill → Change to **AVERAGE**

5. **Format the numbers**
   - Right-click the label pill → **Format**
   - Change to display numbers in **Thousands** with **1 Decimal Place**

### Data-to-Ink Ratio Concept
*Edward Tufte's principle: The more "ink" (pixels) used, the harder data becomes to understand*

**Tufte's 5 Rules:**
1. Above all else, show the data
2. Maximize the data-ink ratio  
3. Erase non-data ink
4. Erase redundant data-ink
5. Revise and edit

*Question: Are value labels on bars helpful or cluttering?*

---

## Module 3: Toeing the Line (Chart)

*Line charts are perfect for showing trends over time*

### Drill 3.1: Show Number of Movies by Release Year

1. **New worksheet** (+)
2. **Drag Number of Movies** to Rows
3. **Drag Release Date** to Columns
4. **Hover over the line** to see tooltips
5. **Rename sheet**: "Number of Movies by Release Year"

### Drill 3.2: Show Budget by Release Year

1. **New worksheet** (+)
2. **Drag Budget** to Rows, **Release Date** to Columns
3. **Rename sheet**: "Movie Budget by Release Year"

### Drill 3.3: Show Gross by Year

1. **New worksheet** (+) 
2. **Drag Gross** to Rows, **Release Date** to Columns
3. **Rename sheet**: "Movie Gross by Release Year"

### Drill 3.4: Show Profit by Release Year

1. **New worksheet** (+)
2. **Drag Profit** to Rows, **Release Date** to Columns  
3. **Rename sheet**: "Movie Profit by Release Year"

### Drill 3.5: Show IMDB Votes by Release Year

1. **New worksheet** (+)
2. **Drag IMDB Votes** to Rows, **Release Date** to Columns
3. **Rename sheet**: "IMDB Votes by Release Year"

### Drill 3.6: Making Lines Show More

1. **Using the IMDB Votes chart**

2. **Change aggregation**
   - Right-click **SUM(IMDB Votes)** → Change to **AVERAGE**
   - Use Undo/Redo to see the difference

3. **Add size and color**
   - Drag **Profit** to **Size** on Marks card
   - Drag **Profit** to **Color** on Marks card
   - Notice how this shows profit trends!

4. **Change aggregations to AVERAGE**
   - Right-click both size and color pills
   - Change both to **AVERAGE**

**When to use line charts**: Perfect for showing trends over time. The connected points help spot patterns that bar charts might miss.

---

## Module 4: Making Sense of the Whole

*Tree maps show how parts contribute to the whole*

### Drill 4.1: Show Share of Movies by Genre

1. **New worksheet** (+)
2. **Drag Genre** to Rows shelf
3. **Drag Number of Movies** to Columns shelf
4. **Change to tree map**
   - Open **Show Me** panel (upper right)
   - Click the **Treemap** icon
5. **Rename sheet**: "Share of Movies by Genre"

### Drill 4.2: Show Share of Movie Budget by Genre

1. **New worksheet** (+)
2. **Drag Genre** to Rows, **Budget** to Columns
3. **Use Show Me** → **Treemap**
4. **Rename sheet**: "Share of Movie Budget by Genre"

### Drill 4.3: Show Share of Movie Profit by Genre

1. **New worksheet** (+)
2. **Drag Genre** to Rows, **Profit** to Columns
3. **Use Show Me** → **Treemap**  
4. **Rename sheet**: "Share of Movie Profit by Genre"

### Why Not Pie Charts?
*Pie charts are often harder to interpret than alternatives. Tree maps and bar charts usually communicate part-to-whole relationships more effectively.*

---

## Module 5: Taking it to the Table (Chart)

*Tables are great for looking up exact values, but not ideal for spotting patterns*

### When Tables Work Best
- Looking up specific, exact values
- Detailed reference information
- When precise numbers matter more than trends

### When Tables Don't Work Well  
- Comparing values across categories
- Spotting patterns or trends
- Quick visual analysis

### Drill 5.1: Show Movies by Year and Rating

1. **New worksheet** (+)
2. **Drag Release Date** to Rows shelf
3. **Drag Rating** to Columns shelf  
4. **Drag Number of Movies** to the **Text** card (Abc icon)
5. **Rename sheet**: "Movies by Year and Rating"

### Drill 5.2: Show Key Financial Data by Rating

1. **New worksheet** (+)
2. **Drag Rating** to Rows shelf
3. **Drag these fields to Text card** (one at a time):
   - Number of Movies
   - Budget  
   - Gross
   - Profit
   - ROI (if available)
4. **Rename sheet**: "Key Financial Data"

**Important**: Notice how Tableau aggregates the data. We'll fix aggregation issues in the next module!

---

## Module 6: Making the Right Calculations

*The #1 mistake in Tableau: Incorrectly aggregating ratios*

### The Problem with Ratios

**Wrong way**: Average of ratios = (90% + 60%) ÷ 2 = 75%  
**Right way**: Ratio of sums = (90 + 6) ÷ (100 + 10) = 87%

### Drill 6.1: Create a Correct ROI Calculation

1. **Start with your Key Financial Data sheet**

2. **Create a calculated field**
   - Notice that in the "Data pane" directly above the list of fields from your data there is a search bar, and next to that are icons for "filter by" (the funnel), "view data", (the speadsheet), and a down arrow.
   - Select the down arrow (this opens up a new dropdown window)
   - Select **"Create Calculated Field..."** (you can also find this under the "Analysis" Tab)

3. **Name and formula**
   - Name: "Correct ROI Ratio"
   - Formula: `SUM([Profit]) / SUM([Budget])`
   - Click **OK**

4. **Add to your table**
   - Drag **Correct ROI Ratio** to your table

5. **Format the numbers**
   - Right-click **Correct ROI Ratio** in data panel
   - **Default Properties** → **Number Format** → **Number (Custom)**
   - Set to **2 decimal places**

**Key Learning**: Always create ratios from sums, not sums of ratios!

---

## Module 7: Mapping Our Data

### Drill 7.1: Show Number of Movies by Country

1. **New worksheet** (+)
2. **Drag Country** to the canvas
   - Tableau automatically creates a map!
3. **Drag Number of Movies** to **Color** card
4. **Rename sheet**: "Number of Movies by Country"

### Drill 7.2: Show Profit Ratio by Country

1. **New worksheet** (+)
2. **Drag Country** to canvas  
3. **Drag Correct ROI Ratio** to **Color** card
   - Use the calculated field, not the original measure!
4. **Rename sheet**: "Profit Ratio by Country"

### Drill 7.3: Improving Tooltips

1. **Using the Profit Ratio by Country map**

2. **Explore current tooltips**
   - Hover over different countries
   - Which country offers the best ROI?

3. **Add more information**
   - Drag **Number of Movies** to **Tooltip** card
   - Hover again - does this change your assessment?

4. **Customize tooltip format**
   - Click directly on **Tooltip** card
   - Edit the text formatting
   - Use Undo/Redo to compare versions

---

## Module 8: Building Dashboards

*Combine multiple visualizations to tell a complete story*

### Drill 8.1: Show Profit Ratio by Genre and Rating

1. **New worksheet** (+)
2. **Build the chart**
   - Drag **Rating** to Columns
   - Drag **Genre** to Rows  
   - Drag **Correct ROI Ratio** to Rows
3. **Add context**
   - Drag **Number of Movies** to Tooltip
   - Then drag **Number of Movies** to **Color** card
4. **Rename sheet**: "Profit Ratio by Rating and Genre"

### Drill 8.2: Show Average Budget and Profit Ratio by Release Year

1. **New worksheet** (+)
2. **Build base chart**
   - Drag **Budget** to Rows, **Release Date** to Columns
   - Change Budget aggregation to **AVERAGE**
3. **Add profit information**
   - Drag **Correct ROI Ratio** to **Color** card
   - Drag **Correct ROI Ratio** to **Size** card
4. **Rename sheet**: "Average Budget and Profit Ratio by Release Year"

### Drill 8.3: Show Profit Ratio by Release Quarter

1. **New worksheet** (+)
2. **Build timeline**
   - Drag **Release Date** to Columns
   - Drag **Correct ROI Ratio** to Rows
3. **Change to quarters**
   - Click on **Release Date** pill → Select **Quarter**
4. **Make it a bar chart**
   - **Show Me** → Select **Bar Chart**
5. **Flip orientation**
   - Click **Swap Rows and Columns** icon (⇄)
6. **Add volume information**
   - Drag **Number of Movies** to **Color** card
7. **Rename sheet**: "Profit Ratio by Release Quarter"

### Drill 8.4: Create a Dashboard

1. **New Dashboard**
   - Click **New Dashboard** button (bottom right)

2. **Add worksheets**
   - Drag **"Profit Ratio by Rating and Genre"** to canvas
   - Drag **"Average Budget and Profit Ratio by Release Year"** below first chart  
   - Drag **"Profit Ratio by Release Quarter"** to the right of second chart

3. **Add title**
   - **Dashboard** menu → Check **"Show Title"**
   - Rename tab: **"What Type of Movie Should We Make?"**

### Drill 8.5: Make the Dashboard Interactive

1. **Enable filtering**
   - Click on each chart
   - Click the **funnel icon** (filter) that appears
   - Do this for all three charts

2. **Test interactivity**
   - Click on elements in one chart
   - Watch how other charts filter
   - Press **Escape** to clear selections

3. **Analyze the results**
   - What type of movie would be best to make?
   - When would be the ideal release time?

### Drill 8.6: Publish to Share

1. **Save to Tableau Public**
   - From the **File** menu Select **Save to Tableau Public As...**
   - This will prepare your workbook for online publishing

2. **Log in or create account**
   - Sign in to your existing Tableau Public account
   - Or create a new free account if you don't have one
   - Complete the login process

3. **Name your visualization**
   - Give your dashboard a descriptive title
   - Click **Save**

4. **Capture your dashboard URL**
   - Once published, your dashboard opens in a web browser
   - Look for the **Share** button (looks like a sideways V with circles at the end of the lines)
   - Click it to get the shareable link
   - Copy this URL for submission or sharing

5. **Test your published dashboard**
   - Paste the copied url into a new web browser
   - Verify interactivity works online
   - Try the filters and hover effects
   - Share the link with others!

---

## Module 9: Next Steps

---

## Final Reflection Assignment

### Part A: Practical Analysis (150-200 words)

Reflect on what you learned from analyzing this movie dataset. Consider these questions:

1. **ROI Insights**: What did your analysis reveal about which types of films have the best return on investment? Think about:
   - Which ratings (G, PG, PG-13, R) showed the highest profit ratios?
   - How did release timing affect profitability?
   - What patterns did you notice between budget size and success?

2. **Historical Perspective**: How might these insights be useful for understanding the film industry during this time period? What questions would you want to explore next?

### Part B: Tutorial Reflection (100-150 words)

Reflect on your experience working through this Tableau tutorial:

1. **Learning Process**: What was the most challenging part of learning Tableau? What clicked for you?
2. **Skills Gained**: Which visualization techniques do you think will be most useful for your future work?

### Part C: Fail Log (100-150 words)

Document your problem-solving process:

1. **Issues Encountered**: What technical problems did you run into? (e.g., data not loading, charts not appearing as expected, confusion about interface elements)
2. **Solutions Found**: How did you overcome these challenges? What resources helped you?
3. **Lessons Learned**: What would you do differently if you started this tutorial again?

---

### Continue Learning Tableau
- **Tableau.com/learn**: Free videos and training
- **Viz of the Day**: Daily inspiration email
- **Makeover Monday**: Weekly data visualization challenges

### Key Takeaways
1. **Start with questions** - What do you want to know?
2. **Iterate and explore** - Analysis is a journey
3. **Choose the right chart type** for your message
4. **Keep it simple** - Follow Tufte's data-ink ratio
5. **Tell a story** - Connect your visualizations meaningfully

---

## Common Mistakes to Avoid

1. **Ratio aggregation errors** - Always use calculated fields for ratios
2. **Wrong chart types** - Match chart to data and message
3. **Too much decoration** - Focus on the data story
4. **No context** - Always include tooltips and explanations
5. **Ignoring your audience** - Design for who will use it

---

*Congratulations! You've completed the Tableau Power Start Workbook. You now have the foundational skills to create compelling data visualizations. Keep practicing and exploring!*