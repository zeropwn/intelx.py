# IntelX

![](https://i.imgur.com/V2kUSg0.png)

IntelX is a Python command-line utility and API wrapper for intelx.io, made to perform any kind of open-source intelligence.

## Installation
```bash
git clone https://github.com/zeropwn/intelx
pip3 install ./intelx
```

## Setup

To specify the API key to use, you can choose one of two options:
* Setting the ```INTELX_KEY``` environment variable.
* Manually supplying the ```-apikey``` argument.

##### Environment Variable
```bash
# create an INTELX_KEY env var with your API key.
export INTELX_KEY=abcd-efgh-ijkl-mnop
```


##### Via the client

```bash
./intelxcli.py -search riseup.net -apikey abcd-efgh-ijkl-mnop
```

## Configuration

On windows, we need to manually configure the command prompt/terminal in order to enable color support. You can do that with the following instructions:

1. Create following file ```Enable Color.reg```
```
Windows Registry Editor Version 5.00
[HKEY_CURRENT_USER\Console]
"VirtualTerminalLevel"=dword:00000001
```

2. Right Click ```Enable Color.reg``` -> Merge

## Usage

```bash
./intelxcli.py -search riseup.net
```


#### Quick search
```bash
./intelxcli.py -search riseup.net
```

#### Quick search in buckets
```bash
./intelxcli.py -search riseup.net -buckets "pastes, darknet.tor"
```

#### Quick search with previews
```bash
./intelxcli.py -search riseup.net --previews
```

#### Search with 100 results
```bash
./intelxcli.py -search riseup.net -results 100
```

#### Preview Item
```bash
./intelxcli.py -sid 28284d79b4239c14f07069c893dcbe7b5a978fb598afe7f7b12421d96124d83d533ab6e9f525c32a5b78666db612dce9df1f051b170cf25036bb0b59ed3e3f83 --preview
```

#### View Item
```bash
./intelxcli.py -sid 28284d79b4239c14f07069c893dcbe7b5a978fb598afe7f7b12421d96124d83d533ab6e9f525c32a5b78666db612dce9df1f051b170cf25036bb0b59ed3e3f83 --view
```

#### View Item in different format
To view the hexdump of a file, we can supply the ```--hex``` argument.
```bash
./intelxcli.py -sid 681a7d30167783f8195a35bb9a3f274cfcc960f661e69c24e46e91f333baf361ab0acee6dd2375ad30884f1534f66467a12f40771180d4ac11bd669c65fc5d13 --view --hex
```

If we want to convert a PDF document to text, we can supply the ```--pdf``` argument.
```bash
./intelxcli.py -sid 681a7d30167783f8195a35bb9a3f274cfcc960f661e69c24e46e91f333baf361ab0acee6dd2375ad30884f1534f66467a12f40771180d4ac11bd669c65fc5d13 --view --pdf
```

#### Download Item

The ```--download``` argument will set the HTTP request type to a stream, ultimately returning the raw bytes.
This allows us to download documents such as PDFs, ZIP, Word documents, Excel, etc.
You may set the filename with the ```-name``` argument.
```bash
# save item as test.pdf
./intelxcli.py -sid 681a7d30167783f8195a35bb9a3f274cfcc960f661e69c24e46e91f333baf361ab0acee6dd2375ad30884f1534f66467a12f40771180d4ac11bd669c65fc5d13 -name test.pdf --download
```


#### Search Phonebook
```bash
./intelxcli.py -search cia.gov --phonebook
```

#### Extract email from phonebook search
```bash
./intelxcli.py -search cia.gov --phonebook --emails
```


## Notes

Typically, the ```IntelX.search()``` function will only aggregate ~1000 results. However we can continue to navigate through more if we specify the -datefrom and -dateto argument, and continue from the "oldest" result. This functionality will be simpler to use in the future (i.e, not having to supply exact time "00:00:00/23:59:59). Will also be adding feature to remove the need for the "dateto" argument if necessary, and have it set itself automatically to the current date.

We can also specify how we want to sort the aggregated data by setting the -sort argument.

```bash
./intelxcli.py -search riseup.net -datefrom "2019-12-28 00:00:00" -dateto "2019-12-31 23:59:59"
```

# Todo
* Bundle package for easier installation with pip.
* Consider multithreading for faster previews.
* Add more accurate stats report.
* Add export/download support.
* Add thorough client documentation with example.
* Add thorough documentation for usage as a library.
* Add examples directory with examples of how to use as a library.
