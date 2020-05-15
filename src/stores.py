import numpy as np
import math

class StoreSchedulingProblem:
    """This class encapsulates the Stores Scheduling problem
    """

    def __init__(self, hardConstraintPenalty):
        """
        :param hardConstraintPenalty: the penalty factor for a hard-constraint violation
        """
        self.hardConstraintPenalty = hardConstraintPenalty

        # list of stores:
        self.stores = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        # stores' respective shift preferences - morning, evening, night:
        self.shiftPreference = [[1, 0], [1, 1], [0, 0], [0, 1], [0, 0], [1, 1], [0, 1], [1, 1]]

        # min and max number of stores allowed for each shift - morning, evening, night:
        store_total = len(self.stores)
        self.shiftMin = [math.ceil(70*store_total/100), math.ceil(70*store_total/100)]
        self.shiftMax = [store_total,store_total]

        # max shifts per week allowed for each stores
        self.maxShiftsPerWeek = 5

        # number of weeks we create a schedule for:
        self.weeks = 1

        # useful values:
        self.shiftPerDay = len(self.shiftMin)
        self.shiftsPerWeek = 7 * self.shiftPerDay

    def __len__(self):
        """
        :return: the number of shifts in the schedule
        """
        return len(self.stores) * self.shiftsPerWeek * self.weeks


    def getCost(self, schedule):
        """
        Calculates the total cost of the various violations in the given schedule
        ...
        :param schedule: a list of binary values describing the given schedule
        :return: the calculated cost
        """

        if len(schedule) != self.__len__():
            raise ValueError("size of schedule list should be equal to ", self.__len__())

        # convert entire schedule into a dictionary with a separate schedule for each store:
        storeShiftsDict = self.getStoreShifts(schedule)

        # count the various violations:
        consecutiveShiftViolations = self.countConsecutiveShiftViolations(storeShiftsDict)
        shiftsPerWeekViolations = self.countShiftsPerWeekViolations(storeShiftsDict)[1]
        storesPerShiftViolations = self.countStoresPerShiftViolations(storeShiftsDict)[1]
        shiftPreferenceViolations = self.countShiftPreferenceViolations(storeShiftsDict)

        # calculate the cost of the violations:
        hardContstraintViolations = consecutiveShiftViolations + storesPerShiftViolations + shiftsPerWeekViolations
        softContstraintViolations = shiftPreferenceViolations

        return self.hardConstraintPenalty * hardContstraintViolations + softContstraintViolations

    def getStoreShifts(self, schedule):
        """
        Converts the entire schedule into a dictionary with a separate schedule for each store
        :param schedule: a list of binary values describing the given schedule
        :return: a dictionary with each store as a key and the corresponding shifts as the value
        """
        shiftsPerStore = self.__len__() // len(self.stores)
        storeShiftsDict = {}
        shiftIndex = 0

        for store in self.stores:
            storeShiftsDict[store] = schedule[shiftIndex:shiftIndex + shiftsPerStore]
            shiftIndex += shiftsPerStore

        return storeShiftsDict

    def countDistanceViolations(self, storeShiftsDict):
        for i in range(0,13):
            for storeShifts in storeShiftsDict.values():
                if storeShifts[i]:
                    violations = violations + checkNeighboorhod(i, storeShiftsDict)
        return violations
    
    def countConsecutiveShiftViolations(self, storeShiftsDict):
        """
        Counts the consecutive shift violations in the schedule
        :param storeShiftsDict: a dictionary with a separate schedule for each store
        :return: count of violations found
        """
        violations = 0
        # iterate over the shifts of each store:
        for storeShifts in storeShiftsDict.values():
            # look for two cosecutive '1's:
            for shift1, shift2 in zip(storeShifts, storeShifts[1:]):
                if shift1 == 1 and shift2 == 1:
                    violations += 1
        return violations

    def countShiftsPerWeekViolations(self, storeShiftsDict):
        """
        Counts the max-shifts-per-week violations in the schedule
        :param storeShiftsDict: a dictionary with a separate schedule for each store
        :return: count of violations found
        """
        violations = 0
        weeklyShiftsList = []
        # iterate over the shifts of each store:
        for storeShifts in storeShiftsDict.values():  # all shifts of a single store
            # iterate over the shifts of each weeks:
            for i in range(0, self.weeks * self.shiftsPerWeek, self.shiftsPerWeek):
                # count all the '1's over the week:
                weeklyShifts = sum(storeShifts[i:i + self.shiftsPerWeek])
                weeklyShiftsList.append(weeklyShifts)
                if weeklyShifts > self.maxShiftsPerWeek:
                    violations += weeklyShifts - self.maxShiftsPerWeek

        return weeklyShiftsList, violations

    def countStoresPerShiftViolations(self, storeShiftsDict):
        """
        Counts the number-of-stores-per-shift violations in the schedule
        :param storeShiftsDict: a dictionary with a separate schedule for each store
        :return: count of violations found
        """
        # sum the shifts over all store:
        totalPerShiftList = [sum(shift) for shift in zip(*storeShiftsDict.values())]

        violations = 0
        # iterate over all shifts and count violations:
        for shiftIndex, numOfStores in enumerate(totalPerShiftList):
            dailyShiftIndex = shiftIndex % self.shiftPerDay  # -> 0, 1, or 2 for the 3 shifts per day
            if (numOfStores > self.shiftMax[dailyShiftIndex]):
                violations += numOfStores - self.shiftMax[dailyShiftIndex]
            elif (numOfStores < self.shiftMin[dailyShiftIndex]):
                violations += self.shiftMin[dailyShiftIndex] - numOfStores

        return totalPerShiftList, violations

    def countShiftPreferenceViolations(self, storeShiftsDict):
        """
        Counts the store-preferences violations in the schedule
        :param storeShiftsDict: a dictionary with a separate schedule for each store
        :return: count of violations found
        """
        violations = 0
        for storeIndex, shiftPreference in enumerate(self.shiftPreference):
            # duplicate the shift-preference over the days of the period
            preference = shiftPreference * (self.shiftsPerWeek // self.shiftPerDay)
            # iterate over the shifts and compare to preferences:
            shifts = storeShiftsDict[self.stores[storeIndex]]
            for pref, shift in zip(preference, shifts):
                if pref == 0 and shift == 1:
                    violations += 1

        return violations

    def printScheduleInfo(self, schedule):
        """
        Prints the schedule and violations details
        :param schedule: a list of binary values describing the given schedule
        """
        storeShiftsDict = self.getStoreShifts(schedule)

        print("Schedule for each store:")
        for store in storeShiftsDict:  # all shifts of a single store
            print(store, ":", storeShiftsDict[store])

        print("consecutive shift violations = ", self.countConsecutiveShiftViolations(storeShiftsDict))
        print()

        weeklyShiftsList, violations = self.countShiftsPerWeekViolations(storeShiftsDict)
        print("weekly Shifts = ", weeklyShiftsList)
        print("Shifts Per Week Violations = ", violations)
        print()

        totalPerShiftList, violations = self.countStoresPerShiftViolations(storeShiftsDict)
        print("Stores Per Shift = ", totalPerShiftList)
        print("Stores Per Shift Violations = ", violations)
        print()

        shiftPreferenceViolations = self.countShiftPreferenceViolations(storeShiftsDict)
        print("Shift Preference Violations = ", shiftPreferenceViolations)
        print()
        
        self.countDistanceViolations(storeShiftsDict)


# testing the class:
def main():
    # create a problem instance:
    stores = StoreSchedulingProblem(10)

    randomSolution = np.random.randint(2, size=len(stores))
    print("Random Solution = ")
    print(randomSolution)
    print()

    stores.printScheduleInfo(randomSolution)

    print("Total Cost = ", stores.getCost(randomSolution))


if __name__ == "__main__":
    main()

