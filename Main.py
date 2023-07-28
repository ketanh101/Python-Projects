from customlib import *

file_name = "PyMeth_DataSci_Salaries.csv"
print("Welcome, please choose an option below: " + "\n")


def main():
    
    dssal = DataScientist(file_name)
    #prompt user for choices
    print("1. Filter by Gender")
    print("2. Filter by Race")
    print("3. Get Top N highest/lowest paid data scientists")
    print("4. Compare Salaries based on Job Title")
    print("5. Compare Salaries based on Company")
    print("6. Analyze salaries")
    print("7. End Program")

    choice = int(input("Enter choice: "))


    #Get Data grouped by Gender
    if choice == 1:
        gender = input("Enter Gender (M, F, Other): ")

        filtered_data = dssal.filter_by_gender(gender)
        filtered_data = filtered_data.loc[filtered_data['title'] == 'Data Scientist']
        print(filtered_data.groupby('gender').head(10))

        filtered_data.groupby('gender').head(10).to_csv('gender.csv', index = False)

        main()

    #Get Data grouped by Race
    elif choice == 2:
        race = input("Enter Race (Asian, Black, Hispanic, Two Or More, White): ")

        filtered_data = dssal.filter_by_race(race)
        filtered_data = filtered_data.loc[filtered_data['title'] == 'Data Scientist']
        print(filtered_data)
        filtered_data.to_csv('race.csv', index = False)

        main()
    #Get the N Highest and N Lowest individual earners
    elif choice == 3:
        n = int(input("Enter N: "))
        highest_paid_employees = dssal.get_top_earners(n)
        lowest_paid_employees = dssal.get_low_earners(n)
        highest_paid_employees.iloc[:,[0, 1, 2, 3, 4, 6, 7, 8, 9]]
        lowest_paid_employees.iloc[:,[0, 1, 2, 3, 4, 6, 7, 8, 9]]

        print("Here are the top earning", n, " Data Scientists by total compensation", "\n")
        print(highest_paid_employees)
        print("\n","Here are the lowest earning", n, " Data Scientists by total compensation")
        print(lowest_paid_employees)
        conc = pd.concat([highest_paid_employees, lowest_paid_employees], ignore_index=True)
        conc.to_csv('highestlowest.csv', index=False)

        main()


    #Get the total comp, base salary, stock, and bonus. Compare Data Science salaries to other prominent tech roles
    elif choice == 4:
        role1 = 'Data Scientist'
        dsavg_salary = dssal.avg_comp(role1)
        dsavg_base = dssal.avg_base(role1)
        dsavg_stock = dssal.avg_stock(role1)
        dsavg_bonus = dssal.avg_bonus(role1)
        dsdf = pd.DataFrame({"role": role1, "avg_comp": dssal.avg_comp(role1), 
                             "avg_base": dssal.avg_base(role1), "avg_stock": dssal.avg_stock(role1), 
                             "avg_bonus": dssal.avg_bonus(role1)}, index=[0])
        
        role2 = 'Business Analyst'
        baavg_salary = dssal.avg_comp(role2)
        baavg_base = dssal.avg_base(role2)
        baavg_stock = dssal.avg_stock(role2)
        baavg_bonus = dssal.avg_bonus(role2)
        badf = pd.DataFrame({"role": role2, "avg_comp": dssal.avg_comp(role2), 
                             "avg_base": dssal.avg_base(role2), "avg_stock": dssal.avg_stock(role2), 
                             "avg_bonus": dssal.avg_bonus(role2)}, index=[0])
        
        role3 = 'Software Engineer'
        seavg_salary = dssal.avg_comp(role3)
        seavg_base = dssal.avg_base(role3)
        seavg_stock = dssal.avg_stock(role3)
        seavg_bonus = dssal.avg_bonus(role3)
        sedf = pd.DataFrame({"role": role3, "avg_comp": dssal.avg_comp(role3),
                              "avg_base": dssal.avg_base(role3), "avg_stock": dssal.avg_stock(role3), 
                              "avg_bonus": dssal.avg_bonus(role3)}, index=[0])
        
        df = pd.concat([dsdf, badf, sedf], ignore_index=True)
        
        #prints compensation breakdown for each role
        print("The Average Total Compensation for a",role1, "is:", "$", round(dsavg_salary), "\n", "Average Base Salary: ", round(dsavg_base), "\n", "Average Stock Grant: ", round(dsavg_stock), "\n", "Average Bonus: ", round(dsavg_bonus), "\n",)
        print("The Average Total Compensation for a",role2, "is:", "$", round(baavg_salary), "\n", "Average Base Salary: ", round(baavg_base), "\n", "Average Stock Grant: ", round(baavg_stock), "\n", "Average Bonus: ", round(baavg_bonus), "\n",)
        print("The Average Total Compensation for a",role3, "is:", "$", round(seavg_salary), "\n", "Average Base Salary: ", round(seavg_base), "\n", "Average Stock Grant: ", round(seavg_stock), "\n", "Average Bonus: ", round(seavg_bonus), "\n",)

        df.to_csv('multirolesals.csv', index = False)
        fig, ax = plt.subplots()
        df.plot(x='role', y=['avg_comp', 'avg_base', 'avg_stock', 'avg_bonus'], kind='bar', ax=ax)
        ax.set_ylabel('Salary (USD)')
        ax.set_title('Average Salary Breakdown by Role')
        plt.xticks(rotation=0)
        plt.show()
        ######################################
        main()
     

    
    #Get the average total compensation grouped by company
    elif choice == 5:
        df = pd.read_csv(file_name)
        dfds = df[df['title'] == 'Data Scientist']
        avg_comp = dfds.groupby('company')['total_comp'].mean().rename('total_comp').reset_index().round()

        avg_comp_top = avg_comp.sort_values('total_comp', ascending=False)
        avg_comp_low = avg_comp.sort_values('total_comp', ascending=True)

        print("The top paying Data Science companies are: ","\n", avg_comp_top.head(5),"\n")
        print("The lowest paying Data Science companies are: ","\n", avg_comp_low.head(5))

        conc = pd.concat([avg_comp_top.head(5), avg_comp_low.head(5)])
        conc.to_csv('compcompany.csv', index = False)


        #Generate a scatterplot showing where data science salaries range
        plt.figure(figsize=(10,6))
        sns.scatterplot(x="company", y="total_comp", data= avg_comp)
        plt.gca().set_xticklabels([])
        plt.title("Companies vs Total Yearly Compensation")
        plt.xlabel("Companies")
        plt.ylabel("Total Yearly Compensation ($)")

        plt.show()

        main()

   #shows box plot of all salaries based on years of experience
    elif choice == 6:
        df = pd.read_csv(file_name)
        dfds = df.loc[df['title'] == 'Data Scientist']
        salary_list = analyze_salaries(dfds)

        sns.boxplot(x=dfds['years_of_experience'], y=dfds['total_comp'])
        plt.title('Years of Experience vs. Total Compensation for Data Scientists')
        plt.xlabel('Years of Experience')
        plt.ylabel('Total Compensation ($)')
        plt.show()

        main()
        
    elif choice == 7:
        print("Thanks for trying the program")
    


    print("Refreshing...")

    
main()

