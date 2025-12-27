##today first morning sum is about the database 

'''
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |

'''

##like i have to find the one empolyee who earns more than his manager 
##step = 1

##so got the intially i learned today how to select two manuplation in one table 
## first 
## select * from emp as a,emp as b

#step = 2

##so and then i need the info like emp with thier manger info

#step = 3

##lastly i compared them with double condition in the where statement 

##select  * from emp as a ,emp as b 
##where  a.salary = b.salary and a.salary > b.salary\\


'''
select a.name as empolyee 
from empolyee as a ,empolyee as b
where a.managerid = b.id and a.salary > b.salary 
'''
###final query for the 
##select a.name as empolyee 