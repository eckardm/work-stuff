'''
materials produced in sustainable formats will be maintained in their original version'''
tier_1_list = [
    # office documents and text-based files
    # docx
    ".docx", 
    ".docm", 
    # xlsx
    ".xlsx", 
    ".xlsm", 
    # pptx
    ".pptx", 
    ".pptm", 
    # odt
    ".odt", 
    ".fodt", 
    # ods
    ".ods", 
    ".fods", 
    # odp
    ".odp", 
    ".fodp", 
    # pdf/a
    ".pdf", # <-- will this work?
    # txt
    ".txt", 
    # rtf
    ".rtf", 
    # xml
    ".xml", 
    # csv
    ".cxv", 
    # tsv
    ".tsv", 
    ".tab", 
    # audio files
    # wav
    ".wav", 
    ".wave", 
    # aiff
    ".aiff", 
    ".aif", 
    ".aifc", 
    # mp3
    ".mp3", 
    # flac
    ".flac", 
    # ogg
    ".ogg", 
    ".ogv", 
    ".oga", 
    ".ogx", 
    ".ogm", 
    ".spx", 
    ".opus", 
    # video files
    # mpeg-1/2
    ".mpg", 
    ".mpeg", 
    ".mp1", 
    ".mp2", 
    ".mp3", 
    ".m1v", 
    ".m1a", 
    ".m2a", 
    ".mpa", 
    ".mpv", 
    ".mpg", 
    ".mpeg", 
    ".m2v", 
    ".mp3", 
    # avi
    ".avi", 
    # mov
    ".mov", 
    ".qt", 
    # mp4
    ".mp4", 
    ".m4a", 
    ".m4p", 
    ".m4b", 
    ".m4r", 
    ".m4v", 
    # mj2
    ".mj2", 
    ".mjp2", 
    # dv
    ".dv", 
    ".dif", 
    # raster (or bitmap) image files
    # tiff
    ".tiff", 
    ".tif", 
    # jpeg/jfif
    ".jpg", 
    ".jpeg", 
    ".jpe", 
    ".jif", 
    ".jfif", 
    ".jfi", 
    # jpeg 2000
    ".jp2", 
    ".j2k", 
    ".jpf", 
    ".jpx",
    ".jpm",
    ".mj2", 
    # gif
    ".gif", 
    # png
    ".png", 
    # vector image files
    # svg
    ".svg", 
    ".svgz", 
    # email files
    # mbox
    ".mbox", 
    # database files
    # csv
    ".csv", 
    # siard
    ".siard", 
    # mysql sql
    ".sql"
]

'''
common "at-risk" formats will be converted to preservation-quality file types to retain important features and functionalities'''
tier_2_list = [
    # audio files
    # wma
    ".asf", 
    ".wma", 
    ".wmv", 
    # ra
    ".ra", 
    ".ram", 
    # snd
    ".snd", 
    # au
    ".au", 
    ".snd", 
    # office documents and text-based files
    # doc
    ".doc", 
    # ppt
    ".ppt", 
    # xls
    ".xls", 
    # email files
    # eml
    ".eml", 
    # pst
    ".pst", 
    # eudora
    ".csom", 
    ".euhl", 
    ".mbx", 
    ".pce", 
    ".rce", 
    ".sta", 
    ".toc", 
    # raster image files
    # bmp
    ".bmp", 
    ".dib", 
    # psd
    ".psd", 
    # fpx
    ".fpx", 
    # pcd
    ".pcd", 
    # pct
    ".pict", 
    ".pct", 
    ".pic", 
    # tga
    ".tga", 
    # vector image files
    # ai
    ".ai", 
    # wmf
    ".wfm", 
    ".emf", 
    ".wmz", 
    ".emz", 
    # ps
    ".ps", 
    # eps
    ".eps", 
    ".epsf", 
    ".epsi", 
    # video files
    # swf
    ".swf", 
    # flv
    ".flv", 
    ".f4v", 
    ".f4p", 
    ".f4a", 
    ".f4b", 
    # wmv
    ".asf", 
    ".wma", 
    ".wmv", 
    # rv
    ".rv"
]

'''
all other content will receive basic bit-level preservation'''
tier_3_list = []
