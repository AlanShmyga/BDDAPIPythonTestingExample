Feature: Market Data
  Scenario: Verify server time
    When I make a request for server time
    Then Response contains a success status
    And Response contains no error
    And Response contains correct timestamp
    And Response contains correct human readable time

  Scenario Outline: Verify trading pair
    When I make a request for <from_asset>/<to_assset> trading pair
    Then Response contains a success status
    And Response contains no error
    And Response contains a trading pair description content
    And Response trading pair description contains valid altname <altname>
    And Response trading pair description contains valid <from_asset>/<to_assset> trading pair name
    And Response trading pair description contains minimum order value <ordermin>

    Examples: Trading pairs
    | from_asset | to_assset | altname | ordermin |
    | XBT        | USD       | XBTUSD  | 0.0001   |
