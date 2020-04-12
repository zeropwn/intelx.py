from intelx import intelx

intelx = intelx()
search = intelx.search('riseup.net')

# grab file contents of first search result
contents = intelx.FILE_VIEW(search['records'][0]['storageid'])

print(contents)