# The Woobles USPS Pickup Automation
Script that runs every day at 7 AM EST to send a pickup request to USPS for the next day. Email confirmation will arrive a couple minutes after.

To run locally, set environment variables
`USER_ID`, `ADDRESS` and `PHONE`

```
USER_ID={USPS_USER_ID} ADDRESS='{ADDRESS}' PHONE={PHONE} python pickup-automation.py
```
