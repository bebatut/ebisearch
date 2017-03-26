#!/usr/bin/env python3

import click
import ebisearch
from pprint import pprint


@click.group()
def main():
    pass


def write_simple_dict_content(dictionary, file):
    """Write the content of a simple dictionary (keys and values) in a file"""
    with open(file, "w") as output_file:
        s = "id\tname\n"
        output_file.write(s)

        for entry in dictionary:
            s = "%s\t" % (entry)
            s += "%s\n" % (dictionary[entry])
            output_file.write(s)


def write_entries(entries, file):
    """Write the content of a dictionary with entries in a file"""
    fields = []
    field_url = []
    view_url = []
    if len(entries) > 0:
        fields = list(entries[0]["fields"].keys())
        if "fieldURLs" in entries[0]:
            nb = len(entries[0]["fieldURLs"])
            field_url.extend(["fieldURLs_%s" % (s) for s in range(nb)])
        if "viewURLs" in entries[0] and len(entries[0]["viewURLs"]) > 0:
            nb = len(entries[0]["viewURLs"])
            view_url.extend(["viewURLs_%s" % (s) for s in range(nb)])
    if "id" in fields:
        fields.remove("id")

    with open(file, "w") as output_file:
        if len(entries) > 0:
            s = "id"
        for field in fields:
            s += "\t%s" % (field)
        for field in field_url:
            s += "\t%s" % (field)
        for field in view_url:
            s += "\t%s" % (field)
        s += "\n"
        output_file.write(s)

        for entry in entries:
            s = "%s" % (entry["id"])
            for field in fields:
                s += "\t%s" % (",".join(entry["fields"][field]))
            if "fieldURLs" in entry:
                for field_url in entry["fieldURLs"]:
                    s += "\t%s" % (field_url["value"])
            if "viewURLS" in entry:
                for view_url in entry["viewURLs"]:
                    s += "\t%s" % (field_url["value"])
            s += "\n"
            output_file.write(s)


@click.command('get_domains', short_help='Get domains')
@click.option(
    '--file',
    required=False,
    type=click.Path(dir_okay=True, writable=True),
    help='File to export the domain information (optional)')
def get_domains(file):
    """Return the list of domains in EBI"""
    domains = ebisearch.get_domains(verbose=False)
    if file:
        write_simple_dict_content(domains, file)
    else:
        pprint(domains)


@click.command('get_fields', short_help='Get retrievable fields')
@click.option(
    '--domain',
    help='Domain id in EBI (accessible with get_domains)')
@click.option(
    '--field_type',
    help='Type fo field',
    type=click.Choice(
        ["searchable", "retrievable", "sortable", "facet", "topterms"]))
@click.option(
    '--file',
    required=False,
    type=click.Path(dir_okay=True, writable=True),
    help='(Optional) File to export the domain information')
def get_fields(domain, field_type, file):
    """Return the list of fields of a type for a specific domain in EBI"""
    fields = ebisearch.get_specific_fields(domain, field_type, verbose=False)
    if file:
        write_simple_dict_content(fields, file)
    else:
        pprint(fields)


@click.command('get_entries', short_help='Get entry content')
@click.option(
    '--domain',
    help='Domain id in EBI (accessible with get_domains)')
@click.option(
    '--entry_id',
    multiple=True,
    help='(Multiple) Entry identifier to retrieve')
@click.option(
    '--field',
    multiple=True,
    help='(Multiple) Field to export (accessible with get_fields with retrieva\
    ble as type')
@click.option('--field_url', is_flag=True, help='Include the field links')
@click.option('--view_url', is_flag=True, help='Include other view links')
@click.option(
    '--file',
    required=False,
    type=click.Path(dir_okay=True, writable=True),
    help='(Optional) File to export the entry content')
def get_entries(domain, entry_id, field, field_url, view_url, file):
    """Return content of entries on a specific domain in EBI"""
    entries = ebisearch.get_entries(
        domain,
        ",".join(entry_id),
        ",".join(field),
        fieldurl=field_url,
        viewurl=view_url)
    if file:
        write_entries(entries, file)
    else:
        pprint(entries)


@click.command('get_query_results', short_help='Get results for a query')
@click.option(
    '--domain',
    help='Domain id in EBI (accessible with get_domains)')
@click.option(
    '--query',
    help='Query (searchable fields accessible with get_fields with searchable \
    as type)')
@click.option(
    '--field',
    multiple=True,
    help='(Multiple) Field to export (accessible with get_fields with\
    retrievable as type)')
@click.option(
    '--order',
    required=False,
    type=click.Choice(["ascending", "descending"]),
    help='(Optional) Order to sort the results (optional), should come along \
    with "sortfield" and not allowed to use with "sort" parameters')
@click.option(
    '--sort_field',
    required=False,
    help='(Optional) Field to sort on (accessible via get_fields with sortable \
    as option), should come along with "sortfield"')
@click.option(
    '--sort',
    multiple=True,
    required=False,
    help='(Optional, Multiple) Sorting criteria with field_id:order (field_id \
    accessible with get_fields with retrievable as type), should not be used \
    in conjunction with any of "sortfield" and "order" parameters')
@click.option('--field_url', is_flag=True, help='Include the field links')
@click.option('--view_url', is_flag=True, help='Include other view links')
@click.option(
    '--facets',
    multiple=True,
    required=False,
    help='(Optional, Multiple) Facet selections to apply on search results \
    with facet_id:facet_value (facet_id accessible with get_fields with facet \
    as type)')
@click.option(
    '--facet_fields',
    multiple=True,
    required=False,
    help='(Optional, Multiple) Facet field identifiers associated with facets \
    to retrieve (facet_id accessible with get_fields with facet as type)')
@click.option(
    '--facet_count',
    type=int,
    required=False,
    help='(Optional) Number of facet values to retrieve')
@click.option(
    '--facet_depth',
    type=int,
    required=False,
    help='(Optional) Number of levels in the facet hierarchy to retrieve')
@click.option(
    '--file',
    required=False,
    type=click.Path(dir_okay=True, writable=True),
    help='(Optional) File to export the entry content')
def get_query_results(
    domain, query, field, order, sort_field, sort, field_url, view_url, facets,
    facet_fields, facet_count, facet_depth, file
):
    """Return the all the results for a query on a specific domain in EBI"""
    if not order:
        order = None
    if not sort_field:
        sort_field = None
    if not sort:
        sort = None
    else:
        sort = ",".join(sort)
    if not facets:
        facets = None
    else:
        facets = ",".join(facets)
    if not facet_fields:
        facet_fields = None
    else:
        facet_fields = ",".join(facet_fields)
    if not facet_count:
        facet_count = None
    if not facet_depth:
        facet_depth = None

    results = ebisearch.get_all_domain_search_results(
        domain=domain,
        query=query,
        fields=",".join(field),
        order=order,
        sortfield=sort_field,
        sort=sort,
        fieldurl=field_url,
        viewurl=view_url,
        facets=facets,
        facetfields=facet_fields,
        facetcount=facet_count,
        facetsdepth=facet_depth)

    if file:
        write_entries(results, file)
    else:
        pprint(results)


main.add_command(get_domains)
main.add_command(get_fields)
main.add_command(get_entries)
main.add_command(get_query_results)


if __name__ == "__main__":
    main()
