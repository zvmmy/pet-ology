from app import parks_db, gmaps
parks_beaches = [
    {
        "name": "Marymoor Park",
        "address": "6046 West Lake Sammamish Pkwy NE, Redmond, WA 98052",
    },
    {
        "name": "Jasper Dog Park",
        "address": "11225 NE 120th St, Kirkland, WA 98034",
    },
    {
        "name": "Grass Lawn Park",
        "address": "7031 148th Ave NE, Redmond, WA 98052",
    },
    {
        "name": "Mark Twain Park",
        "address": "10625 132nd Ave NE, Kirkland, WA 98033",
    },
    {
        "name": "Sixty Acres Park",
        "address": "15200 NE 116th St, Redmond, WA 98052",
    },
    {
        "name": "Hartman Park",
        "address": "17300 NE 104th St, Redmond, WA 98052",
    },
    {
        "name": "Bear Creek Park",
        "address": "Evans Creek Trail, Redmond, WA 98053",
    },
    {
        "name": "Bridle Trails State Park",
        "address": "5300 116th Ave NE, Kirkland, WA 98033",
    },
    {
        "name": "Richmond Beach Saltwater Park",
        "address": "2021 NW 190th St, Shoreline, WA 98177",
    },
    {
        "name": "Luther Burbank Park",
        "address": "2040 84th Ave SE, Mercer Island, WA 98040",
    },
    {
        "name": "Idylwood Park",
        "address": "3650 West Lake Sammamish Pkwy NE, Redmond, WA 98052",
    },
    {
        "name": "Tambark Creek Park",
        "address": "17217 35th Ave SE, Bothell, WA 98012",
    },
    {
        "name": "Warren G. Magnuson Park Off Leash Area",
        "address": "7400 Sand Point Way NE, Seattle, WA 98115",
    },


]
for park in parks_beaches:
    parks_db.insert({
        "name": park["name"],
        "address": park["address"],
        "coord": gmaps.geocode(park["address"])[0]["geometry"]["location"]

    })
