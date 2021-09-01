
*** Settings ***
Documentation     A test suite with a single test for opening chrome browser.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          CentralResourceCollection.resource

*** Test Cases ***
open some pages
    [Documentation]  describing description

    [Tags]  tid:0001  RELEASE  SYSTEM  RISK-391  CHROME

    I open Chrome browser
    I open webpage "https://www.python.org/"
    I wait 0.2 seconds
    I open webpage "https://reservierung.donaubad.de/"
    I wait 0.2 seconds
    I close Chrome browser

open python page
    [Documentation]  describing description

    [Tags]  tid:0001  SYSTEM  CHROME

    I open Chrome browser
    I open webpage "https://www.python.org/"
    I wait 2 seconds
    I close Chrome browser

