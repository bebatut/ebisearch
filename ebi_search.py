#!/usr/bin/env python3

import requests


baseUrl = 'http://www.ebi.ac.uk/ebisearch/ws/rest'


# %prog getFacetedResults <domain> <query> <fields> [OPTIONS: --size | --start | --fieldurl | --viewurl | --sortfield | --order | --sort | --facetcount | --facetfields | --facets | --facetsdepth ]

# %prog getEntries        <domain> <entryids> <fields> [OPTIONS: --fieldurl | --viewurl]
# 
# %prog getDomainsReferencedInDomain <domain>
# %prog getDomainsReferencedInEntry  <domain> <entryid>
# %prog getReferencedEntries         <domain> <entryids> <referencedDomain> <fields> [OPTIONS: --size | --start | --fieldurl | --viewurl | --facetcount | --facetfields | --facets]
# 
# %prog getTopTerms       <domain> <field> [OPTIONS: --size | --excludes | --excludesets]
# 
# %prog getAutoComplete   <domain> <term>

# %prog getMoreLikeThis   <domain> <entryid> <fields> [OPTIONS: --size | --start | --fieldurl | --viewurl | --mltfields | --mintermfreq | --mindocfreq | --maxqueryterm | --excludes | --excludesets]
# %prog getExtendedMoreLikeThis


def get_domain_details(domain):
    """Return a dictionary with the details of a given domain in EBI

    >>> get_domain_details("allebi")

    domain: domain id in EBI
    """
    url = baseUrl + '/' + domain
    r = requests.get(
        url,
        headers={"accept":"application/json"})
    r.raise_for_status()
    return r.json()


def get_details_and_subdomains(domain, level, verbose = False):
    """Return the details (id and name) for the domain and its subdomains

    domain: domain id in EBI
    verbose: Boolean to define the printing info
    """
    domain_details = {domain['id']: domain['name']}
    if verbose:
        print("\t"*level + "%s -- %s" %(domain['id'], domain['name']))

    if "subdomains" not in domain:
        return domain_details
    else:
        for subdomain in domain["subdomains"]:
            domain_details.update(
                get_details_and_subdomains(subdomain, level + 1, verbose))
    return domain_details


def get_domains(verbose = False):
    """Return the list of domains in EBI as a dictionary with the key being the
    domain id and the value the domain name

    verbose: boolean to define the printing info
    """
    allebi = get_domain_details("allebi")
    domain_details = {}
    for domain in allebi["domains"]:
        domain_details.update(get_details_and_subdomains(domain, 0, verbose))
    return domain_details


def print_domain_hierarchy():
    """Print the hierarchy of the domains
    """
    get_domains(verbose = True)


def get_number_of_results(domain, query):
    """Return the number of results for a query on a specific domain in EBI

    domain: domain id in EBI 
    query: query for EBI
    """
    url = baseUrl + '/' + domain + '?query=' + query +'&size=0'
    r = requests.get(
        url,
        headers={"accept":"application/json"})
    r.raise_for_status()
    return r.json()['hitCount']


def get_subdomain_fields(domain):
    """Return the fields of a domain and its subdomains

    domain: domain id in EBI 
    """
    fields = {
        "searchable": {},
        "retrievable": {},
        "sortable": {},
        "facet": {},
        "topterms": {}
    }
    if "subdomains" not in domain:
        for field in domain["fieldInfos"]:
            field_desc = field["description"]
            field_id = field["id"]
            for option in field["options"]:
                if option["name"] in fields and option["value"] == "true":
                    fields[option["name"]].setdefault(field_id, field_desc)
    else:
        for subdomain in domain["subdomains"]:
            subdomain_fields = get_subdomain_fields(subdomain)
            fields["searchable"].update(subdomain_fields["searchable"])
            fields["retrievable"].update(subdomain_fields["retrievable"])
            fields["sortable"].update(subdomain_fields["sortable"])
            fields["facet"].update(subdomain_fields["facet"])
            fields["topterms"].update(subdomain_fields["topterms"])
    return fields


def get_fields(domain, verbose = True):
    """Return the fields (for different type) of a specific domain in EBI

    domain: domain id in EBI
    verbose: boolean to define the printing info
    """
    domain_details = get_domain_details(domain)
    fields = {
        "searchable": {},
        "retrievable": {},
        "sortable": {},
        "facet": {},
        "topterms": {}
    }
    for domain in domain_details["domains"]:
        subdomain_fields = get_subdomain_fields(domain)
        fields["searchable"].update(subdomain_fields["searchable"])
        fields["retrievable"].update(subdomain_fields["retrievable"])
        fields["sortable"].update(subdomain_fields["sortable"])
        fields["facet"].update(subdomain_fields["facet"])
        fields["topterms"].update(subdomain_fields["topterms"])

    if verbose:
        for field_type in fields:
            print("%s" %(field_type))
            for field in fields[field_type]:
                print("\t%s" %(field))
    return fields


def get_results(domain, query, fields, size='', start='', fieldurl='', viewurl='', sortfield='', order='', sort=''):
    """Return the results for a query on a specific domain in EBI

    domain: domain id in EBI 
    query: query for EBI
    fields: 
    """

    url = baseUrl + '/' + domain + '?query=' + query +'&fields=' + fields + '&size=' + size + '&start=' + start + '&fieldurl=' + fieldurl + '&viewurl=' + viewurl + '&sortfield=' + sortfield + '&order=' + order + '&sort=' + sort
    #prog getResults        <domain> <query> <fields> [OPTIONS: --size | --start | --fieldurl | --viewurl | --sortfield | --order | --sort ] 

if __name__ == '__main__':
    #print(get_domain_details("allebi"))
    #print(get_number_of_results(
    #    "metagenomics_runs", 
    #    "experiment_type:(metagenomic)"))
    #print(get_domains(verbose = True))
    #print_domain_hierarchy()
    get_fields("metagenomics_runs")

