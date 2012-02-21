Feature: Search Tab Search
    As a user
    I want to download files
    So that I can view, play and store them

    Scenario: Download videos from a valid url via the Menu option
        Given I choose "Download from a URL" from the "File" menu
        When I enter a "valid" "<url>" in the dialog
        Then the item downloads
          And has the correct "<title>"
          And the video "<title>" is playable

    Examples:
        | url | title |
        | http://traffic.libsyn.com/dilbert/d285.m4v | MBA vs. Witch |

