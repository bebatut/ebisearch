#!/usr/bin/env python3

import sys
import click
import ebisearch
from pprint import pprint

@click.group()
def main():
    pass


@click.command('get_entries', short_help='Get entry content')
@click.option('--domain', help='Domain id in EBI (accessible with get_domains)')
@click.option(
    '--entryid',
    multiple=True,
    help='Entry identifier to retrieve (multiple possible)')
@click.option('--field',
    multiple=True,
    help='Field to export (accessible with get_retrievable_fields, multiple possible)')
@click.option('--fieldurl', is_flag=True, help='Include the field links')
@click.option('--viewurl', is_flag=True, help='Include other view links')
@click.option('--file',
    required=False,
    type=click.Path(dir_okay=True, writable=True),
    help='File to export the entry content (optional)')
def get_entries(domain, entryid, field, fieldurl, viewurl, file):
    """Return content of entries on a specific domain in EBI"""
    click.echo("get_entries for %s" % (domain))
    entries = ebisearch.get_entries(
        domain,
        ",".join(entryid),
        ",".join(field),
        fieldurl=fieldurl,
        viewurl=viewurl)
    if file:
        fields = []
        field_url = []
        view_url = []
        if len(entries)>0:
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
            if len(entries)>0:
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
    else:
        pprint(entries)

main.add_command(get_entries)


if __name__ == "__main__":
    main()
    entries = ebisearch.get_entries(
    domain="metagenomics_runs",
    entryids="ERR1135279",
    fields="id,experiment_type")
    print(entries)