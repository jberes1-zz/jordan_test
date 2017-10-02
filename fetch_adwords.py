import pandas as pd
def fetch_all_adgroups_by_keyword(report_downloader, path):
    header = ['Criteria', 'Impressions', 'AccountDescriptiveName']
    with open(path, 'w') as report_csv:
        report = {
            "reportName": "name",
            "dateRangeType": "LAST_30_DAYS",
            "reportType": "KEYWORDS_PERFORMANCE_REPORT",
            "downloadFormat": "CSV",
            "selector": {
                "fields": header,
                "predicates": [{
                    "field": "Status",
                    "operator": "NOT_EQUALS",
                    "values": "REMOVED"
                }, {
                    "field": "AdGroupStatus",
                    "operator": "NOT_EQUALS",
                    "values": "REMOVED"
                }, {
                    "field": "CampaignStatus",
                    "operator": "NOT_EQUALS",
                    "values": "REMOVED"
                }]
            }
        }

        report_csv.write(",".join(header) + "\n")
        report_downloader.DownloadReport(
                report,
                report_csv,
                skip_report_header=True,
                skip_column_header=True,
                skip_report_summary=True,
                include_zero_impressions=True)

    adgroup_df = pd.read_csv(path, encoding="utf-8")
    if not isinstance(adgroup_df, pd.core.frame.DataFrame):
       print "Skipped because no ads are running in this account"
       print "=" * 131

    return adgroup_df
