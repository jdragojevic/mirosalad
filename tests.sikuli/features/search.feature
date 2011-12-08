Feature: Search Tab Search
    As a user
    I want to be able to find videos from common search engines
    So that I can download them and save them as feeds


    Scenario: Perform a search
        Given I am on the search tab
        When I enter a search for "<search>" using the search engine "<engine>"
        Then search results are displayed for "<search>"
            And I see the Save as Podcast button

    Examples:
        | search | engine |
        | monkey | youtube |
