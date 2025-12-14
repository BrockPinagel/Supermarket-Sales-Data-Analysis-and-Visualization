Brock Pinagel
College of Business and Information Technology, Lawrence Technological University
INT 6103: Python for Data Analysis and Visualization
Dr. Yash Patel
December 18, 2025

**Supermarket Sales Data: Analysis and Visualization**

	This project examines supermarket sales data to explore key issues related to sales performance, customer behavior, and the factors that influence total revenue. Supermarkets operate in a competitive and fast-paced retail environment in which understanding purchasing patterns is essential for maintaining profitability and operational efficiency. This topic holds significant business value because data-driven insights support improved inventory management, reduced waste, more effective marketing strategies, and better alignment of promotions with customer preferences. From an industry perspective, retailers increasingly rely on analytics to enhance decision-making, forecast demand, and strengthen customer satisfaction, making the analysis both relevant and timely.
  The primary goal of this project is to expose patterns and trends derived from total sales across branches, customer types, and monthly sales. Several guiding questions frame the analysis: Which branches generate the highest revenue? Which customer type is the most valuable? How do unit prices and purchase quantities influence total sales? Are there identifiable monthly or seasonal patterns in sales volume? Addressing these questions provides a comprehensive view of supermarket performance and highlights areas where operational and financial improvements may be possible.
  The analytical approach includes descriptive statistics to summarize the dataset, correlation analysis to examine relationships among variables, and predictive modeling using linear and multiple regression to quantify the factors that influence total sales. A visual analytics dashboard will accompany the statistical analysis to present results clearly and effectively. 

**Dataset Description**

  The dataset used for this analysis is titled “Supermarket Sales: Supermarket Sales Annual Report,” created by Kaggle contributor Ilham Hanif. The dataset is publicly available on Kaggle and contains 5,050 rows and 9 columns. It includes a mix of data types, such as strings, integers, decimals, and categorical values. Key variables include Branch, Customer type, Unit price, Quantity, Total, and Rating, which together provide detailed information about customer purchases, pricing, and overall sales performance.
  The dataset is already well-structured and does not contain missing or null values, making it suitable for statistical analysis and modeling without substantial cleaning. Minor preprocessing steps were performed to support analysis and visualization. Specifically, the Date column was converted to a proper datetime format to allow for accurate time-based grouping and trend analysis. No additional imputation, normalization, or data correction was required because the dataset was clean upon acquisition.

**Methodology**

***Data Cleaning and Preparation***

	The analysis began by importing the supermarket sales dataset from a CSV file into a Pandas DataFrame. An initial structural review confirmed that the dataset contained valid column names and appropriate data types for numerical and categorical analysis. Minor preprocessing steps were performed to ensure consistency. The dataset did not contain any missing, null, or NA values; therefore, no imputation or removal procedures were required. The dataset was visually examined for duplicate rows. Although the code does not explicitly drop duplicates, no duplicate entries were detected during the review, and therefore no records were removed. No filtering was required to remove irrelevant variables or records. All columns and rows were kept because they contributed meaningful information to sales, customer behavior, or performance metrics. Two transformations were performed to prepare the data for time-series and numerical analysis. The Date column was converted from string format into datetime which allowed for the grouping of sales by month. A new variable, Total, was created by multiplying Unit price with Quantity for each transaction. This new variable served as the primary dependent variable for descriptive analysis, correlation, and regression testing. Month was also created by extracting month abbreviations from the datetime format. It was used to aggregate sales by month and present them visually in chronological order. No additional columns were created. Finally, variables aov and branch_sales were created for bar charts using group by Customer type and Branch over Total, respectively. 
  
