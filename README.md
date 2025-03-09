>>>>Code Organization
Your project is structured as follows:

pubmed_fetcher.py → The main script that fetches research papers from PubMed, extracts required details, and saves them as a CSV file.
requirements.txt → Contains the list of required dependencies for the project.
README.md → Documentation file explaining the project details.
output.csv → The generated output file where fetched paper details will be stored.
Installation and Execution Instructions
>>>>>1. Install Python
Check if Python is installed by running:


python --version
If Python is not installed, download and install it from the official Python website:
https://www.python.org/downloads/

>>>>2. Clone the Repository
Use Git to clone the project repository:


git clone https://github.com/your-username/pubmed-fetcher.git
cd pubmed-fetcher
>>>>3. Install Dependencies
Run the following command to install the required libraries:


pip install -r requirements.txt
>>>>4. Run the Program
Execute the script by running:

\
python pubmed_fetcher.py
You will be prompted to enter a search query, such as:


Enter search term (e.g., 'cancer research'):
After entering a topic (e.g., "cancer treatment"), the program will fetch the relevant papers and save the results in output.csv.

>>>>5.Tools and Libraries Used
requests → Fetches data from the PubMed API.
pandas → Processes and saves data in a CSV file.
argparse → Handles command-line arguments.
Git → Version control system to track changes and manage the project on GitHub.
VS Code → Recommended editor for writing and running the code.
The PubMed API documentation is available at:
https://www.ncbi.nlm.nih.gov/books/NBK25500/

>>>>6Features and Future Improvements
✅ Fetch research papers from PubMed.
✅ Identify authors affiliated with pharmaceutical/biotech companies.
✅ Save the extracted data in a CSV file.

>>>>7Future Enhancements:

Improve the extraction of author affiliations using advanced methods.
Enhance accuracy in identifying company names.
Convert the project into a command-line tool for better usability.
License
This project is open-source and available under the MIT License.
