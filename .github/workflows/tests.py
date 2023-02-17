import pytest

text = "Legislative amendments were previously held in a section of the eISB known as the Legislation Directory. The information from the Legislation Directory has now been integrated into relevant parts of the site. For example, to find the list of amendments made to a particular Act, go to that Act and then click on the “Amendments, Commencements, SIs made under this Act” button. Users should note that information is displayed differently in relation to Acts enacted before and after 1931. Each Act enacted before 1 January 1931 appears in a table for the year in which the relevant Act was enacted and Acts appear in order of enactment in that table. Entries include details in relation to how each Act has been amended or otherwise affected. Details in relation to commencement information for Acts enacted prior to 1931 can be found on the Acts home page under Acts-More information, Commencement Orders. There is currently no list available of secondary legislation made under individual Acts enacted before 1 January 1931. Each Act enacted since 1 January 1931 has its own table containing three sub-tables: commencement information, amendments and other effects, and other associated secondary legislation (SIs made under the Act) and effects. Work is continuing to extend this newer format to Acts enacted before 1931."

keywords = ['Legislation Directory', 'Directory', 'Legislation', 'happened']

found_keywords = []

for keyword in keywords:
    if keyword in text:
        found_keywords.append(keyword)

if len(found_keywords) > 0:
    print("The following keywords and phrases were found in the text:")
    for keyword in found_keywords:
        print(keyword)
else:
    print("None of the keywords and phrases were found in the text.")
