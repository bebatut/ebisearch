#!/usr/bin/env python3

from .context import ebisearch

print(ebisearch.get_domain_details("metagenomics_runs"))


print(ebisearch.get_number_of_results(
    "metagenomics_runs",
    "experiment_type:(metagenomic)"))
print(ebisearch.get_domains(verbose = True))
ebisearch.print_domain_hierarchy()
ebisearch.get_fields("metagenomics_runs")
# Test get_domain_search_results
ebisearch.get_domain_search_results(
    domain="metagenomics_run",
    query="experiment_type:(metagenomic) AND pipeline_version:(3.0)",
    fields="id,experiment_type")
ebisearch.get_domain_search_results(
    domain="metagenomics_runs",
    query="experiment_type:(metagenomic) AND pipeline_version:(3.0)",
    fields="id,experiment_tye")
res = ebisearch.get_domain_search_results(
    domain="metagenomics_runs",
    query="experiment_type:(metagenomic) AND pipeline_version:(3.0)",
    fields="id,experiment_type",
    size=20)
print(res)
res = ebisearch.get_domain_search_results(
    domain="metagenomics_runs",
    query="experiment_type:(metagenomic) AND pipeline_version:(3.0)",
    fields="id,experiment_type",
    size=10)
print(res)
res = ebisearch.get_domain_search_results(
    domain="metagenomics_runs",
    query="experiment_type:(metagenomic) AND pipeline_version:(3.0)",
    fields="id,experiment_type",
    size=10,
    start=10)
print(res)
# Test get_entries
entries = ebisearch.get_entries(
    domain="metagenomics_runs",
    entryids="ERR1135279",
    fields="id,experiment_type")
print(entries)

domains = ebisearch.get_domains(verbose=False)
for domain in domains:
    topterms = ebisearch.get_topterms_fields("go",verbose=False)
    if len(topterms) > 0:
        print(domain)
        print(topterms)

# Test get_morelikethis
print(ebisearch.get_number_of_morelikethis(
        domain="metagenomics_runs",
        entryid="ERR1135279"))