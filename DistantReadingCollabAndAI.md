---
layout: page
title: "Week Fourteen: Distant Reading with and for AI"
hide_warning: true
---

> Adapted from weekfourteen.md by AMSUCF/HumanitiesAI (original: https://github.com/AMSUCF/HumanitiesAI/blob/main/weekfourteen.md). Used with permission.

## Exercise: Distant Reading with and for AI

This week, we're going to revisit the distant reading we did earlier this semester, but now we'll be approaching the procedural aspects of the project more directly with agentic AI assistance. We'll revisit collecting, processing, and analyzing a dataset of texts, but now we can work at a much larger scale with access to libraries of existing code. We'll primarily be making use of a few Python libraries: 

- [Pandas](https://pandas.pydata.org/) is a library for data manipulation and analysis, used to manage CSV files and structured data.
- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) is a library for parsing HTML and XML, useful for extracting content during web scraping.
- [Requests](https://requests.readthedocs.io/en/latest/) is a library for making HTTP requests in Python, used for downloading data from the web.
- [Matplotlib](https://matplotlib.org/) is a library for creating visualizations like graphs and charts.
- [NLTK](https://www.nltk.org/) is a natural language processing toolkit, used here to filter out stopwords during text preprocessing.

You might find it helpful to look at documentation of these libraries, or even web scraping and distant reading tutorials in Python, for ideas of things to try. While you can install Python directly on your machine to complete these tasks, my demos will be using [Google Colab](https://colab.research.google.com/), a free service for deploying code in different environments - more extensive usage does require paying, but you should have no problems completing these tasks at the free usage level. 

### Working with the Colab Notebook

You'll be using a pre-built Google Colab notebook and working with Python libraries like Pandas, Matplotlib, and NLTK. Before you start, choose at least five novels for your analysis and download them as .txt files from Project Gutenberg.

**Starter Notebook Link**: [Distant Reading](https://colab.research.google.com/drive/13WWZCpxqh1m9Kun8Z2uv2vxdqQxk-9kE?usp=sharing)

Run through every cell in the notebook to complete the basic workflow, then use Gemini (Google Colab's AI agent) to extend your analysis. Once you've completed the basic workflow, ask Gemini to help you create additional analysis. Consider approaches like:

- **Concordance Analysis**: Create concordances for individual texts and combine them to identify frequent words across all books
- **Additional Visualizations**: Create new charts, graphs, or visual representations of your data
- **Comparative Analysis**: Generate code to compare specific aspects across your novel collection

These visualizations can either work with one specific novel or text (as shown in the last cell of the demo, the character network, which will vary in quality depending on how your text is structured) or across all of them.

### Discussion

As you work through the analysis, consider how the relationship with text in distant reading connects to the other ways we've been working with AI (both in text and code) throughout the semester. Share your most interesting findings from your distant reading analysis, including your documented visualizations. What did the computational approach reveal about your chosen novels? How did working with an AI agent change your analytical process compared to our earlier distant reading experiments? What are the benefits and limitations of using agentic AI for literary analysis?

Refer back to this week's readings on algorithms and variables, and connect your experience to broader questions about digital humanities, the relationship between human and machine reading, and how AI tools are changing the perception of "reading."