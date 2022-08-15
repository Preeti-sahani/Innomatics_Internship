#!/usr/bin/env python
# coding: utf-8

# # Descriptive Statistics and Python Implementation
# 
# The topics explained in the notebook are as follows:
# 
# ![DS.jpg](attachment:DS.jpg)

# ## Descriptive Statistics 
# 
# Descriptive statistics are used to describe the basic features of the data in a study. They provide simple summaries about the sample and the measures. Together with simple graphics analysis, they form the basis of virtually every quantitative analysis of data.
# 
# ![ds1.png](attachment:ds1.png)

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
random.seed = 42

df=pd.read_csv("data.csv")


# In[2]:


df.head()


# # Measure of Central Tendency:
# 
# A measure of central tendency is a single value that attempts to describe a set of data by identifying the central position within that set of data. As such, measures of central tendency are sometimes called measures of central location. They are also classed as summary statistics.
# 
# 1. Mean 
# 
# The mean is equal to the sum of all the values in the data set divided by the number of values in the data set.
# ![ds2.jpg](attachment:ds2.jpg)
# 
# 
# 

# 2. Median 
# 
# The median is the middle score for a set of data that has been arranged in order of magnitude. The median is less affected by outliers and skewed data.
# ![ds3.jpg](attachment:ds3.jpg)

# 3. Mode 
# 
# The mode is the most frequent score in our data set. On a histogram it represents the highest bar in a bar chart or histogram. You can, therefore, sometimes consider the mode as being the most popular option. An example of a mode is presented below:
# ![ds4.jpg](attachment:ds4.jpg)
# 

# In[3]:


df.mean()


# In[4]:


df.median()


# In[5]:


df.mode()


# ## Variance 
# 
# Variance is the expected value of the squared variation of a random variable from its mean value, in probability and statistics. Informally, variance estimates how far a set of numbers (random) are spread out from their mean value. Variance is symbolically represented by σ2, s2, or Var(X).
# 
# 
# ![ds6.jpg](attachment:ds6.jpg)

# In[6]:


df.var()


# ## Standard Deviation 
# 
# Standard deviation is the positive square root of the variance. Standard deviation is one of the basic methods of statistical analysis. Standard deviation is commonly abbreviated as SD and denoted by 'σ’ and it tells about the value that how much it has deviated from the mean value.
# 
# 
# ![ds7.webp](attachment:ds7.webp)

# The empirical rule, or the 68-95-99.7 rule, tells you where most of your values lie in a normal distribution:
# 
# 1. Around 68% of values are within 1 standard deviation from the mean.
# 2. Around 95% of values are within 2 standard deviations from the mean.
# 3. Around 99.7% of values are within 3 standard deviations from the mean.
# 
# Features of Normal Distribution Curve:
# 
# 1. The mean, median and mode are exactly the same.
# 2. The distribution is symmetric about the mean—half the values fall below the mean and half above the mean.
# 3. The distribution can be described by two values: the mean and the standard deviation.

# In[7]:


df.std()


# In[8]:


np.corrcoef(df['Mthly_HH_Income'],df['Mthly_HH_Expense'])


# In[9]:


x = np.array(df['Mthly_HH_Income'])
y = np.array(df['Mthly_HH_Expense'])
print(x)
print(y)


# In[10]:


plt.title('Correlation')

plt.scatter(x,y)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))
         (np.unique(x)), color='red')

plt.xlabel('Monthly Income')
plt.ylabel('Monthly Expense')

plt.show()


# In[11]:


df.head(10)


# In[16]:


# Importing the required Libraries:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm,skew


# In[17]:


x_axis = np.array(df['Mthly_HH_Income'])
mean = x_axis.mean()
sd = x_axis.std()
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()


