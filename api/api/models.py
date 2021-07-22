from django.db import models


class Department(models.Model):
    """部署モデル"""
    dept_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.dept_name


class Employee(models.Model):
    """従業員モデル"""
    name = models.CharField(max_length=50)
    join_year = models.IntegerField()
    department = models.ForeignKey(
        Department, related_name="employees", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
