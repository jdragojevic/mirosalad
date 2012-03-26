== Hybrid Album View ==

Narrative:
* '''As''' a miro user
* '''I''' want to view my files grouped by Album / Artist for music, or other logical groupings.
* '''So''' that I can easily find related content.


== Features == 

=== Feature: General Hybrid View Design ===
The hybrid view should show an album  / album art on the left and the tracks to the right.
==== Scenario: Display Track Numbers ==== 
* '''Given''' I am in the Hybrid view
* '''When'''  There are items present in the tab
* '''Then'''  Track numbers display on the right of the album art cell view and are not selectable

==== Scenario: Album with 7 items or more ==== 
* '''Given''' I am in the Hybrid view
* '''When'''  An album has 7 items or more
* '''Then'''  Album art is displayed in the 1st column
** '''And''' There is padding at the top of each album to push the album art down away from the chrome. 
** '''And''' This padding is not clickable. 

==== Scenario: Album with less than 7 items ==== 
* '''Given''' I am in the Hybrid view
* '''When'''  An album has less than 7 items
* '''Then'''  Only text (Album / Artist info) is displayed in the 1st column.

==== Scenario: Mulitple albums in the display ==== 
* '''Given''' I am in the Hybrid view
* '''When'''  There is more than 1 album present
* '''Then'''  A faint divider line is displayed between each album.

==== Scenario: Default Sort Display ==== 
* '''Given''' I am in the Hybrid view for the first time
* '''When'''  There is more than 1 album present
* '''Then'''  Albums are sorted Alphabetically by Album Name 
* Bugs: 
** [[bz:18270]] storing sort configurations separately.

==== Scenario: Unknown Album / Artist ====

==== Scenario: Compilation Albums 1 Album / Multiple Artists ====

==== Scenario: Greatest Hits ====

=== Feature: Clickable actions in the Hybrid View ===

==== Scenario: Single Click on the Album art cell ==== 
* '''Given''' I am in the Hybrid view
* '''When'''  I click on the Album art
* '''Then'''  The first item in the album is selected.

==== Scenario: Double Click on the Album art cell ==== 
* '''Given''' I am in the Hybrid view
* '''When'''  I click on the Album art
* '''Then'''  The first item in the album starts playback
* Bugs: [[bz:18276]]

==== Scenario: Right Click on the Album art cell ==== 
* '''Given''' I am in the Hybrid view
* '''When'''  I right-click on the Album art
* '''Then'''  All album items are selected 
** '''And''' Context menu appropriate to the selected items is displayed. 
* Bugs: [[bz:18277]]

=== Feature: Sorting in the Hybrid View ===
Sorting in the Hybrid view should always be a secondary sort - maintaing album / artist as the primary sort.
* Bugs: [[bz:18251]]

==== Scenario: Click on Sort Headers ==== 
* '''Given''' I am in the Hybrid view
* '''When'''  I click any sort
* '''Then'''  Items in the view are sorted by selected sort

==== Scenario: Default Sort for Podcasts Top level tab ==== 
* '''Given''' I am on the Top-level Podcats tab
* '''When'''  I click on the Hybrid view
* '''Then'''  Items from watched folders are sorted to the bottom of the list. 
* Bugs: [[bz:18278]]

=== Feature: Hybrid view display / availability on Sidebar tabs. ===
Hybrid tab is appropriate for some Sidebar tab, but not all.  
Some tabs needs some specific tailoring.

==== Scenario: Hybrid View on Music tab ====
* '''Given''' that Miro is open
* '''When'''  I click on the MUSIC tab
* '''Then'''  3-toggle view filter is displayed

==== Scenario: Hybrid View on Videos tab ====
* '''Given''' that Miro is open
* '''When'''  I click on the VIDEOS tab
* '''Then'''  3-toggle view filter is displayed

==== Scenario: NO Hybrid View on Search tab ====
* '''Given''' that Miro is open
* '''When'''  I click on the SEARCH tab
* '''Then'''  2-toggle view filter is displayed (No Hybrid View)

==== Scenario: NO Hybrid View on Downloading tab ====
* '''Given''' that Miro is open
* '''When'''  I click on the DOWNLOADING tab
* '''Then'''  2-toggle view filter is displayed (No Hybrid View)

====Scenario: NO Hybrid View on Conversions tab ====
* '''Given''' that Miro is open
* '''When'''  I click on the MUSIC tab
* '''Then'''  2-toggle view filter is displayed (No Hybrid View)

==== Scenario: NO Hybrid View on Connect: Miro Shares tab: All Sub tabs ====
* '''Given''' that Miro is open
* '''When'''  I click on the CONNECT tab
** '''And'''  I click on a Miro Share sub tab (Music, Videos, Podcasts)
* '''Then'''  2-toggle view filter is displayed (No Hybrid View)

==== Scenario: Hybrid View on Connect: Devices: Music tab ====
* '''Given''' that Miro is open
* '''When'''  I click on the Connect tab
** '''And''' I click on a Device sub-tab
** '''And''' I click on the MUSIC sub-tab
* '''Then'''  3-toggle view filter is displayed

==== Scenario: Hybrid View on Connect: Devices: Videos tab ====
* '''Given''' that Miro is open
* '''When'''  I click on the Connect tab
** '''And''' I click on a Device sub-tab
** '''And''' I click on the VIDEO sub-tab
* '''Then'''  3-toggle view filter is displayed

==== Scenario: Hybrid View on PODCASTS tab: top level ====
* '''Given''' that Miro is open
* '''When'''  I click on the PODCASTS tab
* '''Then'''  3-toggle view filter is displayed

==== Scenerio: Show the podcast image / title in PODCASTS top-level album/artist column ====
* '''Given''' that Miro is open
* '''When'''  I click on the PODCASTS tab
* '''Then'''  The Album/Artist column displays the Feed Thumbnail and the Feed Name.
* Bugs: [[bz:18231]]

==== Scenario: NO Hybrid View on Podcasts secion: individual podcasts ====
* '''Given''' that Miro is open
* '''When'''  I click on a podcast tab
* '''Then'''  2-toggle view filter is displayed (No Hybrid View)

==== Scenario: Hybrid View on Podcasts section: watched folders ====
* '''Given''' that Miro is open
* '''When'''  I click on a WATCHED FOLDER tab
* '''Then'''  3-toggle view filter is displayed
