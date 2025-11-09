Here's a revised assignment sheet based on the Programming Historian tutorials your students have completed:

---

# **Assignment: Mapping Enslaved Populations in the American South, 1860**

## **Objective**
Use GIS tools and census data to create a thematic map revealing patterns of enslaved populations across Southern counties in 1860. This assignment will demonstrate the power of digital tools for historical inquiry and give you experience using AI chatbots as coding/technical assistants.

## **Learning Goals**
- Apply GIS skills to historical research questions
- Experience how digital tools can reveal historical patterns invisible in traditional sources
- Practice using AI chatbots as technical problem-solving assistants
- Analyze spatial patterns of slavery on the eve of the Civil War

## **Background Knowledge Required**
You should be comfortable with the QGIS workflows from the Programming Historian tutorials, including loading vector layers, managing different layer types, basic styling, and coordinate system concepts from georeferencing work.

## **Task Overview**
Create a map of Southern US counties showing the relative enslaved populations in 1860. Your map should clearly communicate spatial patterns and include appropriate symbology, legends, and contextual elements.

## **Major Steps** (Figure out the specifics using your tutorial knowledge and AI assistance)
1. **Collect historical data** from IPUMS NHGIS for 1860 (detailed instructions provided below)
2. **Set up QGIS project** with appropriate coordinate system (hint: look for "84")
3. **Load** census data (CSV) and county boundary shapefiles
4. **Join** census data with county boundaries (you'll need to research this process)
5. **Calculate** enslaved population ratios (you'll need to learn about field calculator)
6. **Select** Southern states and create focused map extent
7. **Style** layers to show spatial patterns effectively
8. **Design** final map with legend, title, and context

## **Data Collection Instructions - IPUMS NHGIS**

1. **Create account**: Go to nhgis.org → "Get Data" → register → verify email
2. **Start extract**: Log in → "Get Data" → "Create Extract"
3. **Geographic levels**: Check boxes for "County" and "State"
4. **Select year**: Check "1860"
5. **Browse tables**: Look for population tables including enslaved/slave populations
6. **Add to cart**: Select relevant tables with racial/enslaved population data
7. **Geographic extent**: Choose "United States"
8. **Submit**: Add description → submit extract
9. **Download**: Wait for email → download CSV data and GIS boundary files

## **Technical Problem-Solving Requirement**
Your Programming Historian tutorials covered basic QGIS operations, but this assignment requires additional skills like:
- Joining tabular data to vector layers
- Using field calculator for mathematical operations
- Advanced symbology techniques

**Use an AI chatbot** (ChatGPT, Claude, etc.) to help you learn these new techniques and troubleshoot problems. **Document one specific instance** where the AI helped you solve a problem (include this in your submission).

## **Deliverables**
1. **Final map** (PDF or high-resolution image) showing enslaved population patterns in the South
2. **Brief reflection** (300-500 words) addressing:
   - What spatial patterns do you observe? What historical questions do they raise?
   - How did digital tools change your understanding compared to reading text descriptions?
   - Describe how the AI chatbot assisted you technically
   - What new QGIS skills did you have to learn beyond the Programming Historian tutorials?

## **Evaluation Criteria**
- Technical execution (appropriate data, accurate joins, clear symbology)
- Historical insight (thoughtful analysis of spatial patterns)
- Design quality (readable, professional cartographic presentation)
- Effective use of AI assistance for problem-solving
- Evidence of learning new technical skills

## **Due Date**: [Thurs, Oct 30th at 10am]

## **Resources**
- Programming Historian QGIS tutorials (foundation knowledge)
- IPUMS NHGIS (nhgis.org)
- AI chatbot of your choice for technical assistance
- QGIS documentation and community forums

---