*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://api.wileyas.qa2.viax.io/graphql
${RESOURCE}   https://wileyas.qa2.viax.io/price-proposals

*** Test Cases ***
Test JSON Placeholder API
    [Documentation]    Sample GET request
    Create Session    myapi    ${BASE_URL}
    ${response}=    GET    myapi    ${RESOURCE}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
