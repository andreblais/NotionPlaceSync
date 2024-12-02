## Version History

- **1.0.0** – Initial release of the Notion-Google Places Integration.

# Notion-Google Places Integration

This Python script integrates the Google Places API and the Notion API to  
streamline adding business data (e.g., ratings, contact information) to a  
Notion database. It's designed to help users search for businesses (like  
trailer rentals) within a specified location and automatically populate the  
relevant details into a Notion database.

---

## Features

- **Google Places Search**: Search for businesses based on a query, location,  
  and radius.  
- **Detailed Business Information**: Fetch details such as name, address,  
  ratings, phone number, and website for each business.  
- **Notion Integration**: Automatically add the collected information to a  
  Notion database for better organization and tracking.  
- **Region Restriction**: Limit searches to a specific region (default: Canada).  

---

## Prerequisites

- **Python**: Version 3.10 or higher is recommended.  
- **APIs**:  
  - Google Places API  
  - Notion API  
- **Dependencies**: See the [Installation](#installation) section for required  
  Python packages.  

---

## Installation

1. Clone the repository:  

   git clone <repository_url>
   cd <repository_folder>

2. Install dependencies:

    Copy code
    pip install -r requirements.txt

3. Create a .env file in the project directory and populate it with your API
keys:

    GOOGLE_API_KEY=<Your_Google_API_Key>
    NOTION_API_KEY=<Your_Notion_API_Key>
    DATABASE_ID=<Your_Notion_Database_ID>

4. Set up a .gitignore file (if not already done) to ensure the .env file
is excluded from version control:

    .env

---

## Usage

1. Customize the main function in notion_google_places_sync.py to adjust the
search parameters:

    query = "trailer rentals"  # Search query
    location = "45.500260452766184, -73.56513584465054"  # Coordinates 
      (e.g., Montreal, QC)
    radius = 5000  # Radius in meters

2. Run the script:

    python notion_google_places_sync.py

3. The script will:

- Search for places matching the query and location.
- Fetch details for each place.
- Add the business data to your specified Notion database.

---

## Example Output in Notion

Each business will be added to the database with the following fields:

- Company: Name of the business.
- Google Rating: Average rating on Google.
- Review Count: Total number of Google reviews.
- Location: Full address of the business.
- Phone Number: Contact number.
- Website: Link to the business's website.

---

## Troubleshooting

- ModuleNotFoundError: No module named 'notion_client': Ensure all
dependencies are installed using pip install -r requirements.txt.

- APIResponseError: Phone Number is expected to be phone_number: Check
the add_to_notion function to ensure the property types match your Notion
database schema.

- Invalid API Keys: Verify your API keys and ensure they are entered
correctly in the .env file.

---

## Acknowledgements

- Google Maps Platform
- Notion API Documentation
- dotenv Python Package
- OpenAI