Feature: OrangeHRM logo
  Scenario: Logo presence on OrangeHRM home page
    Given launch Chrome browser
    When open Orange HRM home page
    Then verify that the logo present on page
    And cloe browser