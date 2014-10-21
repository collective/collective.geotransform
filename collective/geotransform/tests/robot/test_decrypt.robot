*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Scenario: Test emails decryption
     When I go to the document 'simple-document'
      And I am sure that the mails were obfuscated by transform
     Then the emails should be readable for user


*** Keywords ***

I go to the document '${document_title}'
    Go to  ${PLONE_URL}/${document_title}


I am sure that the mails were obfuscated by transform
    Page Should Contain Element  xpath=//a[@class='link-mailto' and @rel='nofollow' and contains(text(), 'Contact you')]
    Page Should Contain Element  xpath=//a[@class='link-mailto' and @rel='nofollow' and contains(text(), 'Contact them')]


the emails should be readable for user
    Page Should Contain  Contact me at me@me.com
    Page Should Contain  Contact you
    Page Should Contain  Contact them
    Page Should Contain Element  xpath=//a[@href='mailto:you@you.com']
    Page Should Contain Element  xpath=//a[@href='mailto:them@them.com?subject=supersub']
