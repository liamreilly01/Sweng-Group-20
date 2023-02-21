import pytest
from bot import getKeyWords

testInput = "What happened to the Legislation Directory"
testKeyWords = ['Legislation Directory', 'Directory', 'Legislation', 'happened']
def test_keywords():
    keywordlist = getKeyWords(testInput)
    newList = []
    for element in keywordlist:
        newList.append(element[0])
    assert newList == testKeyWords