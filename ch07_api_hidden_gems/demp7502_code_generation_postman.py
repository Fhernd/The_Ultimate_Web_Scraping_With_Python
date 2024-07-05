import requests
import json

url = "https://use1-prod-th.rbictg.com/graphql"

payload = json.dumps([
  {
    "operationName": "GetRestaurants",
    "variables": {
      "input": {
        "filter": "NEARBY",
        "coordinates": {
          "userLat": 54.3979972,
          "userLng": -126.6482087,
          "searchRadius": 8000
        },
        "first": 20,
        "status": "OPEN"
      }
    },
    "query": "query GetRestaurants($input: RestaurantsInput) {\n  restaurants(input: $input) {\n    pageInfo {\n      hasNextPage\n      endCursor\n      __typename\n    }\n    totalCount\n    nodes {\n      ...RestaurantNodeFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment RestaurantNodeFragment on RestaurantNode {\n  _id\n  storeId\n  isAvailable\n  posVendor\n  chaseMerchantId\n  cateringHours {\n    ...OperatingHoursFragment\n    ...OperatingHoursFragment\n    __typename\n  }\n  curbsideHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  cateringHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  timezone\n  deliveryHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  diningRoomHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  distanceInMiles\n  drinkStationType\n  driveThruHours {\n    ...OperatingHoursFragment\n    __typename\n  }\n  driveThruLaneType\n  email\n  environment\n  franchiseGroupId\n  franchiseGroupName\n  frontCounterClosed\n  hasBreakfast\n  hasBurgersForBreakfast\n  hasCatering\n  hasCurbside\n  hasDelivery\n  hasDineIn\n  hasDriveThru\n  hasTableService\n  hasMobileOrdering\n  hasLateNightMenu\n  hasParking\n  hasPlayground\n  hasTakeOut\n  hasWifi\n  hasLoyalty\n  id\n  isDarkKitchen\n  isFavorite\n  isHalal\n  isRecent\n  latitude\n  longitude\n  mobileOrderingStatus\n  name\n  number\n  parkingType\n  phoneNumber\n  physicalAddress {\n    address1\n    address2\n    city\n    country\n    postalCode\n    stateProvince\n    stateProvinceShort\n    __typename\n  }\n  playgroundType\n  pos {\n    vendor\n    __typename\n  }\n  posRestaurantId\n  restaurantImage {\n    asset {\n      _id\n      metadata {\n        lqip\n        palette {\n          dominant {\n            background\n            foreground\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    crop {\n      top\n      bottom\n      left\n      right\n      __typename\n    }\n    hotspot {\n      height\n      width\n      x\n      y\n      __typename\n    }\n    __typename\n  }\n  restaurantPosData {\n    _id\n    __typename\n  }\n  status\n  vatNumber\n  timezone\n  __typename\n}\n\nfragment OperatingHoursFragment on OperatingHours {\n  friClose\n  friOpen\n  monClose\n  monOpen\n  satClose\n  satOpen\n  sunClose\n  sunOpen\n  thrClose\n  thrOpen\n  tueClose\n  tueOpen\n  wedClose\n  wedOpen\n  __typename\n}\n"
  }
])
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
  'Accept': '*/*',
  'Accept-Language': 'en-GB,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'content-type': 'application/json',
  'apollographql-client-name': 'wl-web',
  'apollographql-client-version': '4238baf',
  'X-Session-Id': '9860be97-be70-4588-8704-e01466954643',
  'x-forter-token': 'd91e7f32c1654d5f82872220f9b87556_1720176283477__UDF43-m4_13ck_tt',
  'x-user-datetime': '2024-07-05T05:45:47-05:00',
  'x-ui-language': 'en',
  'x-ui-region': 'CA',
  'x-ui-platform': 'web',
  'Origin': 'https://www.timhortons.ca',
  'Connection': 'keep-alive',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'cross-site',
  'Priority': 'u=4',
  'TE': 'trailers'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
