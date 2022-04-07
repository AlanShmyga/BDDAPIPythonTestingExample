Feature: User Data

  Scenario: Verify Open Orders
    Given I am a registered user
    When I make a request for my open orders
    Then Response contains a success status
    And Response contains no error
    And Response contains correct open orders