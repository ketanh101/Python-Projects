#######################################
# Ketan Honrao
# PMDS
# Final Project: Custom Library
# Used pandas, matplotlib, and seaborn
#######################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import csv
# Original data contained 60,000 rows. Used filters on Race and Education to remove NA rows. 
# Removed unnecessary columns, only leaving employee or compensation related columns
# Result was roughly 21,000 rows of cleaned data

#Analyze average compensation 
#Analyze factors leading to higher salaries
#Analyze pay disparities based on gender and ethnicity

#custom library

#define constants

max_years_exp = 50
min_years_at_company = 1

#load all data
def load_data(file_path):
    df = pd.read_csv(file_path)
    print(df)
    return df



#parent class
class Employee:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def filter_by_gender(self, gender):
        return self.df[self.df['gender'] == gender]

    def filter_by_race(self, race):
        return self.df[self.df['Race'] == race]
    
    def filter_by_education(self, education):
        return self.df[self.df['Education'] == education]

    def get_highest_paid_employees(self, n=10):
        ds_df = self.df.loc[self.df['title'] == 'Data Scientist']
        return ds_df.nlargest(n, 'total_comp')

    
#create Data Scientist child class using Employee parent class
class DataScientist(Employee):
    def __init__(self, file_path):
        super().__init__(file_path)

    def avg_comp(self, job_title):

        ds_df = self.df[self.df['title'] == job_title]
        avg_comp = ds_df['total_comp'].mean()
        return avg_comp
    
    def avg_base(self, job_title):
        ds_df = self.df[self.df['title'] == job_title]
        avg_base = ds_df['base_salary'].mean()
        return avg_base
    
    def avg_stock(self, job_title):
        ds_df = self.df[self.df['title'] == job_title]
        avg_stock = ds_df['stock_grant_value'].mean()
        return avg_stock
    
    def avg_bonus(self, job_title):
        ds_df = self.df[self.df['title'] == job_title]
        avg_bonus = ds_df['bonus'].mean()
        return avg_bonus
    
    def get_top_earners(self, n):
        data = self.df[self.df['title'] == 'Data Scientist']
        sorted_data = data.sort_values('total_comp', ascending=False)
        return sorted_data.head(n)

    def get_low_earners(self, n):
        data = self.df[self.df['title'] == 'Data Scientist']
        sorted_data = data.sort_values('total_comp', ascending=True)
        return sorted_data.head(n)

    def get_salary_range(self, gender, race, years_of_experience, education, title):
    # Filter the data based on the user input criteria
        filtered_data = self.df[(self.df['years_of_experience'] >= years_of_experience) &
                                      (self.df['gender'] == gender) &
                                      (self.df['Race'] == race) &
                                      (self.df['Education'] == education) &
                                      (self.df['title'] == title)]
        if len(filtered_data) == 0:
            return "Sorry, no data available for your specified criteria"
        
        else:
            print(filtered_data)
            min_sal = filtered_data['total_comp'].min()
            max_sal = filtered_data['total_comp'].max()
            print ("Your estimated salary range should be between", min_sal, "-" ,max_sal)



#stack to get highest and lowest earners
#creates a list of salaries and prints them out
def analyze_salaries(df):
        salaries = list(df['total_comp'])
        max_salary = max(salaries)
        min_salary = min(salaries)
        avg_salary = sum(salaries) / len(salaries)
        print("Max salary: $",max_salary)
        print("Min salary: $",min_salary)
        print("Avg salary: $",avg_salary)
        
        # Create a stack of salaries
        salary_stack = []
        for salary in salaries:
            salary_stack.append(salary)
        
        # Pop salaries off the stack
        while salary_stack:
            print("Salary: $",salary_stack.pop())

       




    



#csv file methods

def read_csv_file(filename):
    df = pd.read_csv(filename)
    return df 

def write_csv_file(df):
    with open ('newfile.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(df)