***Analysis Methods***

	The methodology used to expose patterns and trends derived from the “Supermarket Sales” dataset included descriptive statistics, exploratory visualization, correlation analysis, and predictive modeling. Descriptive statistics were computed for key numerical variables, including Unit price, Quantity, Total, and Rating. The .describe() function in Pandas provided measures of central tendency (mean, median), dispersion (standard deviation), and distributional shape (minima and maxima). Additionally, value counts were generated for categorical variables such as Gender and Product line to identify the most common customer demographics and product categories. Grouped descriptive statistics were also produced. Total sales and quantity sold were aggregated by Product line using .groupby(), allowing comparison of product category performance. A comprehensive visual analytics dashboard was created using Matplotlib and Seaborn. The dashboard contained six charts that illustrated trends and patterns across customer, branch, and time-based segments. This includes a histogram of total purchase amounts to observe overall spending distribution, a boxplot of ratings by branch to compare customer satisfaction across store locations, a line plot of monthly sales totals to identify seasonal or monthly patterns, a correlation heatmap highlighting relationships among numerical variables, a bar chart of average order value by Customer type, and a bar chart of total sales by Branch to visualize performance differences across locations. Correlation analysis was performed to assess linear relationships between numerical variables. The primary correlation of interest was between Unit price and Total. A Pearson correlation coefficient and corresponding p-value were computed using SciPy’s pearsonr() function to determine statistical significance. A full correlation matrix was also generated using df.corr(numeric_only=True) to visualize relationships among all numerical variables. Two regression approaches were used to evaluate predictors of total sales including simple linear regression and multiple regression. A linear regression model was fitted with Unit price as the predictor and Total as the response variable. The model provided the coefficient, intercept, and R² value, indicating how much variation in total sales was explained by unit price alone. A multivariate linear regression model was constructed using all numerical predictors except Total. This approach allowed examination of how various quantitative factors, such as quantity purchased and rating, jointly contributed to predicting total sales. The model produced coefficient estimates and R² scores, demonstrating the collective predictive strength of multiple variables. Additionally, Statsmodels OLS regression was used to generate a full statistical summary, offering p-values, confidence intervals, and diagnostic measures.

**Visualization Figures**

Figure 1
Bar Chart of Average Order Value by Customer Type

  The bar chart shows two categories on the x-axis, labeled “Member” and “Normal” customer types, with average order value on the y-axis. On average, customers who are members of the supermarket chain spend more per order than non-member customers. Members spend an average of $225 per order, whereas normal customers spend roughly $170. This may indicate that members may be taking advantage of membership benefits, discount programs, or special offers making them more inclined to spend more.

Figure 2
Box plot of Average Rating by Branch

	This box plot shows the distribution of customer ratings for each branch of the supermarket, with Brooklyn, Manhattan, and Queens on the x-axis and rating on the y-axis. All branches have a similar average rating of approximately 7, possibly suggesting that each branch provides a comparable, above-average quality experience to customers.

Figure 3
Correlation Heatmap

	Figure 3 displays a correlation heatmap showing the relationships between continuous variables in the dataset, including Unit price, Quantity, Rating, and Total. The matrix indicates that Unit price and Quantity have the strongest positive impact on Total; as Unit price and purchase Quantity increase, Total also increases.

Figure 4
Histogram of Distribution of Transaction Values

	Figure 4 presents the distribution of transaction values as a histogram with a trend line. Total value per transaction is shown on the x-axis, and transaction count is displayed on the y-axis. The histogram reveals that the vast majority of transactions have totals below $200, possibly suggesting that customers purchase lower-cost items far more frequently than higher-cost items.

Figure 5
Line Plot of Monthly Total Sales

	Figure 5 illustrates monthly sales figures, with months on the x-axis and total sales on the y-axis. Sales peak in April and reach their lowest point in August, with a sharp decline in between, before climbing again in September and maintaining positive growth through January. This pattern may indicate that shoppers take advantage of spring specials with bulk purchases to avoid higher prices during the summer months, before resuming purchases in the fall.

Figure 6
Pie Chart Percentage of Total Sales by Branch

	The pie chart displays the percentage of total sales by branch, including Brooklyn, Manhattan, and Queens. All three branches account for similar proportions of total sales, which may suggest that each store maintains comparable foot traffic and attracts a healthy number of customers in its respective area.

**Dashboard**

Figure 7
Graphics Dashboard

	Figure 7 presents the dashboard, with the histogram in the upper left, box plot in the upper right, time series in the middle left, correlation matrix in the middle right, bar chart in the lower left, and pie chart in the lower right. Although the dashboard is static, it consolidates all relevant and meaningful data visualizations into a single figure. Insights from the dashboard include relationships between branch ratings and sales proportions, as well as the impact of Unit price, Quantity, and transaction values on total sales. Since all three branches have similar ratings, they may attract a stable and consistent number of customers, resulting in steady sales. Additionally, the correlation heatmap and the right-skewed histogram may indicate that customers may frequently purchase low-cost items in bulk, which contributes significantly to total sales.
  
