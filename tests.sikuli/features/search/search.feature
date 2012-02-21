@search
Feature: Search Tab Search
    As a user
    I want to be able to find videos from common search engines, urls and podcasts
    So that I can download them and/or save them as feeds


    Scenario: Perform a search engine search
        Given I am on the "Search" sidebar tab
        When I enter a search for "<search>" using the search engine "<engine>"
        Then results are displayed for "<search>"
            And I see the "Save as Podcast" button

    Examples:
        | search | engine |
        | monkey | youtube |
