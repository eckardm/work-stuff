'''
Here's the draft of the FA attached as well as the original metadata spreadsheets I gave Rob. The series that need to be addressed are:

  * Sound Materials - Audio Reel-to-Reel News Briefs (1975-1994)
  * Audio Podcasts (2006 - 2010)
  * Digital Video

For the podcasts and video, we want to keep:

  * Unit title
  * Unit date
  * Note field
  * Physical facet--file extension(s)

Let me know if you have any questions--thanks!

MIke'''

# import what we need
import xlrd

# location of spreadsheets
spreadsheet_1_path = 'C:/Users/eckardm/GitHub/work-stuff/um-news-av/deepBlue_87265.11_0004'
spreadsheet_2_path = 'C:/Users/eckardm/GitHub/work-stuff/um-news-av/deepBlue_87265_0002'
spreadsheet_3_path = 'C:/Users/eckardm/GitHub/work-stuff/um-news-av/deepBlue_87265_0003'
spreadsheet_4_path = 'C:/Users/eckardm/GitHub/work-stuff/um-news-av/newsandinfopodcastdeposit2_87265_0001'
spreadsheet_5_path = 'C:/Users/eckardm/GitHub/work-stuff/um-news-av/newsandinfopodcastsdeposit_87265_0001'
spreadsheet_6_path = 'C:/Users/eckardm/GitHub/work-stuff/um-news-av/UM-News_AV_2014113'

# skip header row when necessary and identify columns for each spreadsheet
spreadsheet_1 = open_workbook(spreadsheet_1_path)
for row in spreadsheet_1.sheets():
    spreadsheet_1_header_row(0)
    spreadsheet_1_unit_title = row[]
    spreadsheet_1_unit_date = row[]
    spreadsheet_1_note_field = row[]
    spreadsheet_1_physical_facet = row[]
    
spreadsheet_2= open_workbook(spreadsheet_2_path)
for row in spreadsheet_2.sheets():
    spreadsheet_2_header_row(0)
    spreadsheet_2_unit_title = row[]
    spreadsheet_2_unit_date = row[]
    spreadsheet_2_note_field = row[]
    spreadsheet_2_physical_facet = row[]
    
spreadsheet_3 = open_workbook(spreadsheet_3_path)
for row in spreadsheet_3.sheets():
    spreadsheet_3_unit_title = row[]
    spreadsheet_3_unit_date = row[]
    spreadsheet_3_note_field = row[]
    spreadsheet_3_physical_facet = row[]
    
spreadsheet_4 = open_workbook(spreadsheet_4_path)
for row in spreadsheet_4.sheets():
    spreadsheet_4_header_row(0)
    spreadsheet_4_unit_title = row[]
    spreadsheet_4_unit_date = row[]
    spreadsheet_4_note_field = row[]
    spreadsheet_4_physical_facet = row[]

spreadsheet_5 = open_workbook(spreadsheet_5_path)
for row in spreadsheet_5.sheets():
    spreadsheet_5_header_row(0)
    spreadsheet_5_unit_title = row[]
    spreadsheet_5_unit_date = row[]
    spreadsheet_5_note_field = row[]
    spreadsheet_5_physical_facet = row[]
    
spreadsheet_6 = open_workbook(spreadsheet_6_path)
for row in spreadsheet_6.sheets():
    spreadsheet_6_header_row(0)
    spreadsheet_6_unit_title = row[]
    spreadsheet_6_unit_date = row[]
    spreadsheet_6_note_field = row[]
    spreadsheet_6_physical_facet = row[]   