import csv
import re
from Bio import Entrez, Medline

# Set your email (Required by NCBI)
Entrez.email = "your_email@example.com"

# Function to fetch PubMed articles
def fetch_pubmed_articles(query, max_results=20):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()

    if not record["IdList"]:  # Handle no results
        print("❌ No records found for the given query.")
        return []

    return record["IdList"]

# Function to get detailed article info
def get_article_details(pubmed_ids):
    if not pubmed_ids:
        return []
    
    handle = Entrez.efetch(db="pubmed", id=",".join(pubmed_ids), rettype="medline", retmode="text")
    records = list(Medline.parse(handle))
    handle.close()
    return records

# Function to extract required fields
def extract_data(records):
    data = []
    
    for record in records:
        pubmed_id = record.get("PMID", "N/A")
        title = record.get("TI", "N/A")
        pub_date = record.get("DP", "N/A")
        authors = record.get("FAU", [])  # Full Author Names
        affiliations = record.get("AD", ["N/A"])  # Use list to prevent indexing issues

        # Extract non-academic authors & company affiliations
        non_academic_authors = []
        company_affiliations = []
        
        for i, author in enumerate(authors):
            aff = affiliations[i] if i < len(affiliations) else "N/A"
            if aff and not re.search(r"university|college|institute|school", aff, re.IGNORECASE):
                non_academic_authors.append(author)
            if aff and re.search(r"pharma|biotech|company|corporation|inc|ltd|llc", aff, re.IGNORECASE):
                company_affiliations.append(aff)

        # Extract corresponding author email (if available)
        email = "N/A"
        email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", " ".join(affiliations))
        if email_match:
            email = email_match.group(0)

        data.append([
            pubmed_id,
            title,
            pub_date,
            "; ".join(non_academic_authors) if non_academic_authors else "N/A",
            "; ".join(company_affiliations) if company_affiliations else "N/A",
            email
        ])

    return data

# Function to save results as CSV
def save_to_csv(data, filename="pubmed_results.csv"):
    headers = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

# Main execution
if __name__ == "__main__":
    query = "cancer treatment"
    pubmed_ids = fetch_pubmed_articles(query)
    
    if not pubmed_ids:  # Stop execution if no records found
        print("❌ No PubMed records found. Exiting script.")
    else:
        records = get_article_details(pubmed_ids)
        extracted_data = extract_data(records)
        save_to_csv(extracted_data)
        print(f"✅ Results saved to pubmed_results.csv ({len(extracted_data)} records)")
