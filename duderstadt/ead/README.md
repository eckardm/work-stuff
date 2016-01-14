Duderstadt EAD
==============

Description
-----------
Use DSpace stats  and metadata scraped from DSpace full item record to update Duderstadt EAD with component physloc, unitdate, physdesc/physfacet, dao href and dao/daodesc, as well as accessrestrict where appropriate.

Considerations: 

  * This is all item-level stuff even though we don't normally do item-level description. 
  * Components should be nested under appropriate series and subseries. For the recent large deposit, you should be able to tell what series and subseries based on the filename, which follows this convention: Digital Documents - University of Michigan Presidency, 1986-1997 - [series] - [subseries] - [unittitle]. For everything else, it should go into a new subseries of Faculty Archives, YYYY-ongoing, sorted by date. Once you know the oldest date, you can make that the YYYY.
  * Some series are restricted (and would get series-level accessrestrict), while some items in open series are restricted (and would get item-level accessrestrict). 
  * Look in dc.date.issued for unitdate, even though that's not our normal convention.
  * You could throw in some normal attributes for those unitdates.
  * Every once in a while there may be an item-level dc.description.abstract, which could be incorporated in the EAD somehow.
