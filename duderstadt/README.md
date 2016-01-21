This is a legacy cleanup-type project. We had some files taken from CDs belonging to Duderstadt. Some of these got processed for a FOIA request and put online. This project attempts to reconcile all of the legacy data (account for and update what got processed, account for and attempt to process what didn't get processed, and account for everything else he's added since then).

Do the heavy lifting in these parts:
  
  1. Collect all the existing metadata that's on those HTML pages using **get_metadata.py**. This makes **metadata.p** and essentially gives you the *something like* the original filename, a date, and the name of the preservation version (taken from the anchor's href attribute's value), that is, the "JJD" version of the files.
  2. We'll also need information on what files got converted with AutoPro. Do that with **get_converted_files.py**, which outputs **converted_files.p**. To be clear, these were made before the broader scope of the project was determined--these are simply updated preservation versions of the "JJD" version of the files.
  3. Next we do the real heavy lifting. **make_information_packages.py** attempts to use the outputs of the above and collect every piece of information we'll ever need (before depositing content to DeepBlue). It goes through the original filelist and collects the following information, outputing it to **information_packages.p**:
    * series
    * subseries
    * accessrestrict
    * unittitle
    * original
    * original_location
    * unitdate
    * preservation (best that can be done here using fuzzywuzzy)
    * preservation_location
    * autopro
    * autopro_location
  4. **make_deepblue_metadata.py** uses **information_packages.p** to make the CSV we need to send to Jose for DeepBlue. CHANGING THIS ONE will cause the least amount of "rippling affect" damage.
  
*Note: At this point, the files themselves (with the exception of a copy of the originals, which are in the 9811_0003 folder) have been copied/moved to the MLibrary/DeepBlue folder.*
    