# # Positively Skewed & Negatively Skewed Normal Distribution
# 
# If one tail is longer than another, the distribution is skewed. These distributions are sometimes called asymmetric or asymmetrical distributions as they don’t show any kind of symmetry. Symmetry means that one half of the distribution is a mirror image of the other half. For example, the normal distribution is a symmetric distribution with no skew. The tails are exactly the same.
# 
# ![ds11.jpg](attachment:ds11.jpg)
# 
# A **left-skewed distribution** has a long left tail. Left-skewed distributions are also called negatively-skewed distributions. That’s because there is a long tail in the negative direction on the number line. The mean is also to the left of the peak.
# 
# A **right-skewed distribution** has a long right tail. Right-skewed distributions are also called positive-skew distributions. That’s because there is a long tail in the positive direction on the number line. The mean is also to the right of the peak.
# 
# 

# ## Skewed Left (Negative Skew)
# 
# A left skewed distribution is sometimes called a negatively skewed distribution because it’s long tail is on the negative direction on a number line.
# 
# A common misconception is that the peak of distribution is what defines “peakness.” In other words, a peak that tends to the left is left skewed distribution. This is incorrect. There are two main things that make a distribution skewed left:
# 
# 1. The mean is to the left of the peak. This is the main definition behind “skewness”, which is technically a measure of the distribution of values around the mean.
# 2. The tail is longer on the left.
# 3. In most cases, the mean is to the left of the median. This isn’t a reliable test for skewness though, as some distributions (i.e. many multimodal distributions) violate this rule. You should think of this as a “general idea” kind of rule, and not a set-in-stone one.
# 
# ## Skewed Right / Positive Skew
# 
# A right skewed distribution is sometimes called a positive skew distribution. That’s because the tail is longer on the positive direction of the number line.
# 
# ![ds13.jpg](attachment:ds13.jpg)
# 

# ## skew normal distribution
# 
# The skew normal distribution is a normal distribution with an extra shape parameter, α. The shape parameter skews the normal distribution to the left or right. As it is only the skew of the normal distribution that’s being changed, the skew normal family has many of the same properties of the normal distribution:
# 1. It’s defined over the real number line.
# 2. The square of a random variable is a chi-square variable (from a chi-square distribution) with one degree of freedom.
# 3. The distribution is unimodal (one peak).
# 4. The location parameter, μ(i.e. the mean), defines where the peak is and the scale parameter, σ(i.e. the standard deviation) determines the distribution’s spread.
# 
# 
# The skew normal has a number of interesting properties related to alpha:
# 
# 1. If the skew normal has a skew of zero, then it becomes the normal distribution.
# 2. If the sign of alpha changes, the distribution will flip over the y-axis.
# 3. As alpha increases (in absolute value), the skew also increases.
# 4. As alpha tends towards infinity, the series converges to the folded normal density function.
# 
# Therefore, the normal distribution can be seen as a special case of the skew normal distribution.

# ## QQ Plot(Quantile-Quantile):
# 
# In Statistics, Q-Q(quantile-quantile) plots play a very vital role to graphically analyze and compare two probability distributions by plotting their quantiles against each other. If the two distributions which we are comparing are exactly equal then the points on the Q-Q plot will perfectly lie on a straight line y = x.
# 
# ![ds14.jpeg](attachment:ds14.jpeg)

# In[18]:


data_points = np.array(df['Mthly_HH_Income'])
z = (data_points - np.mean(data_points))/np.std(data_points)

stats.probplot(z,dist='norm',plot=plt)
plt.title("Normal Q-Q plot")
plt.show()


# ## Box-Cox 
# 
# Box-Cox method helps to address non-normally distributed data by transforming to normalize the data. However there is no guarantee that data follows normality, because it does not really checks for normality. The Box-Cox method checks whether the standard deviation is the smallest or not.

# In[19]:


data_points = np.array(df['Mthly_HH_Income'])
fitted_data, fitted_lambda = stats.boxcox(data_points)
fig, ax = plt.subplots(1, 2)


sns.distplot(data_points, hist = False, kde = True,
            kde_kws = {'shade': True, 'linewidth': 2},
            label = "Non-Normal", color ="green", ax = ax[0])
 
sns.distplot(fitted_data, hist = False, kde = True,
            kde_kws = {'shade': True, 'linewidth': 2},
            label = "Normal", color ="green", ax = ax[1])

plt.legend(loc = "upper right")
 
# rescaling the subplots
fig.set_figheight(5)
fig.set_figwidth(10)
plt.show()


# In[ ]:




