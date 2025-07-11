*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://wileyas.qa2.viax.io/price-proposals
${RESOURCE}    https://api.wileyas.qa2.viax.io/graphql

*** Test Cases ***
Test JSON Placeholder API
    [Documentation]    Sample GET request
    Create Session    myapi    ${BASE_URL}
    ${response}=    GET    myapi    ${RESOURCE}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${response.json()}
