'''
A financial app tracks a user's monthly income, expenses, and a savings goal. Calculate the remaining balance by subtracting expenses from income. If the balance is negative, print "Debt". If the balance is zero or positive, check if it satisfies the savings goal to print "Goal Met", otherwise print "Below Goal". Input Format: Three space-separated numbers representing income, expenses, and savings goal. Output Format: A single string showing the financial status.
'''
def solve():
    data = input().split()
    income = float(data[0])
    expenses = float(data[1])
    goal = float(data[2])
    
    balance = income - expenses
    
    if balance < 0:
        print("Debt")
    else:
        if balance >= goal:
            print("Goal Met")
        else:
            print("Below Goal")

if __name__ == "__main__":
    solve()