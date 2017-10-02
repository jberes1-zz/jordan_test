from googleads import adwords
import fetch_adwords as f_adwords

CUSTOMER_ID = 5548820786  # TODO: SET ACCOUNT ID
API_VERSION = 'v201708'  # API VERSION

def main(client):
    ############################################
    # INITIALISE PATHS
    ############################################
    path_all_adgroups_with_keywords = "Keywords.csv"

    ############################################
    # GET SERVICES
    ############################################
    report_downloader = client.GetReportDownloader(version=API_VERSION)

    ############################################
    # SELECT ACCOUNT
    ############################################
    client.SetClientCustomerId(CUSTOMER_ID)

    ############################################
    # GRAB KEYWORDS
    ############################################
    keywords_df = f_adwords.fetch_all_adgroups_by_keyword(report_downloader, path=path_all_adgroups_with_keywords)

    print(keywords_df)
    # Do your stuff here

if __name__ == "__main__":
    credentials_path = 'set/path/to/credentials.yaml'
    adwords_client = adwords.AdWordsClient.LoadFromStorage(credentials_path)
    main(adwords_client)
