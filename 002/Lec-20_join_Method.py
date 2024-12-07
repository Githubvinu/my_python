from loguru import logger
logger.info("*****Join Method****88")

lst = ['A','1','B','2','C','3']
result = " # ".join(lst)
print(result)

dst = {'rahul':500,'vinay':1000,'mohan':550}
rslt_1 = " ".join(dst)
print(rslt_1)

state_dept_info = [{"state":"Bihar","department":"IT"},
{"state":"Delhi", "department": "Marketing"}]
print(state_dept_info)

query = """select * from(
select e.employee_name, e.state, e.zip, e.salary ,d.department
from employee_tbl e
inner join department d
ON e.emp_id = d.emp_id
)a
where salary>100000 """
print(query)

final_condation = []
for i in state_dept_info:
    for key,value in i.items():
        final_condation.append(f"{key}='{value}'")
print(final_condation)

final_condation = " OR ".join(final_condation)
print(final_condation)

final_query = query + " AND (" + final_condation + ")"
print(final_query)

