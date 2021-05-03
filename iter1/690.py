"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        sum_ = 0
        employees = {employee.id: employee for employee in employees}
        def dfs(employee):
            nonlocal sum_, employees
            sum_ += employee.importance
            for subordinate in employee.subordinates:
                dfs(employees[subordinate])
        dfs(employees[id])
        return sum_


