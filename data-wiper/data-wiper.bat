REM Usage: sdelete [-p passes] [-s] [-q] <file or directory> ...
REM sdelete [-p passes] [-z|-c] [drive letter] ...
REM -a	Remove Read-Only attribute.
REM -c	Clean free space.
REM -p passes	Specifies number of overwrite passes (default is 1).
REM -q	Don't print errors (Quiet).
REM -s or -r	Recurse subdirectories.
REM -z	Zero free space (good for virtual disk optimization).
sdelete -p 7 -s -a "path\to\file"
