"""" conditionals
     conditionals allow you to make specific code execution choices
     based a certain condition.It allows you to ask  questions.

     1.> - Greater than
     2.>= - Greater than or equal to
     3.< = - Less than
     4.<= - Less than or equal to
     5.== - Strict comparison
     6. != - not equal to
     7. = - Assignment operator
     8. if - statement that allows you to check conditions

"""
"""
Example.1
Code block Example:Covers using "if statement".
Check to see if x is less  than y using an if statement
"""
x = int(input("What's x "))

y = int(input("What's y "))

# if x < y:
#     print("X is less than y")
# if y < x:
#     print("y is less than x")
# if x == y:
#     print("x is equal to y")
""" Topic End"""
"""
Designs flaws with the code above.

1.if statement used frequently,repetitive code.

-Design solution for code, elif .This would stop
 the task based on certain conditions ,preventing
 unnecessary computation or repetitive code.


Example 2.
Using elif- to solve repetitiveness of using the 
if statement. If the statement returns true,then  the code
execution will be stopped.
"""

# if x < y:
#     print("x is less than y ")
# elif x > y:
#     print("x is greater than y ")
# elif x == y:
#     print("x is equal to y ")

""" Topic End """

"""
Example 3.
Using else-  If a third check does not need to be performed,
the else statement(keyword) can be used.
By using the else keyword, the code does not perform the
third check , being that x could only be 1 of 3 solutions,
Properly using if,elif, and else, optimizes the codes performance.
(< , >, =).
"""
# if x < y:
#     print("x is less than y ")
# elif x>y:
#     print("x is greater than y")
# else:
#     print("x is equal to y ")
"""Topic End"""

"""
Example 4.
Using or- This keyword will allow for multiple conditions
to be checked.
"""

# if x > y or x <y:
#     print("x is not equal to y ")
# else:
#     print("x is equal to y ")
"""Topic End"""

"""
Example 5.
Using and - This keyword will allow for multiple conditions to be
checked and returns true if both conditions are met.
"""