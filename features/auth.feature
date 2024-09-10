Feature: Authentication

  Scenario: User can login
    Given I am a user with id "1"
    When I register
    Then I should receive a token
    And I should be able to login with the token