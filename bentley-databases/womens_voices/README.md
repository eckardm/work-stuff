Women's Voices
==============

The Bentley publication entitled *Women's Voices: Early Years at the University of Michigan* was created to showcase the results of a 1924 survey conducted by the Alumni Council of the Alumni Association of the University of Michigan. The survey was sent to approximately 10,250 women who had attended the University from the year 1870, when women were first admitted, to 1924. The survey responses are now part of the University Archives at the Bentley Historical Library.

You can view the publication online as [HTML](http://quod.lib.umich.edu/w/womv/images/WomensVoices.pdf), as a [PDF](http://quod.lib.umich.edu/w/womv/), or browse or search the [Alumnae Survey Database](http://bentley.umich.edu/legacy-support/um/voices/).

This dataset is organized by survey response in both JSON and CSV formats.

Survey Responses
----------------

Below are the metadata fields you'll find in the JSON and CSV that describe a survey response. In the CSV file, lists are represented by a single pipe-delimited string, such as "Events -- Commencement|Faculty -- De Pont, Paul R.".

Name | Question | JSON | CSV | Value
--- | --- | --- | --- | ---
ID  | ID assigned by the database. | key | alumID | integer
First name | Name in full | first_name | first_name | string
Middle name | Name in full | middle_name | middle_name | string
Last name | Maiden name | last_name | last_name | string
Married name | Name in full | married_name | married_name | string
Address (home) | Address (Home) | address_home (with keys for country, state, city) | address_home | dictionary in JSON (country, state and city are strings), string in CSV
Address (business) | Address (Business) | address_business (with keys for country, state and city) | address_business | dictionary in JSON (country, state and city are strings), string in CSV
Place of Birth | Place of birth | place_of_birth (with keys for country, state and city) | place_of_birth | dictionary in JSON (country, state and city are strings), string in CSV
Race | Race | race | race | string
Occupation | Present occupation | occupation | occupation | string
Other occupations | ... | other_occupation | other_occupation | string
Achievements | ... | achievement | achievement | string
Family attending UM | ... | family_attending_um | family_attending_um | string
Public offices | ... | public_office | public_office | string
Degrees | ... | degrees | degrees | dictionary in JSON (start_year and end_year are integers; school, field and degree are strings; type is an enumeration with values of undergraduate and graduate), string in CSV
Departments | ... | departments | departments | list of enumerations with values of ... in JSON and CSV
Influential women | ... | influential_women | influential_women | list of enumerations with values of ... in JSON and CSV
Memories (as LCSHs--because who doesn't remember things as LCSHs?) | ... | memories | memories | list of enumerations with values of ... in JSON and CSV

Example JSON:

```json
{
	"690": {
		"first_name": "Leita Margarita",
		"last_name": "Davis",
		"middle_name": "",
		"addresses": [{
			"type": "birth",
			"address": {
				"country": "United States",
				"state": "KS",
				"city": "Elk City"
			}
		},
		{
			"type": "home",
			"address": {
				"country": "United States",
				"state": "KS",
				"city": "Liberty"
			}
		},
		{
			"type": "business",
			"address": {
				"country": "United States",
				"state": "OK",
				"city": "Edmond"
			}
		}],
		"influential_women": ["Palmer, Alice Freeman, 1855-1902",
		"Pomeroy, Katharine P."],
		"married_name": "",
		"departments": ["College of Literature, Science, and the Arts"],
		"other_occupation": "",
		"family_attending_um": "Father: Davis, Dr. J.T.",
		"public_office": "",
		"degrees": [{
			"start_year": "",
			"degree": "",
			"end_year": "",
			"school": "Columbia University",
			"field": "",
			"type": "graduate"
		},
		{
			"start_year": "1907",
			"degree": "AB",
			"end_year": "1911",
			"school": "University of Michigan",
			"field": "Hist.",
			"type": "undergraduate"
		},
		{
			"start_year": "",
			"degree": "MA",
			"end_year": "",
			"school": "University of Pennsylvania",
			"field": "",
			"type": "graduate"
		}],
		"race": "White",
		"memories": ["Faculty -- Dow, Earle W.",
		"Faculty -- Van Tyne, Claude H.",
		"Faculty -- Wenley, Robert Mark",
		"Flora and fauna -- Huron River",
		"Learning -- courses -- History"],
		"achievement": "Teacher; Assoc.Prof. State Teacher's College, History; Social Work",
		"occupation": "Asst.Prof.Hist.College"
	}
}
```
