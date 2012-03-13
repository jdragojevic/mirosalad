Feature: Download videos by url 
    As a user
    I want to download files
    So that I can view, play and store them

    Scenario: Download files from urls that Miro can recognize 
        When I download the item "<url>" 
        Then I have "<title>" in the "<item kind>" tab
            And I can verify the video "<title>" is playable

    Examples:
        | url | title |item kind |
        | http://pculture.org/feeds_test/short-video.ogv | short | Videos |
        #| http://traffic.libsyn.com/dilbert/d285.m4v | d285 | Videos |


