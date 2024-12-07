from loguru import logger

list_of_number = ['2','1','23','101','222','555']
print(list_of_number)

#need to merge all data
#way !
rst = ""
for number in list_of_number:
    rst = rst + " " + number

print(rst)

#way to using JOIN
result = "_".join(list_of_number)
print(result)

labout_with_cost = {"Mahesh":500,"Ramesh":400,"mithlesh":600,"parmesh":800}
print(labout_with_cost)

result_1 = " # ".join(labout_with_cost)
print(result_1)


state_dept_info = [{"state": "Bihar", "department":"IT"},{"state":"Delhi","department":"Marketing"}]
print(state_dept_info)

query = """ select * from (
select e.employee_name, e.state, e.zip, e.salary ,d.department
from employee_tbl e
inner join department d
ON e.emp_id = d.emp_id
)a
where salary>100000 """
print(query)
print("\n")
filter_condation = []
for condation in state_dept_info:
    for key,values in condation.items():
        filter_condation.append(f"{key}={values}")

print(filter_condation)

result_2 = " OR ".join(filter_condation)
print(result_2)

print(query + " AND " + result_2)

