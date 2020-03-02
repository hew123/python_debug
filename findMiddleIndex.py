
#
# Complete the 'balancedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY sales as parameter.
#

def balancedSum(sales):
    # Write your code here
   sum_left = sales[0]
   sum_right = sum(sales[2:])
   if sum_left == sum_right:
        return 1
   else:
        for index in range(1,len(sales)):
            sum_left += sales[index]
            sum_right -= sales[index+1]
            if sum_left == sum_right:
                return index+1

def main():
    sales = [1,2,3,3]
    print(balancedSum(sales))

main()