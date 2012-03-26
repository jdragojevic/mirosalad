Feature: Hybrid view filter
 - Hybrid view filter is only available on the tabs where it makes sense to display grouped items.  For Music tabs it groups by Album, for Video displays it groups by series (generic term for Show name, podcast and last folder).
 - Sidebar tabs that have a hybrid view option:
  - Videos
  - Music
  - Misc
  - Devices
    - Music tab
    - Videos tab
  - Podcasts (top level tab)
  - Watched Folders
  - Playlists
 - Sidebar tabs that do not have a hybrid view option:
  - Downloading
  - Feeds
  
Scenario Outline: Hybrid View Available on Static tabs
    When I am on the "<tab>" sidebar tab
    Then I see the "Hybrid Filter" button

Examples:
    |tab|
    |Videos|
    |Music |
    |Podcasts|

Scenario Outline: Hybrid View Available on Hideable tabs
    Given the "<tab>" is present
    When I am on the "<tab>" sidebar tab
    Then I see the "Hybrid Filter" button

Examples:
    |tab|
    |Misc|
    |Playlists |
    |Watched Folders|

Scenario Outline: Hybrid View NOT Available
    Given the "<tab>" is present
    When I am on the "<tab>" sidebar tab
    Then I do not see the "Hybrid Filter" button

Examples:
    |tab|
    |podcast|
    |Downloading |
