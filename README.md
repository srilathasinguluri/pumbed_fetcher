To fetch PubMed data and extract the required fields into a CSV file, you can use Python with the Entrez module from Biopython.

📌 Steps to Implement
Fetch PubMed articles using a query (e.g., "cancer treatment").
Extract relevant details:
PubmedID (PMID)
Title
Publication Date
Non-academic Author(s) (Filtered based on affiliation)
Company Affiliation(s) (Biotech/Pharma companies)
Corresponding Author Email
Save to a CSV file.
