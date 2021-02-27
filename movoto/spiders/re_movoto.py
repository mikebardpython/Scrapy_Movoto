import scrapy
import json
from ..utils import cookie_parser

class ReMovotoSpider(scrapy.Spider):
    name = 're_movoto'
    allowed_domains = ['movoto.com']


    def start_requests(self):
        yield scrapy.Request(
            method='GET',
            url="https://www.movoto.com/api/v/search/?path=%2Ffor-sale%2Fmemphis-tn%2Fsingle-family%2Fprice-0-175000%2Fp-2%2F@40.9206784,-74.1081088%2F&fullUrlPath=%2Ffor-sale%2Fmemphis-tn%2Fsingle-family%2Fprice-0-175000%2Fp-2%2F@40.9206784,-74.1081088%2F",
            cookies=cookie_parser(),
            callback=self.parse,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
            },

        )

    def parse(self, response):
        resp_dict = json.loads(response.body)
        listings = resp_dict.get('data').get('listings')

        for listing in listings:
            daysOnMovoto = listing.get('daysOnMovoto')
            id = listing.get('id')
            tnImgPath = listing.get('tnImgPath')
            listDate = listing.get('listDate')
            listingAgent = listing.get('listingAgent')
            listPrice = listing.get('listPrice')
            lotSize = listing.get('lotSize')
            mlsDbNumber = listing.get('mlsDbNumber')
            mlsNumber = listing.get('mlsNumber')
            bath = listing.get('bath')
            bed = listing.get('bed')
            officeListName = listing.get('officeListName')
            photoCount = listing.get('photoCount')
            propertyType = listing.get('propertyType')
            propertyTypeDisplayName = listing.get('propertyTypeDisplayName')
            yearBuilt = listing.get('yearBuilt')
            zipCode = listing.get('zipCode')
            path = listing.get('path')
            status = listing.get('status')
            houseRealStatus = listing.get('houseRealStatus')
            propertyId = listing.get('propertyId')
            visibility = listing.get('visibility')
            soldDate = listing.get('soldDate')
            createdAt = listing.get('createdAt')
            imageDownloaderStatus = listing.get('imageDownloaderStatus')
            onMarketDateTime = listing.get('onMarketDateTime')

            address = listing.get('geo').get('address')
            city = listing.get('geo').get('city')
            state = listing.get('geo').get('state')
            zipcode = listing.get('geo').get('zipcode')

            total_listings = resp_dict.get('data').get('totalCount')
            page_size = resp_dict.get('data').get('pageSize')
            page_index = resp_dict.get('data').get('searchCondition').get('pageIndex')
            page_index = int(page_index)

            pagination = ((total_listings // page_size) + 1)

            # print(type(total_listings))
            # print(type(page_size))
            # print(type(page_index))
            # print(type(pagination))

            yield {
                'days_on_movoto': daysOnMovoto,
                'id': id,
                'tnImgPath': tnImgPath,
                'listDate': listDate,
                'listingAgent': listingAgent,
                'listPrice': listPrice,
                'lotSize': lotSize,
                'mlsDbNumber': mlsDbNumber,
                'mlsNumber': mlsNumber,
                'bath': bath,
                'bed': bed,
                'officeListName': officeListName,
                'photoCount': photoCount,
                'propertyType': propertyType,
                'propertyTypeDisplayName': propertyTypeDisplayName,
                'yearBuilt': yearBuilt,
                'zipCode': zipCode,
                'path': path,
                'status': status,
                'houseRealStatus': houseRealStatus,
                'propertyId': propertyId,
                'visibility': visibility,
                'soldDate': soldDate,
                'createdAt': createdAt,
                'imageDownloaderStatus': imageDownloaderStatus,
                'onMarketDateTime': onMarketDateTime,



                'address': address,
                'city': city,
                'state': state,
                'zipcode': zipcode,

                'page_size': page_size,
                'total_listings': total_listings,
                'page_index': page_index,
            }

            page = 1
            pagination = ((total_listings // page_size) + 1)
            for x in range(pagination):
                if page_index < pagination:
                    page += 1
                    next_url = f"https://www.movoto.com/api/v/search/?path=%2Ffor-sale%2Fmemphis-tn%2Fsingle-family%2Fprice-0-175000%2Fp-{page}%2F@40.9206784,-74.1081088%2F&fullUrlPath=%2Ffor-sale%2Fmemphis-tn%2Fsingle-family%2Fprice-0-175000%2Fp-{page}%2F@40.9206784,-74.1081088%2F"

                    yield scrapy.Request(
                        url=next_url,
                        method='GET',
                        callback=self.parse,
                        # meta={
                        #     'currentPage': page
                        # }
                    )




