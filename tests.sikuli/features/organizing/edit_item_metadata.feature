Feature: Edit Item Metadata
    As a user
    I want to change the file type setting


Scenario Outline: Drag an item to a Library tab to change the type

Given I have "<item name>" in the "<tab>" tab
When I drag "<item name>" to the "<new type>" tab
Then I can verify "<item name>" has the characteristics of a "<new type>" item

Examples:
    | tab | new type | item name |
    | Videos | Music | Tongue |
    | Music | Videos | Paris |


Scenario Outline: Use the Edit Item Details panel to change item type.

Given I have "<item name>" in the "<tab>" tab
When I edit the "<type>" metadata to "<new type>" for "<itme name>"
Then I can verify "<item name>" has the characteristics of a "<new type>" item

Examples:
    | tab | new type | item name |
    | Videos | Music | Tongue |
    | Music | Video | Sample|
    | Misc  | Video | CIRCUS |
 
 
Scenario Outline: Edit Album Art

Given I have "<item name>" in the "<tab>" tab
When I change the "art" field to "<art file>"
Then I can verify the "<item name>" has the "<art file>" thumbnail image

Examples:
    | item name | tab | art file | 
    | Pancakes  | Music | album_art1.jpg |
    | summer    | Videos | album_art1.jpg | 

            
