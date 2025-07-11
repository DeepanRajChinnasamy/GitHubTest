*** Settings ***
Library    RequestsLibrary
Library    OperatingSystem
Library    Response.py
Library    CustomLib.py

*** Variables ***
${GraphqlURL}    https://api.wileyas.qa2.viax.io/graphql
${Environment}    qa2
${PPURL}         https://wileyas.qa2.viax.io/price-proposals

*** Test Cases ***
Post JSON To GraphQL
    ${token}=    get token    auth.wileyas.${Environment}.viax.io
    ${JsonResp}=  Evaluate  ${token}
    @{list}=     CustomLib.Get Value From Json    ${JsonResp}    $.access_token
    ${AuthToken}=    set variable    ${list}[0]
    set suite variable    ${AuthToken}    ${AuthToken}
    Create Session    order_session    ${PPURL}    verify=True
    ${headers}=    Create Dictionary    Content-Type=application/json    Authorization=Bearer ${AuthToken}
    ${json_content}=    Get File    Institutional.json
    ${response}=    Post On Session    order_session    url=${GraphqlURL}    data=${json_content}    headers=${headers}
    Log    ${response.status_code}
    Log    ${response.text}
    Should Be Equal As Integers    ${response.status_code}    200
