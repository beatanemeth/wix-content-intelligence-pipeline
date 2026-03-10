# Data Science Brainstorming & Strategy

This document tracks the analysis goals, strategy, and progress for the Wix Data Science Study project.

## 1. Analysis Framework: The 4-Group Structure

### **Group 1: Baseline Volume & Trends (Temporal Analysis)**

- **Goal**: Establish the "Source of Truth" regarding the volume of content and events over time.
- **Key Charts**: Annual Activity Comparison (Bar), Monthly Seasonality (Line), Content Velocity (Growth Trend).
- **Metric**: Total counts of records per Year/Month.

### **Group 2: Descriptive Performance (Efficiency & Demand)**

- **Goal**: Identify "The Winners" and measure how hard each asset works for the brand.
- **Efficiency Benchmarking**: Move beyond raw totals to "Average Views per Post" and "Average Attendance per Event" to identify high-impact formats.
- **Time-Weighted Normalization**: Account for older content having more time to accumulate views (e.g., Views per month since publication).
- **Metrics**: Engagement Rate (Likes/Views), Attendance Rate (Going/Total), Waitlist Pressure.

### **Group 3: Content Strategy & Structural Modeling**

- **Goal**: Analyse the "What" and "How" of the content creation.
- **Metrics**: Category Popularity (Frequency of posts vs. Average Engagement).
- **Structural**: Word Count vs. Engagement (Correlation between text length and performance).

### **Group 4: Advanced NLP & Unstructured Text Analysis**

- **Goal**: Extract hidden value and themes from `contentText` and `descriptionText`.
- **N-Gram Analysis**: Extract common 2-word and 3-word phrases to identify high-performing topics and "Content Hooks."
- **Modeling**: Topic Modeling (LDA) for broader theme discovery (if dataset size permits).
- **Sentiment**: Analyse if certain tones (Enthusiastic vs. Professional) correlate with higher engagement.

---

## 2. Step-by-Step Strategy & Plan

**Phase 1: Discovery & Preparation**

1.  **Load Data**: Import all three JSON files into a single Jupyter Notebook.
2.  **Data Cleaning**: Convert dates to datetime objects and handle missing categories.
3.  **Feature Engineering**: Create columns for `engagement_efficiency`, `attendance_rate`, `word_count`, and `days_since_publication`.

**Phase 2: Exploratory Data Analysis (EDA)**

1.  **Trends**: Run Group 1 analysis (Years/Months).
2.  **Efficiency**: Run Group 2 analysis (Averages/Normalization/Top Performers).
3.  **Content**: Run Group 3 analysis (Categories/Word Count).

**Phase 3: Visualisation & NLP**

1.  **Charts**: Generate the visualisations using a consistent visual identity (Custom Palettes).
2.  **NLP**: Run N-Gram extraction, Keyword extraction and basic Sentiment analysis (Group 4).

**Phase 4: Future Polish**

1.  **Brand-Aligned Data Storytelling**: Ensure all final charts follow the project's visual identity for professional portfolio presentation.
2.  **Interactive Dashboard**: Convert the final analysis into a Streamlit application for interactive filtering (e.g., by Year or Category).

---

## 3. Data Sources

- `articles.json`: CMS Content (Static)
- `blog_posts.json`: Blog Content (Dynamic with Metrics)
- `events.json`: Events (Attendance Metrics)

## 4. Recommended Plotting Libraries

- **Seaborn**: Built on top of Matplotlib, it produces modern, aesthetically pleasing charts with less code and natively handles Pandas DataFrames.
- **Plotly**: Recommended for creating interactive charts (hover for values, zoom, etc.), providing a more professional and "live" feel to the portfolio.
- **Matplotlib**: Used for fine-tuning charts, such as adjusting axis labels and layouts.
