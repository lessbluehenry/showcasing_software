*** Settings ***
Documentation     testing math
...
Resource          CentralResourceCollection.resource

*** Test Cases ***
checking simple addition
    [Documentation]  describing description
    [Tags]  tid:0003  MATH  SANITY  PLUS
    I ensure 1 plus 2 equals 3

checking three digits addition
    [Documentation]  describing description
    [Tags]  tid:0003  MATH  BIG NUMBERS  PLUS
    I ensure 123 plus 876 equals 999

checking simple subtraction
    [Documentation]  describing description
    [Tags]  tid:0003  MATH  MINUS
    I ensure 6 minus 2 equals 4

checking three digits subtraction
    [Documentation]  describing description
    [Tags]  tid:0003  MATH  BIG NUMBERS  MINUS
    I ensure 789 minus 123 equals 666

