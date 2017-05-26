EBISearch
=========

.. image:: https://travis-ci.org/bebatut/ebisearch.svg?branch=master
    :target: https://travis-ci.org/bebatut/ebisearch
.. image:: https://badge.fury.io/py/ebisearch.svg
    :target: https://badge.fury.io/py/ebisearch

EBISearch is a Python library for interacting with `EBI Search <http://www.ebi.ac.uk/ebisearch/overview.ebi>`_'s API.


Usage
-----

EBISearch is easy to use

.. code-block:: bash

    $ ebisearch --help
    Usage: ebisearch [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      get_domains        Get domains
      get_entries        Get entry content
      get_fields         Get retrievable fields
      get_query_results  Get results for a query

    $ get_entries --help
    Usage: ebisearch get_entries [OPTIONS]

      Return content of entries on a specific domain in EBI

    Options:
      --domain TEXT    Domain id in EBI (accessible with get_domains)
      --entry_id TEXT  (Multiple) Entry identifier to retrieve
      --field TEXT     (Multiple) Field to export (accessible with get_fields with
                       retrieva    ble as type
      --field_url      Include the field links
      --view_url       Include other view links
      --file PATH      (Optional) File to export the entry content
      --help           Show this message and exit.

It can also be used as a Python library:

.. code-block:: python

    >>> import ebisearch
    >>> ebisearch.get_entries(
            domain="metagenomics_runs",
            entryids="ERR1135279,SRR2135754",
            fields="id,experiment_type")
    [{'fields': {'experiment_type': ['metagenomic'], 'id': ['ERR1135279']}, 'source': 'metagenomics_runs', 'id': 'ERR1135279'}, {'fields': {'experiment_type': ['metagenomic'], 'id': ['SRR2135754']}, 'source': 'metagenomics_runs', 'id': 'SRR2135754'}]
    >>> ebisearch.get_number_of_results(
            domain="metagenomics_runs",
            query="experiment_type:(metagenomic)")
    13227


Installation
------------

To install EBISearch, simply:

.. code-block:: bash

    $ pip install ebisearch


Tests
-----

EBISearch comes with tests:

.. code-block:: bash

    $ make test