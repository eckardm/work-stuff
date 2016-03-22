## Administration tab

The Processing Configuration page of the Administration tab provides archivists with an easy form to configure processing defaults for a transfer or SIP. Changing the options using the web interface writes the necessary XML behind the scenes.

![Processing Configuration](images/processing-configuration.png)

Please consult with the Assistant Archivist for Digital Curation before changing any of the "Born-digital" processing defaults---while they should work for the majority of collections, there will undoubtably be exceptions to these rules! See the following explanations for more information:

  * **Send transfer to quarantine** should be set to **No** unless we need to quarantine a transfer to allow for virus definitions to update. Likewise, **Remove from quarantine after (days)** is not applicable because we will not be sending digital objects to quarantine.
  * **Generate transfer structure report** should be set to **Yes**. [Original order](http://www2.archivists.org/glossary/terms/o/original-order) is a fundamental principle of archives allowing us to preserve existing relationships and evidential significance that can be inferred from the context of the records and exploit the record creator's mechanisms to access the records.  
  * **Select file format identification command (Transfer)** should be set to **Seigfried version 1.0.0 PUID runs Identify using Siegfried**. Siegfried, while slower, especially for larger files, is sometimes more accurate than FIDO and is better at recognizing contaner formats, such as the Office Open XML format.
  * **Extract packages** should be set to **Yes** so that content from zipped or otherwise packaged content will be extracted.
  * **Delete packages after extraction** should be set to **Yes**, as we're most interested in preserving what's contained in the packages, not the packages themselves.
  * **Examine contents** should be set to **Yes**. This will allow us to check for Personally Identifiable Information (PII), like Social Security numbers and credit card numbers, during the Appraisal step.
  * **Create SIP(s)** should be set to **Send to backlog**, as this will allow us make use of the Appraisal tab later. The Assistant Archivist for Digital Curation will keep track of exceptions to this rule. 
  * **Select file format identification command (Ingest)** should be set to **Seigfried version 1.0.0 PUID runs Identify using Siegfried**. See above.
  * **Normalize** should be set to **Normalize for preservation**, which will create preservation copies of the original objects. Note that the original objects are always kept along with their normalized versions.
  * **Approve normalization** should be set to **Yes** because we want to process material as efficiently as possible and it is unrealistic to *manually* approve normalization for every file.
  * **Reminder: add metadata if desired** should be set to **Continue**. The Appraisal tab allows archivists to create descriptive metadata and PREMIS Rights Statements.
  * **Transcribe files (OCR)** should be set to **Yes** due to the enormous potential of Optical Character Recognition (OCR) for improving access to material. 
  * **Select file format identification command (Submission documentation & metadata)** should be be set to **Seigfried version 1.0.0 PUID runs Identify using Siegfried**. See above.
  * **Select compression algorithm** should be set to **Uncompressed**. Compression adds a layer of complexity to an AIP, making it harder to preserve, and will only be considered if storage becomes an issue. Likewise **Select compressing level** is not applicable and should be set to **None**.
  * **Store AIP** should be set to **Yes** so that we're processing material as efficiently as possible.
  * **Store AIP location** should be set to **aip storage (bhl-archivematica)**. This location managed by MLibrary.
  * **Store DIP location** should bet set to **None**. It is not applicable as we will not be creating DIPs.
  
If you do change any of the "Born-digital" processing defaults, be sure to hit the **Save** button.
  
***

[Digital Processing](digital-processing.md)
  * **Administration**
  * [Appraisal](appraisal.md)
  * [Description and Arrangement](arrangement.md)
  * [Ingest](ingest.md)

