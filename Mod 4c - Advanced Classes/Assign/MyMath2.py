class MyMath:
    """
        Class used to request users to input numbers to add to the list.
        Average and standard deviation of the populated list will then be calculated.
    """

    def __init__(self, num_list = []):
        self.num_list  = num_list

    user_input = input("Enter a space-separated numbers to add to the list: ").split()
    num_list = [int(item) for item in user_input]


    def average(num_list):
        """Calculates and returns the average of a list of numbers."""
        
        sum = 0
        
        for num in num_list:
            sum = sum + num
        
        avg = sum / len(num_list)
        
        return avg


    def raisedDifference(num_list):
        """ 
            Calls the function "average" to calculate and return the average 
            of the raised difference of the list of numbers and the average. 
         """
        raisedDifference = 0
        sumRaisedDifference = 0
        
        for num in num_list:
            raisedDifference = (num - average(num_list)) ** 2
            sumRaisedDifference =  sumRaisedDifference + raisedDifference
        
        avg2 = sumRaisedDifference / len(num_list)
        
        return avg2
        
        
    def standardDeviation(num_list):
        """
            Calls the function "raisedDifference" to calculate 
            and return the standard deviation of the list of numbers.
        """
        from math import sqrt

        raisedDifference = 0
        
        
        standardDeviation = sqrt(raisedDifference(a))
        
        return standardDeviation

    averageOfList = average(num_list)
    stdDevOfList = standardDeviation(num_list)

    print(averageOfList)
    print(stdDevOfList)





