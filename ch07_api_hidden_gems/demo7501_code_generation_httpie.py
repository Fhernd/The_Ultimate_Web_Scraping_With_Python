import requests

url = "https://use1-prod-th.rbictg.com/graphql"

payload = [
    {
        "operationName": "GetRestaurants",
        "variables": {"input": {
                "filter": "NEARBY",
                "coordinates": {
                    "userLat": 43.6447708,
                    "userLng": -79.37330639999999,
                    "searchRadius": 8000
                },
                "first": 20,
                "status": "OPEN"
            }},
        "query": """query GetRestaurants($input: RestaurantsInput) {
  restaurants(input: $input) {
    pageInfo {
      hasNextPage
      endCursor
      __typename
    }
    totalCount
    nodes {
      ...RestaurantNodeFragment
      __typename
    }
    __typename
  }
}

fragment RestaurantNodeFragment on RestaurantNode {
  _id
  storeId
  isAvailable
  posVendor
  chaseMerchantId
  cateringHours {
    ...OperatingHoursFragment
    ...OperatingHoursFragment
    __typename
  }
  curbsideHours {
    ...OperatingHoursFragment
    __typename
  }
  cateringHours {
    ...OperatingHoursFragment
    __typename
  }
  timezone
  deliveryHours {
    ...OperatingHoursFragment
    __typename
  }
  diningRoomHours {
    ...OperatingHoursFragment
    __typename
  }
  distanceInMiles
  drinkStationType
  driveThruHours {
    ...OperatingHoursFragment
    __typename
  }
  driveThruLaneType
  email
  environment
  franchiseGroupId
  franchiseGroupName
  frontCounterClosed
  hasBreakfast
  hasBurgersForBreakfast
  hasCatering
  hasCurbside
  hasDelivery
  hasDineIn
  hasDriveThru
  hasTableService
  hasMobileOrdering
  hasLateNightMenu
  hasParking
  hasPlayground
  hasTakeOut
  hasWifi
  hasLoyalty
  id
  isDarkKitchen
  isFavorite
  isHalal
  isRecent
  latitude
  longitude
  mobileOrderingStatus
  name
  number
  parkingType
  phoneNumber
  physicalAddress {
    address1
    address2
    city
    country
    postalCode
    stateProvince
    stateProvinceShort
    __typename
  }
  playgroundType
  pos {
    vendor
    __typename
  }
  posRestaurantId
  restaurantImage {
    asset {
      _id
      metadata {
        lqip
        palette {
          dominant {
            background
            foreground
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    crop {
      top
      bottom
      left
      right
      __typename
    }
    hotspot {
      height
      width
      x
      y
      __typename
    }
    __typename
  }
  restaurantPosData {
    _id
    __typename
  }
  status
  vatNumber
  timezone
  __typename
}

fragment OperatingHoursFragment on OperatingHours {
  friClose
  friOpen
  monClose
  monOpen
  satClose
  satOpen
  sunClose
  sunOpen
  thrClose
  thrOpen
  tueClose
  tueOpen
  wedClose
  wedOpen
  __typename
}
"""
    }
]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "apollographql-client-name": "wl-web",
    "apollographql-client-version": "50b4a4a",
    "X-Session-Id": "9860be97-be70-4588-8704-e01466954643",
    "x-forter-token": "d91e7f32c1654d5f82872220f9b87556_1719415252700__UDF43-m4_13ck_tt",
    "x-user-datetime": "2024-06-26T10:21:37-05:00",
    "x-ui-language": "en",
    "x-ui-region": "CA",
    "x-ui-platform": "web",
    "Origin": "https://www.timhortons.ca",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Priority": "u=4",
    "TE": "trailers",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
