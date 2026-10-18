
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fetch_analysis")

@mcp.tool()
async def fetch_analysis()->str:
    return json.dumps([
    {
        "ga_session_id": "1729213694",
        "client_id": "8410291.1729213694",
        "linked_clarity_id": "ms_clarity_98410291",
        "session_start": "2026-10-18T01:08:14Z",
        "session_end": "2026-10-18T01:13:42Z",
        "session_duration_seconds": 328,
        "geo": {"country": "United Kingdom", "city": "London"},
        "device": {"category": "mobile", "operating_system": "iOS", "browser": "Safari"},
        "traffic_source": {"source": "google", "medium": "organic"},
        "page_paths": ["/", "/collections/electronics", "/products/noise-canceling-headphones"],
        "events": [
            {"event_name": "session_start", "timestamp": "2026-10-18T01:08:14Z"},
            {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T01:08:15Z"},
            {"event_name": "page_view", "page_path": "/collections/electronics", "timestamp": "2026-10-18T01:09:20Z"},
            {"event_name": "view_item_list", "item_category": "electronics", "timestamp": "2026-10-18T01:09:21Z"},
            {"event_name": "page_view", "page_path": "/products/noise-canceling-headphones", "timestamp": "2026-10-18T01:10:45Z"},
            {"event_name": "view_item", "item_id": "NCH-001", "item_name": "Noise-Canceling Headphones", "timestamp": "2026-10-18T01:10:46Z"},
            {"event_name": "scroll", "percent_scrolled": 85, "timestamp": "2026-10-18T01:12:30Z"},
            {"event_name": "user_engagement", "engagement_time_msec": 328000, "timestamp": "2026-10-18T01:13:42Z"}
        ],
        "ecommerce": {"items_viewed": 1, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
    },
    {
        "ga_session_id": "1729214585",
        "client_id": "8410344.1729214585",
        "linked_clarity_id": "ms_clarity_98410344",
        "session_start": "2026-10-18T01:23:05Z",
        "session_end": "2026-10-18T01:25:50Z",
        "session_duration_seconds": 165,
        "geo": {"country": "India", "city": "Mumbai"},
        "device": {"category": "desktop", "operating_system": "Windows", "browser": "Chrome"},
        "traffic_source": {"source": "(direct)", "medium": "(none)"},
        "page_paths": ["/", "/collections/apparel/sale", "/products/merino-wool-pullover"],
        "events": [
            {"event_name": "session_start", "timestamp": "2026-10-18T01:23:05Z"},
            {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T01:23:05Z"},
            {"event_name": "page_view", "page_path": "/collections/apparel/sale", "timestamp": "2026-10-18T01:23:40Z"},
            {"event_name": "filter_applied", "filter_type": "size", "filter_value": "Large", "timestamp": "2026-10-18T01:24:10Z"},
            {"event_name": "page_view", "page_path": "/products/merino-wool-pullover", "timestamp": "2026-10-18T01:24:35Z"},
            {"event_name": "view_item", "item_id": "MWP-L-02", "item_name": "Merino Wool Pullover", "timestamp": "2026-10-18T01:24:36Z"},
            {"event_name": "user_engagement", "engagement_time_msec": 165000, "timestamp": "2026-10-18T01:25:50Z"}
        ],
        "ecommerce": {"items_viewed": 1, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
    }])#,
#     {
#         "ga_session_id": "1729215922",
#         "client_id": "8410419.1729215922",
#         "linked_clarity_id": "ms_clarity_98410419",
#         "session_start": "2026-10-18T01:45:22Z",
#         "session_end": "2026-10-18T01:48:10Z",
#         "session_duration_seconds": 168,
#         "geo": {"country": "Germany", "city": "Berlin"},
#         "device": {"category": "desktop", "operating_system": "macOS", "browser": "Safari"},
#         "traffic_source": {"source": "email", "medium": "order_notification"},
#         "page_paths": ["/account/login", "/account/orders"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T01:45:22Z"},
#             {"event_name": "page_view", "page_path": "/account/login", "timestamp": "2026-10-18T01:45:22Z"},
#             {"event_name": "login", "method": "credentials", "timestamp": "2026-10-18T01:46:12Z"},
#             {"event_name": "page_view", "page_path": "/account/orders", "timestamp": "2026-10-18T01:46:14Z"},
#             {"event_name": "file_download", "file_name": "invoice_89211.pdf", "timestamp": "2026-10-18T01:47:30Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 168000, "timestamp": "2026-10-18T01:48:10Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729217499",
#         "client_id": "8410492.1729217499",
#         "linked_clarity_id": "ms_clarity_98410492",
#         "session_start": "2026-10-18T02:11:39Z",
#         "session_end": "2026-10-18T02:18:04Z",
#         "session_duration_seconds": 385,
#         "geo": {"country": "Canada", "city": "Toronto"},
#         "device": {"category": "mobile", "operating_system": "Android", "browser": "Chrome"},
#         "traffic_source": {"source": "google", "medium": "cpc"},
#         "page_paths": ["/", "/products/smart-home-hub", "/cart"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T02:11:39Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T02:11:39Z"},
#             {"event_name": "page_view", "page_path": "/products/smart-home-hub", "timestamp": "2026-10-18T02:12:45Z"},
#             {"event_name": "view_item", "item_id": "SHH-401", "item_name": "Smart Home Hub", "timestamp": "2026-10-18T02:12:46Z"},
#             {"event_name": "add_to_cart", "item_id": "SHH-401", "value": 129.99, "currency": "CAD", "timestamp": "2026-10-18T02:14:10Z"},
#             {"event_name": "page_view", "page_path": "/cart", "timestamp": "2026-10-18T02:14:12Z"},
#             {"event_name": "view_cart", "value": 129.99, "currency": "CAD", "timestamp": "2026-10-18T02:14:13Z"},
#             {"event_name": "estimate_shipping", "region": "Ontario", "timestamp": "2026-10-18T02:15:20Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 385000, "timestamp": "2026-10-18T02:18:04Z"}
#         ],
#         "ecommerce": {"items_viewed": 1, "items_added_to_cart": 1, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729218858",
#         "client_id": "8410531.1729218858",
#         "linked_clarity_id": "ms_clarity_98410531",
#         "session_start": "2026-10-18T02:34:18Z",
#         "session_end": "2026-10-18T02:36:20Z",
#         "session_duration_seconds": 122,
#         "geo": {"country": "Australia", "city": "Sydney"},
#         "device": {"category": "tablet", "operating_system": "iOS", "browser": "Safari"},
#         "traffic_source": {"source": "partner_referral", "medium": "referral"},
#         "page_paths": ["/", "/pages/about-us", "/pages/contact"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T02:34:18Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T02:34:18Z"},
#             {"event_name": "page_view", "page_path": "/pages/about-us", "timestamp": "2026-10-18T02:34:55Z"},
#             {"event_name": "page_view", "page_path": "/pages/contact", "timestamp": "2026-10-18T02:35:40Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 122000, "timestamp": "2026-10-18T02:36:20Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729219965",
#         "client_id": "8410588.1729219965",
#         "linked_clarity_id": "ms_clarity_98410588",
#         "session_start": "2026-10-18T02:52:45Z",
#         "session_end": "2026-10-18T02:54:15Z",
#         "session_duration_seconds": 90,
#         "geo": {"country": "United States", "city": "New York"},
#         "device": {"category": "mobile", "operating_system": "iOS", "browser": "Safari"},
#         "traffic_source": {"source": "pinterest", "medium": "social"},
#         "page_paths": ["/collections/footwear"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T02:52:45Z"},
#             {"event_name": "page_view", "page_path": "/collections/footwear", "timestamp": "2026-10-18T02:52:45Z"},
#             {"event_name": "view_item_list", "item_category": "footwear", "timestamp": "2026-10-18T02:52:46Z"},
#             {"event_name": "sort_applied", "sort_direction": "price_asc", "timestamp": "2026-10-18T02:53:15Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 90000, "timestamp": "2026-10-18T02:54:15Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729221302",
#         "client_id": "8410612.1729221302",
#         "linked_clarity_id": "ms_clarity_98410612",
#         "session_start": "2026-10-18T03:15:02Z",
#         "session_end": "2026-10-18T03:19:40Z",
#         "session_duration_seconds": 278,
#         "geo": {"country": "United States", "city": "Austin"},
#         "device": {"category": "desktop", "operating_system": "Windows", "browser": "Firefox"},
#         "traffic_source": {"source": "(direct)", "medium": "(none)"},
#         "page_paths": ["/", "/search?q=mechanical+keyboard", "/products/rgb-mechanical-keyboard"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T03:15:02Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T03:15:02Z"},
#             {"event_name": "view_search_results", "search_term": "mechanical keyboard", "timestamp": "2026-10-18T03:15:44Z"},
#             {"event_name": "page_view", "page_path": "/search?q=mechanical+keyboard", "timestamp": "2026-10-18T03:15:44Z"},
#             {"event_name": "page_view", "page_path": "/products/rgb-mechanical-keyboard", "timestamp": "2026-10-18T03:16:30Z"},
#             {"event_name": "view_item", "item_id": "KB-RGB-09", "item_name": "RGB Mechanical Keyboard", "timestamp": "2026-10-18T03:16:31Z"},
#             {"event_name": "add_to_wishlist", "item_id": "KB-RGB-09", "timestamp": "2026-10-18T03:18:50Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 278000, "timestamp": "2026-10-18T03:19:40Z"}
#         ],
#         "ecommerce": {"items_viewed": 1, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729222691",
#         "client_id": "8410667.1729222691",
#         "linked_clarity_id": "ms_clarity_98410667",
#         "session_start": "2026-10-18T03:38:11Z",
#         "session_end": "2026-10-18T03:40:02Z",
#         "session_duration_seconds": 111,
#         "geo": {"country": "Singapore", "city": "Singapore"},
#         "device": {"category": "mobile", "operating_system": "Android", "browser": "Samsung Internet"},
#         "traffic_source": {"source": "instagram", "medium": "social_story"},
#         "page_paths": ["/blogs/news/top-10-winter-essentials"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T03:38:11Z"},
#             {"event_name": "page_view", "page_path": "/blogs/news/top-10-winter-essentials", "timestamp": "2026-10-18T03:38:11Z"},
#             {"event_name": "scroll", "percent_scrolled": 100, "timestamp": "2026-10-18T03:39:40Z"},
#             {"event_name": "click_outbound", "url": "https://affiliate.partner.com/winter-deal", "timestamp": "2026-10-18T03:39:58Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 111000, "timestamp": "2026-10-18T03:40:02Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729223970",
#         "client_id": "8410705.1729223970",
#         "linked_clarity_id": "ms_clarity_98410705",
#         "session_start": "2026-10-18T03:59:30Z",
#         "session_end": "2026-10-18T04:02:12Z",
#         "session_duration_seconds": 162,
#         "geo": {"country": "Ireland", "city": "Dublin"},
#         "device": {"category": "desktop", "operating_system": "macOS", "browser": "Chrome"},
#         "traffic_source": {"source": "google", "medium": "organic"},
#         "page_paths": ["/", "/collections/all"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T03:59:30Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T03:59:30Z"},
#             {"event_name": "page_view", "page_path": "/collections/all", "timestamp": "2026-10-18T04:00:15Z"},
#             {"event_name": "view_item_list", "item_category": "all", "timestamp": "2026-10-18T04:00:16Z"},
#             {"event_name": "pagination_click", "page_number": 2, "timestamp": "2026-10-18T04:01:25Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 162000, "timestamp": "2026-10-18T04:02:12Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729225100",
#         "client_id": "8410754.1729225100",
#         "linked_clarity_id": "ms_clarity_98410754",
#         "session_start": "2026-10-18T04:18:20Z",
#         "session_end": "2026-10-18T04:22:45Z",
#         "session_duration_seconds": 265,
#         "geo": {"country": "India", "city": "Delhi"},
#         "device": {"category": "mobile", "operating_system": "iOS", "browser": "Safari"},
#         "traffic_source": {"source": "(direct)", "medium": "(none)"},
#         "page_paths": ["/", "/products/leather-messenger-bag", "/pages/shipping-policy"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T04:18:20Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T04:18:20Z"},
#             {"event_name": "page_view", "page_path": "/products/leather-messenger-bag", "timestamp": "2026-10-18T04:19:10Z"},
#             {"event_name": "view_item", "item_id": "LMB-55", "item_name": "Leather Messenger Bag", "timestamp": "2026-10-18T04:19:11Z"},
#             {"event_name": "page_view", "page_path": "/pages/shipping-policy", "timestamp": "2026-10-18T04:21:05Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 265000, "timestamp": "2026-10-18T04:22:45Z"}
#         ],
#         "ecommerce": {"items_viewed": 1, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729226469",
#         "client_id": "8410811.1729226469",
#         "linked_clarity_id": "ms_clarity_98410811",
#         "session_start": "2026-10-18T04:41:09Z",
#         "session_end": "2026-10-18T04:43:00Z",
#         "session_duration_seconds": 111,
#         "geo": {"country": "France", "city": "Paris"},
#         "device": {"category": "desktop", "operating_system": "Windows", "browser": "Edge"},
#         "traffic_source": {"source": "google", "medium": "organic"},
#         "page_paths": ["/pages/faq"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T04:41:09Z"},
#             {"event_name": "page_view", "page_path": "/pages/faq", "timestamp": "2026-10-18T04:41:09Z"},
#             {"event_name": "faq_accordion_expand", "question_topic": "international_warranty", "timestamp": "2026-10-18T04:41:40Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 111000, "timestamp": "2026-10-18T04:43:00Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729227770",
#         "client_id": "8410860.1729227770",
#         "linked_clarity_id": "ms_clarity_98410860",
#         "session_start": "2026-10-18T05:02:50Z",
#         "session_end": "2026-10-18T05:08:15Z",
#         "session_duration_seconds": 325,
#         "geo": {"country": "India", "city": "Bengaluru"},
#         "device": {"category": "mobile", "operating_system": "Android", "browser": "Chrome"},
#         "traffic_source": {"source": "facebook", "medium": "cpc"},
#         "page_paths": ["/", "/collections/kitchenware", "/products/cast-iron-skillet", "/cart"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T05:02:50Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T05:02:50Z"},
#             {"event_name": "page_view", "page_path": "/collections/kitchenware", "timestamp": "2026-10-18T05:03:30Z"},
#             {"event_name": "view_item_list", "item_category": "kitchenware", "timestamp": "2026-10-18T05:03:31Z"},
#             {"event_name": "page_view", "page_path": "/products/cast-iron-skillet", "timestamp": "2026-10-18T05:04:10Z"},
#             {"event_name": "view_item", "item_id": "CIS-10", "item_name": "Cast Iron Skillet", "timestamp": "2026-10-18T05:04:11Z"},
#             {"event_name": "add_to_cart", "item_id": "CIS-10", "value": 45.00, "currency": "INR", "timestamp": "2026-10-18T05:05:02Z"},
#             {"event_name": "page_view", "page_path": "/cart", "timestamp": "2026-10-18T05:05:05Z"},
#             {"event_name": "view_cart", "value": 45.00, "currency": "INR", "timestamp": "2026-10-18T05:05:06Z"},
#             {"event_name": "apply_coupon_failure", "coupon_code": "SAVE20", "reason": "expired", "timestamp": "2026-10-18T05:06:40Z"},
#             {"event_name": "remove_from_cart", "item_id": "CIS-10", "timestamp": "2026-10-18T05:07:30Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 325000, "timestamp": "2026-10-18T05:08:15Z"}
#         ],
#         "ecommerce": {"items_viewed": 1, "items_added_to_cart": 1, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729228773",
#         "client_id": "8410903.1729228773",
#         "linked_clarity_id": "ms_clarity_98410903",
#         "session_start": "2026-10-18T05:19:33Z",
#         "session_end": "2026-10-18T05:21:40Z",
#         "session_duration_seconds": 127,
#         "geo": {"country": "United Arab Emirates", "city": "Dubai"},
#         "device": {"category": "tablet", "operating_system": "Android", "browser": "Chrome"},
#         "traffic_source": {"source": "google", "medium": "organic"},
#         "page_paths": ["/", "/collections/new-arrivals"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T05:19:33Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T05:19:33Z"},
#             {"event_name": "page_view", "page_path": "/collections/new-arrivals", "timestamp": "2026-10-18T05:20:15Z"},
#             {"event_name": "view_item_list", "item_category": "new-arrivals", "timestamp": "2026-10-18T05:20:16Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 127000, "timestamp": "2026-10-18T05:21:40Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729229832",
#         "client_id": "8410948.1729229832",
#         "linked_clarity_id": "ms_clarity_98410948",
#         "session_start": "2026-10-18T05:37:12Z",
#         "session_end": "2026-10-18T05:42:01Z",
#         "session_duration_seconds": 289,
#         "geo": {"country": "Netherlands", "city": "Amsterdam"},
#         "device": {"category": "desktop", "operating_system": "macOS", "browser": "Chrome"},
#         "traffic_source": {"source": "(direct)", "medium": "(none)"},
#         "page_paths": ["/collections/office-furniture", "/products/ergonomic-desk-chair"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T05:37:12Z"},
#             {"event_name": "page_view", "page_path": "/collections/office-furniture", "timestamp": "2026-10-18T05:37:12Z"},
#             {"event_name": "view_item_list", "item_category": "office-furniture", "timestamp": "2026-10-18T05:37:13Z"},
#             {"event_name": "page_view", "page_path": "/products/ergonomic-desk-chair", "timestamp": "2026-10-18T05:38:20Z"},
#             {"event_name": "view_item", "item_id": "EDC-909", "item_name": "Ergonomic Desk Chair", "timestamp": "2026-10-18T05:38:21Z"},
#             {"event_name": "copy_sku", "sku": "EDC-909-GRY", "timestamp": "2026-10-18T05:41:10Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 289000, "timestamp": "2026-10-18T05:42:01Z"}
#         ],
#         "ecommerce": {"items_viewed": 1, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729230867",
#         "client_id": "8411001.1729230867",
#         "linked_clarity_id": "ms_clarity_98411001",
#         "session_start": "2026-10-18T05:54:27Z",
#         "session_end": "2026-10-18T05:56:10Z",
#         "session_duration_seconds": 103,
#         "geo": {"country": "India", "city": "Hyderabad"},
#         "device": {"category": "mobile", "operating_system": "iOS", "browser": "Safari"},
#         "traffic_source": {"source": "google", "medium": "organic"},
#         "page_paths": ["/", "/pages/store-locator"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T05:54:27Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T05:54:27Z"},
#             {"event_name": "page_view", "page_path": "/pages/store-locator", "timestamp": "2026-10-18T05:55:01Z"},
#             {"event_name": "geolocation_permission_granted", "timestamp": "2026-10-18T05:55:20Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 103000, "timestamp": "2026-10-18T05:56:10Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729231928",
#         "client_id": "8411045.1729231928",
#         "linked_clarity_id": "ms_clarity_98411045",
#         "session_start": "2026-10-18T06:12:08Z",
#         "session_end": "2026-10-18T06:19:50Z",
#         "session_duration_seconds": 462,
#         "geo": {"country": "Japan", "city": "Tokyo"},
#         "device": {"category": "desktop", "operating_system": "Windows", "browser": "Chrome"},
#         "traffic_source": {"source": "newsletter", "medium": "email"},
#         "page_paths": ["/", "/products/ceramic-pour-over-set", "/cart", "/checkout"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T06:12:08Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T06:12:08Z"},
#             {"event_name": "page_view", "page_path": "/products/ceramic-pour-over-set", "timestamp": "2026-10-18T06:13:20Z"},
#             {"event_name": "view_item", "item_id": "CPS-88", "item_name": "Ceramic Pour Over Set", "timestamp": "2026-10-18T06:13:21Z"},
#             {"event_name": "add_to_cart", "item_id": "CPS-88", "value": 65.00, "currency": "USD", "timestamp": "2026-10-18T06:14:45Z"},
#             {"event_name": "page_view", "page_path": "/cart", "timestamp": "2026-10-18T06:14:50Z"},
#             {"event_name": "view_cart", "value": 65.00, "currency": "USD", "timestamp": "2026-10-18T06:14:51Z"},
#             {"event_name": "page_view", "page_path": "/checkout", "timestamp": "2026-10-18T06:15:30Z"},
#             {"event_name": "begin_checkout", "value": 65.00, "currency": "USD", "items_count": 1, "timestamp": "2026-10-18T06:15:32Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 462000, "timestamp": "2026-10-18T06:19:50Z"}
#         ],
#         "ecommerce": {"items_viewed": 1, "items_added_to_cart": 1, "checkouts": 1, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729232924",
#         "client_id": "8411090.1729232924",
#         "linked_clarity_id": "ms_clarity_98411090",
#         "session_start": "2026-10-18T06:28:44Z",
#         "session_end": "2026-10-18T06:31:05Z",
#         "session_duration_seconds": 141,
#         "geo": {"country": "India", "city": "Chennai"},
#         "device": {"category": "mobile", "operating_system": "Android", "browser": "Chrome"},
#         "traffic_source": {"source": "google", "medium": "cpc"},
#         "page_paths": ["/collections/footwear/sneakers", "/products/retro-runner-white"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T06:28:44Z"},
#             {"event_name": "page_view", "page_path": "/collections/footwear/sneakers", "timestamp": "2026-10-18T06:28:44Z"},
#             {"event_name": "page_view", "page_path": "/products/retro-runner-white", "timestamp": "2026-10-18T06:29:20Z"},
#             {"event_name": "view_item", "item_id": "RRW-01", "item_name": "Retro Runner White", "timestamp": "2026-10-18T06:29:21Z"},
#             {"event_name": "view_out_of_stock_variant", "variant_size": "UK 9", "timestamp": "2026-10-18T06:30:15Z"},
#             {"event_name": "generate_lead", "lead_type": "restock_notification", "timestamp": "2026-10-18T06:30:50Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 141000, "timestamp": "2026-10-18T06:31:05Z"}
#         ],
#         "ecommerce": {"items_viewed": 1, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729233615",
#         "client_id": "8411132.1729233615",
#         "linked_clarity_id": "ms_clarity_98411132",
#         "session_start": "2026-10-18T06:40:15Z",
#         "session_end": "2026-10-18T06:43:20Z",
#         "session_duration_seconds": 185,
#         "geo": {"country": "United States", "city": "San Francisco"},
#         "device": {"category": "desktop", "operating_system": "macOS", "browser": "Safari"},
#         "traffic_source": {"source": "audit_tool", "medium": "referral"},
#         "page_paths": ["/policies/privacy-policy", "/policies/terms-of-service"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T06:40:15Z"},
#             {"event_name": "page_view", "page_path": "/policies/privacy-policy", "timestamp": "2026-10-18T06:40:15Z"},
#             {"event_name": "page_view", "page_path": "/policies/terms-of-service", "timestamp": "2026-10-18T06:41:40Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 185000, "timestamp": "2026-10-18T06:43:20Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729234190",
#         "client_id": "8411178.1729234190",
#         "linked_clarity_id": "ms_clarity_98411178",
#         "session_start": "2026-10-18T06:49:50Z",
#         "session_end": "2026-10-18T06:52:10Z",
#         "session_duration_seconds": 140,
#         "geo": {"country": "United States", "city": "Chicago"},
#         "device": {"category": "mobile", "operating_system": "iOS", "browser": "Safari"},
#         "traffic_source": {"source": "push_notification", "medium": "crm"},
#         "page_paths": ["/", "/collections/clearance"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T06:49:50Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T06:49:50Z"},
#             {"event_name": "page_view", "page_path": "/collections/clearance", "timestamp": "2026-10-18T06:50:20Z"},
#             {"event_name": "view_item_list", "item_category": "clearance", "timestamp": "2026-10-18T06:50:21Z"},
#             {"event_name": "scroll", "percent_scrolled": 70, "timestamp": "2026-10-18T06:51:30Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 140000, "timestamp": "2026-10-18T06:52:10Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     },
#     {
#         "ga_session_id": "1729234624",
#         "client_id": "8411215.1729234624",
#         "linked_clarity_id": "ms_clarity_98411215",
#         "session_start": "2026-10-18T06:57:04Z",
#         "session_end": "2026-10-18T06:59:48Z",
#         "session_duration_seconds": 164,
#         "geo": {"country": "India", "city": "Pune"},
#         "device": {"category": "desktop", "operating_system": "Windows", "browser": "Chrome"},
#         "traffic_source": {"source": "(direct)", "medium": "(none)"},
#         "page_paths": ["/", "/pages/newsletter-signup", "/collections/all"],
#         "events": [
#             {"event_name": "session_start", "timestamp": "2026-10-18T06:57:04Z"},
#             {"event_name": "page_view", "page_path": "/", "timestamp": "2026-10-18T06:57:04Z"},
#             {"event_name": "page_view", "page_path": "/pages/newsletter-signup", "timestamp": "2026-10-18T06:57:40Z"},
#             {"event_name": "generate_lead", "lead_type": "footer_newsletter", "timestamp": "2026-10-18T06:58:15Z"},
#             {"event_name": "page_view", "page_path": "/collections/all", "timestamp": "2026-10-18T06:58:40Z"},
#             {"event_name": "view_item_list", "item_category": "all", "timestamp": "2026-10-18T06:58:41Z"},
#             {"event_name": "user_engagement", "engagement_time_msec": 164000, "timestamp": "2026-10-18T06:59:48Z"}
#         ],
#         "ecommerce": {"items_viewed": 0, "items_added_to_cart": 0, "checkouts": 0, "transactions": 0, "revenue": 0.0}
#     }
# ])

if __name__ == "__main__":
    mcp.run(transport = "stdio")