**Findings and Insights**

	The analysis of the supermarket sales dataset revealed several meaningful patterns across customer behavior, branch performance, pricing, and transaction characteristics. Clear trends emerged across the visualizations. The histogram indicated that most transaction totals fell below $200, possibly suggesting that customers primarily purchase low-cost items and often in smaller bundles. The box plot showed that all three branches; Brooklyn, Manhattan, and Queens, maintain identical average customer ratings of 7, which may indicate consistent customer satisfaction across locations.
  The time-series analysis revealed a distinct seasonal pattern, with sales peaking in April and declining sharply through August before rising again in September and continuing upward into January. This trend may indicate that customers engage in bulk purchasing during spring promotions and reduce spending during summer months. The pie chart showed that total sales are nearly evenly distributed across branches, indicating similar levels of foot traffic and stable customer bases at each location.
  Several relationships among variables were uncovered. The correlation heatmap demonstrated that Unit price and Quantity have the strongest positive relationships with total sales and total transaction value. This pattern aligns with the right-skewed distribution of transaction totals, further reinforcing that larger totals are driven primarily by increased quantities and higher-priced items. The bar chart comparing customer types revealed that members spend considerably more per order (approximately $225) than non-members (roughly $170), which may indicate that membership incentives, discounts, or brand loyalty may influence higher spending habits.
  No major anomalies appeared in the dataset, and data quality remained consistent across branches and customer groups. Overall, the findings highlight predictable purchasing behavior, stable branch performance, and strong relationships between pricing, quantity, and total sales. These insights provide a clear understanding of key factors driving supermarket revenue among the store branches in New York’s three boroughs.

**Recommendations**

	Based on the patterns identified in the analysis, two data-driven recommendations can help improve business performance and guide future strategy. First, the supermarket chain should consider expanding or promoting membership programs. Members spend significantly more per transaction than non-members, indicating that incentives tied to membership; such as discounts, loyalty points, or exclusive offers, successfully encourage higher spending. Increasing marketing efforts around membership enrollment or enhancing member-only benefits could drive substantial revenue growth. 
  Second, promotional strategies should be aligned with observed seasonal trends. Sales peak in April and fall sharply through August, suggesting customers respond strongly to spring promotions but reduce spending during summer months. Introducing targeted summer discounts, bundle deals, or seasonal product campaigns may stabilize sales during historically low-performing months. Additionally, maintaining strong promotions in early spring can maximize revenue during periods of naturally high demand.
  
**Conclusion**

	The analysis successfully addressed the original goal of understanding sales performance, customer behavior, and the key factors influencing total sales within the supermarket dataset. Through descriptive statistics, visualization, correlation analysis, and predictive modeling, the project identified clear patterns in purchasing behavior, seasonal sales trends, and branch-level performance. The findings showed that customer spending is concentrated in lower-cost purchases, membership status is associated with higher average order values, all branches perform consistently, and total sales are strongly driven by unit price and quantity.
  Several insights emerged from the project, including the stability of branch ratings, the even distribution of sales across locations, and the pronounced seasonal dip in sales during the summer months. The correlation heatmap and regression models also reinforced the relationships between pricing, quantity, and total transaction value, providing a deeper understanding of the variables that most directly affect revenue.
  Despite these meaningful findings, the analysis faced certain limitations. The dataset covered only one year of transactions, which restricted long-term trend analysis and reduced the ability to model seasonality with higher accuracy. The dataset also lacked demographic variables, limiting insights into customer segments and purchasing motivations. Additionally, the absence of cost or margin data prevented the evaluation of profitability rather than revenue alone. Future work could incorporate multi-year data, demographic information, and more advanced predictive models to provide a more comprehensive analysis. 

References

HANIF, I. (2025). Supermarket Sales. Kaggle.com. https://www.kaggle.com/datasets/hanif13/supermarket-sales

‌






 





Disclosure: AI was used for brainstorming, grammar, punctuation, organization, peer-review, and tone. The content and ideas for the project and this paper are my own.
