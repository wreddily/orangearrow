## orangearrow

### A Python library for interacting with the Amazon Product Advertising API.

#### What is it?

[orangearrow](https://github.com/wreddily/orangearrow) is a Python library that simplifies usage of the [Amazon Product Advertising API](https://docs.aws.amazon.com/AWSECommerceService/latest/GSG/Welcome.html). It aims to be easy to use, flexible and gets out of your way when you need it to.

#### What do I need to get started?

You will need an Amazon Associate Tag and Amazon API credentials. All of that is covered [here](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/becomingDev.html).

#### How do I use it?

To use Search or Lookup functionality, first create an instance of the `AmazonProductAPI` class. You will need to pass your Amazon API credentials like so:

    from orangearrow import AmazonProductAPI

    amazon_api = AmazonProductAPI(
        access_key='AKIAIOSFODNN7EXAMPLE',
        secret_key='1234567890',
        associate_tag='mytag-20'
    )

##### Search

To search for items, use the `item_search` method with a valid [Search Index](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/LocaleUS.html) and a list of keywords:

    search_response = amazon_api.item_search(
        'Electronics',
        ['Television', 'Flatscreen',]
    )

You can also optionally pass a `page` parameter to paginate results:

    search_response = amazon_api.item_search(
        'Electronics',
        ['Television', 'Flatscreen',],
        page=2
    )

As well as specifying [Response Groups](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/CHAP_ResponseGroupsList.html) to filter the information that you want returned:

    search_response = amazon_api.item_search(
        'Electronics',
        ['Television', 'Flatscreen',],
        page=2,
        response_groups=['Variations', 'Reviews',],
    )

To customize the request even further, you can add any [ItemSearch parameters supported by the Amazon API](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/ItemSearch.html#ItemSearch-rp) into a `parameters` dictionary:

    search_response = amazon_api.item_search(
        'Electronics',
        ['Television', 'Flatscreen',],
        parameters={
            'Brand': 'Sony',
            'MaximumPrice': '50000',
        }
    )

##### Item Lookup

The `item_lookup` method can be used to look up individual items by their ASIN ID:

    product_response = amazon_api.item_lookup('B07D4FQB8S')

Or by a different supported [IdType](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/ItemLookup.html) and [Search Index](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/LocaleUS.html):

    product_response = amazon_api.item_lookup(
        '602498631416',
        search_index='Music',
        id_type='UPC'
    )

Similar to the `search` method, `response_groups` and extra `parameters` supported by [ItemSearch](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/ItemLookup.html#ItemLookup-rp) may also be used:

    product_response = amazon_api.item_lookup(
        '602498631416',
        search_index='Music',
        id_type='UPC',
        response_groups=['Reviews'],
        parameters={'TruncateReviewsAt': 200}
    )

##### Similarity Lookup

The `similarity_lookup` method can be used to find similar items for one or more ASIN values:

    similarities_response = amazon_api.similarity_lookup(['B00JFC9ALE', 'B06XY1YTMJ'])

This method will also accept `response_groups` and additional `parameters` that are supported by [Similarity Lookup](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/SimilarityLookup.html#SimilarityLookup-rp):

    similarities_response = amazon_api.similarity_lookup(
        ['B00JFC9ALE', 'B06XY1YTMJ'],
        response_groups=['EditorialReview'],
        parameters={'MerchantId': 'Amazon'}
    )

##### Responses

In the Search and Lookup examples above, an instance of `AmazonProductAPIResponse` will be returned. The returned data can be accessed in a dictionary via the `data` property of the response:

    search_response.data

Or the raw XML can be accessed via the `raw_response_content` property:

    search_response.raw_response_content

If any errors occurred, the following properties will contain error information:

    search_response.is_error
    search_response.error_code
    search_response.error_msg

The instance will also contain the response's status code and headers:

    search_response.status_code
    search_response.headers

