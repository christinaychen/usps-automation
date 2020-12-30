import requests
import logging
import os

logging.basicConfig(level="INFO")

url = "https://secure.shippingapis.com/ShippingAPI.dll?API=CarrierPickupSchedule&XML="

userid = os.environ.get('USER_ID')
first_name = "Xinli"
last_name = "Zhang"
address2 = os.environ.get('ADDRESS')
city = "Cary"
state = "NC"
zip5 = "27519"
zip4 = "6554"
phone = os.environ.get('PHONE')
service_type = "FirstClass"
package_count = "120"
estimated_weight = "50"
package_location = "Front Door"
email_address = "cychen120@gmail.com"

xml = '<CarrierPickupScheduleRequest USERID="{}">\
<FirstName>{}</FirstName>\
<LastName>{}</LastName>\
<FirmName></FirmName>\
<SuiteOrApt></SuiteOrApt>\
<Address2>{}</Address2>\
<Urbanization></Urbanization>\
<City>{}</City>\
<State>{}</State>\
<ZIP5>{}</ZIP5>\
<ZIP4>{}</ZIP4>\
<Phone>{}</Phone>\
<Extension></Extension>\
<Package>\
<ServiceType>{}</ServiceType>\
<Count>{}</Count>\
</Package>\
<EstimatedWeight>{}</EstimatedWeight>\
<PackageLocation>{}</PackageLocation>\
<SpecialInstructions></SpecialInstructions>\
<EmailAddress>{}</EmailAddress>\
</CarrierPickupScheduleRequest>'.format(userid, first_name, last_name, address2, city, state, zip5, zip4, phone,
                                        service_type, package_count, estimated_weight, package_location, email_address)

if __name__ == '__main__':
    log = logging.getLogger("logger")
    # request_url = 'https://secure.shippingapis.com/ShippingAPI.dll?API=CarrierPickupAvailability&XML' \
    #               '=<CarrierPickupAvailabilityRequest ' \
    #               'USERID="{}"><FirmName></FirmName><SuiteOrApt></SuiteOrApt><Address2>{}' \
    #               '</Address2><Urbanization></Urbanization><City>Cary</City><State>NC</State><ZIP5>27519</ZIP5' \
    #               '><ZIP4>6554</ZIP4></CarrierPickupAvailabilityRequest>'.format(userid, address2)

    request_url = url + xml
    print("REQUEST URL: " + request_url)

    request = requests.get(request_url)
    status = request.status_code
    attempt = 1
    log.info("Made attempt {} of pickup scheduling".format(attempt))
    while status != 200 and attempt < 4:
        request = requests.get(request_url)
        status = request.status_code
        attempt += 1
        log.info("Made attempt {} of pickup scheduling".format(attempt))
    log.info("Response: {}".format(request.content))
