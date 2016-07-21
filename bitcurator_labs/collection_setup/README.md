**collection_setup.py** works in Windows.

**collection_setup.py** works in the BitCurator Ubuntu distribution.

Dependencies:
  * Shared folders
  * Logitech Webcam folder
  * ImageMagick
  * Beautiful Soup
  
Dependencies
============

Shared folders
--------------

If you wish to move processed materials back to your host machine from the BitCurator VM, you can set up a shared folder that both the host and the VM can write to. In the Shared Folders tab of BitCurator's Settings, click the folder with the green “plus” on it to choose a folder on your host machine to share.sudo

![Add Share](add_share.png)

Collection Setup assumes that you've created a shared folder in BitCurator called "sf_Collections_Processing" mapped to someplace on your local machine.

Logitech Webcam folder
----------------------

Collection Setup assumes that you've got a folder called "Logitech Webcam" in "/home/bcadmin/Pictures".

ImageMagick
-----------

To install ImageMagick in BitCurator:
  * Open Terminal
  * Type: 
```
sudo apt-get install imagemagick
```

BeautifulSoup
-------------

To install BeautifulSoup in BitCurator:
  * Open Terminal
  * Type:
```
sudo apt-get install python-bs4
```
