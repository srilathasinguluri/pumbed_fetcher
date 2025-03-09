import requests
import pandas as pd
import xml.etree.ElementTree as ET

# PubMed API URLs
PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def search_pubmed(query, max_results=10):
    """Search PubMed for papers and return a list of PubMed IDs."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(PUBMED_SEARCH_URL, params=params)
    data = response.json()
    return data["esearchresult"].get("idlist", [])

def fetch_pubmed_details(pubmed_ids):
    """Fetch details of PubMed papers using IDs."""
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(PUBMED_FETCH_URL, params=params)
    root = ET.fromstring(response.text)

    papers = []
    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text
        authors = []
        affiliations = []
        for author in article.findall(".//Author"):
            last_name = author.find("LastName")
            first_name = author.find("ForeName")
            full_name = f"{first_name.text} {last_name.text}" if first_name is not None and last_name is not None else "Unknown"
            authors.append(full_name)
            affiliation = author.find(".//Affiliation")
            if affiliation is not None:
                affiliations.append(affiliation.text)

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Authors": ", ".join(authors),
            "Affiliations": ", ".join(affiliations)
        })

    return papers

if __name__ == "__main__":
    query = input("Enter search term: ")
    pubmed_ids = search_pubmed(query, max_results=5)
    if not pubmed_ids:
        print("No papers found.")
    else:
        papers = fetch_pubmed_details(pubmed_ids)
        df = pd.DataFrame(papers)
        df.to_csv("pubmed_results.csv", index=False)
        print("Results saved to pubmed_results.csv")
