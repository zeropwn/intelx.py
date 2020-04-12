IntelX: NSA-like search engine
===============================

**IntelX** is a Python command-line utility and API wrapper for intelx.io, made to perform any kind of open-source intelligence.

It's really as simple as this:

.. code-block:: python

    from intelx import intelx

    intelx = intelx('APIKEY')
    intelx.search('hackerone.com')

Features
--------

**IntelX** allows you to perform an internet-wide (darkweb included) search for these selector types: 

- Email address
- Domain, including wildcards like \*.example.com
- URL
- IP, CIDR. Both IPv4 and IPv6 are fully supported.
- Phone Number
- Bitcoin address
- MAC address
- IPFS Hash
- Credit Card Number
- Social Security Number
- IBAN (International Bank Account Number)
- and other internal ones like UUID, Storage ID, Simhash

In these categories:

- Paste sites, including historical ones
- Darknet: Tor and I2P
- Wikileaks & Cryptome
- Government sites of North Korea and Russia
- Public Data Leaks
- Whois Data
- Dumpster: Everything else
- Public Web

Installation
------------

Install **IntelX** by running:

.. code-block:: bash

   pip3 install intelx

or clone the repository

.. code-block:: bash

   git clone https://github.com/zeropwn/intelx
   pip3 install ./intelx


Usage as a library
------------------
**IntelX** is a double-edged sword. You can use it as a library for your own tooling, or you can use the command-line utility.

To use it as a library, all you have to do is import it in your project, and initialize the class. If you supply an API key, it will use that, if not, it will automatically select the public API key (limited functionality).

.. code-block:: python
   
   from intelx import intelx
   intelx = intelx()

Once you've done that, you can use any of the functions defined in the class.

Quick search
############

To execute a quick search, we can easily just use the intelx.search() function.

.. code-block:: python
   
   from intelx import intelx

   intelx = intelx('abcd-efgh-ijkl-mnop')
   search = intelx.search('hackerone.com')

Advanced search
###############
By default, the "maxresults" limit is set to 100 to avoid unnecessarily overloading the system. This value can be overridden at any time by setting the maxresults argument.

.. code-block:: python
   
   from intelx import intelx

   intelx = intelx('abcd-efgh-ijkl-mnop')
   search = intelx.search('hackerone.com', maxresults=200)

The following arguments have default values, but can be overridden to your choosing:

- maxresults=100
- buckets=[]
- timeout=5
- datefrom=""
- dateto=""
- sort=4
- media=0
- terminate=[]

Searching buckets
*****************

Lets say we want to search a term within specific buckets (leaks & darknet), we can modify our code to look something like this:

.. code-block:: python
   
   from intelx import intelx

   b = ['darknet', 'leaks']

   intelx = intelx('abcd-efgh-ijkl-mnop')
   search = intelx.search('hackerone.com', maxresults=200, buckets=b)

Filtering by date
*****************

Another thing we can do is filter results based on their date.

When setting the dateto and datefrom options, it's very important to note that you cannot use one without the other.
If you choose to use one, you must provide the other if you want it to work properly.

You must also accurately set the times as well.

.. code-block:: python
   
   from intelx import intelx

   startdate = "2014-01-01 00:00:00"
   enddate = "2014-02-02 23:59:59"

   intelx = intelx('abcd-efgh-ijkl-mnop')

   search = intelx.search(
      'riseup.net',
      maxresults=200,
      datefrom=startdate,
      dateto=enddate
   )


Filtering by data type
**********************

We can filter results based on their data type using the "media" argument.

Using the following script, we can filter paste documents dated between 2014-01-01 and 2014-02-02 that have been collected.

You can find a table below with all the media types and their respective IDs.

.. code-block:: python
   
   from intelx import intelx

   media_type = 1 # Paste document
   startdate = "2014-01-01 00:00:00"
   enddate = "2014-02-02 23:59:59"

   intelx = intelx('abcd-efgh-ijkl-mnop')

   search = intelx.search(
      'riseup.net',
      maxresults=200,
      media=media_type,
      datefrom=startdate,
      dateto=enddate
   )

Search statistics
*****************

If we want to collect some statistics, we can use the following code:


.. code-block:: python
   
   from intelx import intelx

   intelx = intelx('abcd-efgh-ijkl-mnop')

   search = intelx.search(
      'riseup.net',
      maxresults=1000,
   )

   stats = intelx.stats(search)
   print(stats)


Viewing/reading files
#####################

There is one fundamental difference between the ``FILE_VIEW`` function and ``FILE_READ`` function. Viewing is for quickly viewing contents of a file (generally assumed to be text).
``FILE_READ``, on the other hand, is for direct data download.

This means if the resource is a ZIP/Binary or any other type of file, you can reliably get the contents without any encoding issues.

Viewing
*******
.. code-block:: python
   
   from intelx import intelx

   intelx = intelx()
   search = intelx.search('riseup.net')

   # grab file contents of first search result
   contents = intelx.FILE_VIEW(search['records'][0]['storageid'])

   print(contents)

It is worth noting that the view function accepts a "format" argument, which allows us to view the file in a different format.

For example, if we have a binary file and want to get a hex dump of it, we can set the format argument to "1".

See :ref:`Format Types` for more.

.. code-block:: python
   
   from intelx import intelx

   intelx = intelx()
   search = intelx.search('riseup.net')

   # grab file contents of first search result
   contents = intelx.FILE_VIEW(search['records'][0]['storageid'], format=1)

   print(contents)

For other format types, please refer to :ref:`Media Types`

Reading
*******

If we want to download/read a file's raw bytes, we can use the ``FILE_READ`` function.
The file will be saved as "file.contents". If a name hasn't been set, it will save as the storage id.

.. code-block:: python

   from intelx import intelx

   intelx = intelx()
   search = intelx.search('riseup.net')

   # save the first search result file as "file.contents"
   intelx.FILE_READ(search['records'][0]['storageid'], name="file.contents")


Other Notes
###########

.. _Media Types:

Media Types
***********
Here is a table listing the media types, along with their respective IDs.

=====  ============================================
ID     Media Type
=====  ============================================
0      All
1      Paste document
2      Paste user
3      Forum
4      Forum board 
5      Forum thread
6      Forum post
7      Forum user
8      Screenshot of website
9      HTML copy of a website    
13     Tweet
14     URL
15     PDF document
16     Word document
17     Excel document
18     Powerpoint document
19     Picture
20     Audio file
21     Video file
22     Container file (ZIP, RAR, TAR, etc included)
23     HTML file
24     Text file    
=====  ============================================

.. _Format Types:

Format Types
************
====  =================================
ID    Format Type
====  =================================
0     textview of content
1     hex view of content
2     auto detect hex view or text view
3     picture view
4     not supported
5     html inline view (sanitized)
6     text view of pdf
7     text view of html
8     text view of word file
====  =================================

Contribute
----------

- Issue Tracker: github.com/zeropwn/intelx
- Source Code: github.com/zeropwn/intelx

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@google-groups.com

License
-------

The project is licensed under the BSD license.