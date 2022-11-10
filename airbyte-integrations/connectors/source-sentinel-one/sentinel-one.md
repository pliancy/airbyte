# Sentinel One

 This page contains the setup guide and reference information for the Sentinel One source connector.

## Prerequisites

1. Please generate a `API_TOKEN`, from your Sentinel One account, by clicking on your user-email -> My user -> Options -> Generate API. 
  - Copy Paste the API TOKEN in a secure location.
2. Copy paste your account URL. 
  - URL: `https://www.user1.sentinelone.net/dashboard`
  - `your_management_url` would be `//www.user1.sentinelone.net`


## Setup guide
## Step 1: Set up the Sentinel One connector in Airbyte

### For Airbyte OSS:

1. Navigate to the Airbyte Open Source dashboard.
2. In the left navigation bar, click **Sources**. In the top-right corner, click **+new source**.
3. On the Set up the source page, enter the name for the `source-sentinel-one` connector and select **source-sentinel-one** from the Source type dropdown.
4. Enter your Prerequiste value `API_TOKEN` and `your_management_url`.
5. Select `Authenticate your account`.
6. Click **Set up source**.

## Supported sync modes

The Sentinel One source connector supports the following [sync modes](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):

| Feature           | Supported? |
| :---------------- | :--------- |
| Full Refresh Sync | Yes        |
| Incremental Sync  | No         |

## Suported Streams
#### Note: Need to have a Sentinel One account to read the API DOCs. <br>

End point Name - `Category` <br>


1. Activities
2. Accounts 
3. Agents
4. Config_override
5. Installed_applications - `Application Risk`
6. Installed_applications_cves - `Application Risk`
7. Alerts
8. Cloud_detection_rules
9. Blacklist(**args)
10. Exclusions
11. Filters
12. Firewall_control - `Firewall Control`
13. Firewall_control_protocols - `Firewall Control` 
14. Groups
15. Locations
16. Applications_catalog - `Marketplace`
17. Marketplace_installed_applications - `Marketplace`
18. Rbac_roles
19. Reports - `Reports` 
20. Report_tasks - `Reports` 
21. Service_users
22. Threats
23. Users