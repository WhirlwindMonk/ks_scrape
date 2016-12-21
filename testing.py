from re import match
texts = [
'https://www.kickstarter.com/projects/1986219362/dies-irae-english-localization-project-commences/description',
'https://www.kickstarter.com/projects/1986219362/dies-irae-english-localization-project-commences',
'http://www.kickstarter.com/projects/1986219362/dies-irae-english-localization-project-commences?ref=nav_search',
'https://www.kickstarter.com/projects/1986219362/dies-irae-english-localization-project-commences/?ref=kicktraq',
'www.google.com',
]
for text in texts:
	blah = match('(https?://www.kickstarter.com/projects/\d+/.+?)(/.+|\?.+)?$', text)
	if blah != None:
		print(blah.group(1))
	else:
		print(blah)