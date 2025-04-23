# Created by jackd at 4/22/2025
Feature: Test Scenarios for Reelly Setting Page
  # Enter feature description here

  Scenario: User can open the Reelly community page
    Given Open Reelly login page
    When Input signin email
    And Input signin password
    And Click Continue signin button
    And Click on Settings
    And Click on Community
    Then Verify Contact support button is clickable