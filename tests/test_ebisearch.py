#!/usr/bin/env python3

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    import ebisearch
except:
    raise


def cmp(la, lb):
    """Compare two lists"""
    return (la > lb) - (la < lb)


def get_domain_details():
    """Test get_domain_details function"""
    domain_details = ebisearch.get_domain_details("metagenomics_runs")
    obs_keys = list(domain_details["domains"][0].keys())
    exp_keys = ['description', 'id', 'fieldInfos', 'name', 'indexInfos']
    assert cmp(obs_keys, exp_keys)


def get_number_of_results():
    """Test get_number_of_results function"""
    nb_results = ebisearch.get_number_of_results(
        "metagenomics_runs",
        "experiment_type:(metagenomic)")
    assert nb_results >= 13227


def get_domains():
    """Test get_domains function"""
    domains = ebisearch.get_domains(verbose=False)
    assert "uniref" in domains and 'sra-analysis' in domains


def print_domain_hierarchy():
    """Test print_domain_hierarchy function"""
    ebisearch.print_domain_hierarchy()


def get_fields():
    """Test get_fields function"""
    fields = ebisearch.get_fields("metagenomics_runs", verbose=False)
    field_type = ["searchable", "retrievable", "sortable", "facet", "topterms"]
    assert cmp(fields, field_type) and "temperature" in fields["retrievable"]


def get_domain_search_results():
    """Test get_domain_search_results function"""
    res = ebisearch.get_domain_search_results(
        domain="metagenomics_runs",
        query="experiment_type:(metagenomic) AND pipeline_version:(3.0)",
        fields="id,experiment_type",
        size=20)
    fields = res[0].keys()
    res_fields = res[0]["fields"].keys()

    exp_fields = ['source', 'id', 'fields', 'experiment_type']
    exp_res_fields = ['id', 'experiment_type']
    assert cmp(fields, exp_fields) and cmp(res_fields, exp_res_fields)


def get_all_domain_search_results():
    """Test get_all_domain_search_results function"""
    res = ebisearch.get_all_domain_search_results(
        domain="metagenomics_runs",
        query="experiment_type:(metagenomic) AND pipeline_version:(3.0)",
        fields="id,experiment_type")
    assert len(res) >= 2092


def get_entries():
    """Test get_entries function"""
    ent = ebisearch.get_entries(
        domain="metagenomics_runs",
        entryids="ERR1135279,SRR2135754",
        fields="id,experiment_type")
    fields = ent[0].keys()
    res_fields = ent[0]["fields"].keys()
    exp_fields = ['source', 'id', 'fields', 'experiment_type']
    exp_res_fields = ['id', 'experiment_type']
    assert len(ent) > 2
    assert cmp(fields, exp_fields)
    assert cmp(res_fields, exp_res_fields)


if __name__ == "__main__":
    get_domain_details()
    get_number_of_results()
    get_domains()
    print_domain_hierarchy()
    get_fields()
    get_domain_search_results()
    get_all_domain_search_results()
    get_entries()
