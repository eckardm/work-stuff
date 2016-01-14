REM Usage: sdelete [-p passes] [-s] [-q] <file or directory> ...
REM sdelete [-p passes] [-z|-c] [drive letter] ...
REM -a	Remove Read-Only attribute.
REM -c	Clean free space.
REM -p passes	Specifies number of overwrite passes (default is 1).
REM -q	Don't print errors (Quiet).
REM -s or -r	Recurse subdirectories.
REM -z	Zero free space (good for virtual disk optimization).
"C:\Users\eckardm\work-stuff\data-wiper\SDelete\sdelete.exe" -p 7 -s -a "R:\Dark Archive\Collections\9979\0014"
"C:\Users\eckardm\work-stuff\data-wiper\SDelete\sdelete.exe" -p 7 -s -a "R:\Content Backup\dark-archive-backup\9979\0014"
"C:\Users\eckardm\work-stuff\data-wiper\SDelete\sdelete.exe" -p 7 -s -a "V:\9979\0014"
"C:\Users\eckardm\work-stuff\data-wiper\SDelete\sdelete.exe" -p 7 -s -a "Y:\dark-archive-backup\9979\0014"
