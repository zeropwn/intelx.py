from intelx import intelx

intelx = intelx()
search = intelx.search('riseup.net')

# save the first search result file as "file.contents"
intelx.FILE_READ(search['records'][0]['storageid'], name="file.contents")