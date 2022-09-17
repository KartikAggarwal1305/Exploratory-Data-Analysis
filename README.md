Exploratory Data Analysis in Python - Part1 (Basic)


Exploratory Data Analysis What is Exploratory Data Analysis(EDA)?
So, before knowing what EDA is , firstly you should dive into the data and When you want dig deeper inside data we use EDA. In EDA, we try to investigate , try to look what is hidden into the data ,  for example some patterns or any anomalies that will eventually give results and add meaning to entire exercise we are doing.

Why is it important!
:->It helps us understand data before coming to conclusion
:->It helps with clarity before making any assumption
:->It help us to spot erroneous in data 
:->It backs up data with proof for example, when you showcase any observations, you have the appropriate data to back up your observations
:->EDA, gives us the trend analysis and that lead us to the future predictions
:->When EDA is used in machine learning it helps us in handling underfitting and overfitting models.


Types of EDA
1) Univariate analysis  :- Analysis of single variable.
2) Bivariate Analysis  :- Analysis of two variables.
3) Multivariate Analysis :- Analysis based on more than two variables. 
You can think of univariate and bivariate analysis , Let me give you example on multivariate analysis' , if you are trying to teach a machine learning algorithm, which will predict if a person is diabetic or not, it will depend on a lot of different things , it depends on your age , hereditary , blood sugar , BMI , obesity or not , there are million different variables that can be used to access that a person has diabetes or not , so to analyze these kind of analysis multivariate analysis is used.


#Moving to Important Aspects Of EDA

(EDA) Data Visualization  in Python

Data Visualization involves converting textual and numerical data into aesthetically pleasing and functional graphs/reports. Dashboarding is a key part of data visualization. Non technical audience should understand data / dashboards just by looking at it.

1) Matplotlib :- Its Very Versatile in terms of support for graphs and charts
2) Seaborn :- Seaborn Provides a high level interface that can be used for statistical graphs
3) Plotly :- It Provides Multiple unique 3D plots supported

Important Graphs for Visualization in EDA
1) Bar Plots
2) Pie Charts
3) Histograms
4) Boxplots
5) Scatterplot
6) Strip Plot
7) Heatmap

We all have heard of first 3 graphs, Lets look into :- 

BOXPLOT IN EDA
A box plot is a representation of a measure, for example , if you have a lot of data point and you calculate the central tendency that is Mean , Median and Mode.
Box plot so if you look at box plot , its divided into 4 quartile , like you see 1st is Min to Q1 , 2nd is from Q1 to Median, 3rd is Median to Q3 and 4th is Q3 to Max. So in this case , we have Min value as maybe 1 and max is at 29. The outliers are the value some rare cases which are exponentially higher value than the data.

SCATTERPLOT IN EDA
Scatter plot are the graphs that present the relationship of two Numerical Data.
It denotes the intersection of two numerical data points and usually the result is plotted into a regression line. The independent variable is plotted on x axis and dependent variable is plotted on the Y axis.

STRIPPLOT IN EDA
( Almost similar to scatterplot)
It is a good complement to a boxplot in cases where all observations are shown along with some representation of the underlying distribution. It is used to draw a scatter plot based on the category.
In scatter plot we use two numerical format data, but in strip plot we can use one categorical ( a ,b ,c etc. ) and other numerical data points 

HEATMAP IN EDA
Heatmap is colorful beautiful matrix of independency between two variables. Correlation matrix shows how one value effect on other. Colors are used to signify the correlation
