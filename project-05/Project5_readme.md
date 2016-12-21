
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 5: Loan Classification
#### Due Wednesday, December 21, 9 am

### Overview

You are going to create a model to predict loan status (good / bad) using data from Lending Club.  Download the 2015 data from [here](https://www.lendingclub.com/info/download-data.action).  

#### Data Manipulation

The data require some cleaning before you can build the model.  Think about what you are trying to predict, and how to re-engineer categories in order to do this.  What are the categories for loan status in the data?<br>
*hint*:  only use loans that have been determined (i.e. not current loans).<br>
*hint*:  re-categorize the loans into "good" and "bad" (only two categories)

Let's use annual income, debt-to-income, interest rate, loan term, funded amount and home ownership to model the loan status.  If you don't know what these features are, have a look at the data dictionary on the Lending Club [page](https://www.lendingclub.com/info/download-data.action).

#### EDA
Before doing any kind of modelling, explore the data.  For example, what is the distribution of good / bad loans?  Are interest rate and DTI related?  Make some pivot tables / plots to better understand the data you have.

#### Model
Create your classification model using the above features!<br>
*hint*: your data must be numerical in order to create your model.  Are all of the data numerical?  What can you do to make them numerical?  (Look-up dummy variables)

Once you have your model, make a prediction based on the first row of data.  What is the probability of loan repayment for this person?  If your boss asked you whether the person is going to repay, what would you say?



**Deliverables**: a Jupyter  notebook including EDA (plotting) and your model.  Or you can work in pycharm, but you must submit EDA as well.  Also you should submit a blog post describing your project.
