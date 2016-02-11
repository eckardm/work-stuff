Appraisal
=========

[Appraisal](http://www2.archivists.org/glossary/terms/a/appraisal), or the process of determining whether records and other materials have permanent (archival) value, is a fundamental archival principle. The Appraisal feature in Archivematica allows archivists to:

  1. review and appraise files in a particular transfer; 
  2. logically arrange digital content with archival description from ArchivesSpace; and
  3. ingest SIPs and deposit AIPs from Archivematica into DSpace, including metadata linked from ArchivesSpace.
  
![Appraisal and Arrangement tab](appraisal-arrangment.png)

Preliminaries
-------------

The design of the Appraisal tab is based on the idea of having different "panes" which can be toggled on and off as needed. When the tab is loaded, the **Backlog** and **Analysis** panes are loaded. Clicking on the other pane options (i.e., **File List** or **ArchivesSpace**) will load those panes; any pane can be removed from view by clicking again.

![Toggling](toggling.png)

Backlog
-------

Search the backlog by **Accession number** to pull up all transfers associated with a particular accession.

![Searching the Backlog by Accession Number](backlog-accession-number.png)

Alternatively, search the backlog using the **Path** option to search by transfer title (part of the path). Note that Archivematica sanitzes file and folder names as part of it's initial **Transfer** microservices--any spaces will have been replaced with underscores.

![Searching the Backlog by Path](backlog-path.png)

Note that in the image above, Events_2006 is crossed out because the everything in that transfer has already been ingested.

To explore a transfer, click on folder icons to expand the contents of that folder. To collapse the contents of a particular folder, click again on the icon. Digital content is located in the "objects" folder. Tags may be applied in the **Backlog** pane---see **Tagging** below.

![Exploring a Transfer](explore-transfer.png)

Appraisal
---------

Select one or more folders from the backlog search results by clicking on the folder's name. You can choose an entire transfer, a folder within a transfer or individual files. 

### Objects

Click on **Objects** in the **Analysis** pane to see a report of file types and sizes and sizes. Click **Report** to see information on file format, PRONOM PUID (clicking on this field will take you to a summary from PRONOM's technical registry), Archivematica FPR Group, number of files and size in tabular form.

![Report]()

Click on **Visualizations** to see information on formats by either total number of files or total size of files in a pie chart.

![Visualizations]()

### File list

Ensure that the **File List** pane is toggled on. Clicking on a format type in the **Objects** report or a wedge of the pie chart visualization will populate the **File List** pane with information on files of that format type, including filename, size and last modified date. Tags may be applied and files may be previewed from the **File List** pane---see **Tagging** and **Preview file** below.

![File List](file-list.png)

### Tags

Click on **Tags** in the **Analysis** pane to see a see a report of tags that have been applied to a particular selection in a transfer and their counts. See **Tagging** below.

![Tags](tags.png)

### Examine contents

Click on **Examine Contents** in the **Analysis** pane to see [bulk_extractor](http://forensicswiki.org/wiki/Bulk_extractor) log content for Personably Identifiable Information (PII), including Social Security numbers, as well as credit card numbers. Click on a file name to see a tabular view of content and surrounding context from the bulk_extractor report. Click on **Bulk Extractor logs** to download the logs for local analysis in BEViewer, if necessary. Tags may be applied and files may be previewed from **Examine contents**---see **Tagging** and **Preview file** below. 

!

### Preview file

To preview a file in **Preview file** in the **Analysis** pane, click on a filename from the **File List** pane or **Examine contents** in the **Analysis** pane. If your browser has a viewer for the format, it will appear. Alternatively, all files can be downloaded for local analysis:

  * Use **Quick View Plus** to review the content of most files.
  * Use **VLC Media Player** to review the content of audio/video files.
  * Use **IrfanView** to review the content of raster images.
  * Use **Inkscape** to review the content of vector images.
  
!

Tagging
-------

Dessert lollipop danish muffin. Chocolate lollipop caramels sesame snaps dragée caramels jujubes. Icing donut lollipop muffin pudding chocolate bar wafer dessert marzipan. Wafer cake candy croissant brownie chocolate bar fruitcake toffee. Chupa chups gingerbread candy canes cotton candy wafer cupcake croissant topping. Soufflé tiramisu macaroon donut cotton candy. Chocolate bar chocolate fruitcake. Brownie sesame snaps powder chocolate bar. Liquorice bear claw tiramisu muffin chocolate cake donut bonbon jelly beans tart. Pie sesame snaps chocolate cake candy. Soufflé croissant cheesecake halvah halvah pie. Sweet roll jelly cheesecake chocolate carrot cake liquorice. Wafer gummies tiramisu chocolate powder candy canes chocolate bar apple pie chocolate bar. Gummi bears topping gingerbread jelly-o.

### From the **Backlog**

Dessert lollipop danish muffin. Chocolate lollipop caramels sesame snaps dragée caramels jujubes. Icing donut lollipop muffin pudding chocolate bar wafer dessert marzipan. Wafer cake candy croissant brownie chocolate bar fruitcake toffee. Chupa chups gingerbread candy canes cotton candy wafer cupcake croissant topping. Soufflé tiramisu macaroon donut cotton candy. Chocolate bar chocolate fruitcake. Brownie sesame snaps powder chocolate bar. Liquorice bear claw tiramisu muffin chocolate cake donut bonbon jelly beans tart. Pie sesame snaps chocolate cake candy. Soufflé croissant cheesecake halvah halvah pie. Sweet roll jelly cheesecake chocolate carrot cake liquorice. Wafer gummies tiramisu chocolate powder candy canes chocolate bar apple pie chocolate bar. Gummi bears topping gingerbread jelly-o.

!

### From the **File List**

Dessert lollipop danish muffin. Chocolate lollipop caramels sesame snaps dragée caramels jujubes. Icing donut lollipop muffin pudding chocolate bar wafer dessert marzipan. Wafer cake candy croissant brownie chocolate bar fruitcake toffee. Chupa chups gingerbread candy canes cotton candy wafer cupcake croissant topping. Soufflé tiramisu macaroon donut cotton candy. Chocolate bar chocolate fruitcake. Brownie sesame snaps powder chocolate bar. Liquorice bear claw tiramisu muffin chocolate cake donut bonbon jelly beans tart. Pie sesame snaps chocolate cake candy. Soufflé croissant cheesecake halvah halvah pie. Sweet roll jelly cheesecake chocolate carrot cake liquorice. Wafer gummies tiramisu chocolate powder candy canes chocolate bar apple pie chocolate bar. Gummi bears topping gingerbread jelly-o.

!



Arrangement to ArchivesSpace
----------------------------

Dessert lollipop danish muffin. Chocolate lollipop caramels sesame snaps dragée caramels jujubes. Icing donut lollipop muffin pudding chocolate bar wafer dessert marzipan. Wafer cake candy croissant brownie chocolate bar fruitcake toffee. Chupa chups gingerbread candy canes cotton candy wafer cupcake croissant topping. Soufflé tiramisu macaroon donut cotton candy. Chocolate bar chocolate fruitcake. Brownie sesame snaps powder chocolate bar. Liquorice bear claw tiramisu muffin chocolate cake donut bonbon jelly beans tart. Pie sesame snaps chocolate cake candy. Soufflé croissant cheesecake halvah halvah pie. Sweet roll jelly cheesecake chocolate carrot cake liquorice. Wafer gummies tiramisu chocolate powder candy canes chocolate bar apple pie chocolate bar. Gummi bears topping gingerbread jelly-o.

[Administration](administration.md) | **Appraisal** | [Ingest](ingest.md)