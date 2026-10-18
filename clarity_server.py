import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fetch_summaries")

@mcp.tool()
async def fetch_summaries()->str:
    return json.dumps([
    {
        "session_id": "ms_clarity_98410291",
        "start_time": "2026-10-18T01:08:14Z",
        "end_time": "2026-10-18T01:13:42Z",
        "duration_seconds": 328,
        "device": "Mobile (iOS / Safari)",
        "geo_location": "London, United Kingdom",
        "pages_visited": ["/", "/collections/electronics", "/products/noise-canceling-headphones"],
        "metrics": {"total_clicks": 14, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 85},
        "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 110},
        "copilot_summary": "The user arrived via organic search and browsed the electronics collection. They spent nearly 3 minutes on the noise-canceling headphones product page, expanded the technical specifications accordion, read customer reviews, but closed the browser tab without adding the item to the cart."
    },
    {
        "session_id": "ms_clarity_98410344",
        "start_time": "2026-10-18T01:23:05Z",
        "end_time": "2026-10-18T01:25:50Z",
        "duration_seconds": 165,
        "device": "Desktop (Windows 11 / Chrome)",
        "geo_location": "Mumbai, India",
        "pages_visited": ["/", "/collections/apparel/sale", "/products/merino-wool-pullover"],
        "metrics": {"total_clicks": 9, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 72},
        "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 94},
        "copilot_summary": "Visitor navigated directly to the clearance apparel section, applied the 'Size: Large' filter successfully, and viewed the product page for the Merino Wool Pullover. After verifying sizing chart options, the user left the site without taking further action."
    }])#,
#     {
#         "session_id": "ms_clarity_98410419",
#         "start_time": "2026-10-18T01:45:22Z",
#         "end_time": "2026-10-18T01:48:10Z",
#         "duration_seconds": 168,
#         "device": "Desktop (macOS / Safari)",
#         "geo_location": "Berlin, Germany",
#         "pages_visited": ["/account/login", "/account/orders"],
#         "metrics": {"total_clicks": 6, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 40},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 78},
#         "copilot_summary": "Existing customer authenticated via login page. They checked the tracking updates of an existing order dispatched earlier in the week, downloaded an invoice PDF, and cleanly logged out without browsing new inventory."
#     },
#     {
#         "session_id": "ms_clarity_98410492",
#         "start_time": "2026-10-18T02:11:39Z",
#         "end_time": "2026-10-18T02:18:04Z",
#         "duration_seconds": 385,
#         "device": "Mobile (Android / Chrome)",
#         "geo_location": "Toronto, Canada",
#         "pages_visited": ["/", "/products/smart-home-hub", "/cart"],
#         "metrics": {"total_clicks": 18, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 90},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 130},
#         "copilot_summary": "User added the Smart Home Hub to their shopping cart. Proceeded to the /cart drawer, tested shipping cost calculation for Ontario, paused on the total summary for 90 seconds, and abandoned the session before triggering the checkout pipeline."
#     },
#     {
#         "session_id": "ms_clarity_98410531",
#         "start_time": "2026-10-18T02:34:18Z",
#         "end_time": "2026-10-18T02:36:20Z",
#         "duration_seconds": 122,
#         "device": "Tablet (iPadOS / Safari)",
#         "geo_location": "Sydney, Australia",
#         "pages_visited": ["/", "/pages/about-us", "/pages/contact"],
#         "metrics": {"total_clicks": 5, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 60},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 85},
#         "copilot_summary": "User landed on the homepage via a referral link, browsed the About Us background story, checked customer service operational hours on the Contact page, and navigated away."
#     },
#     {
#         "session_id": "ms_clarity_98410588",
#         "start_time": "2026-10-18T02:52:45Z",
#         "end_time": "2026-10-18T02:54:15Z",
#         "duration_seconds": 90,
#         "device": "Mobile (iOS / Safari)",
#         "geo_location": "New York, United States",
#         "pages_visited": ["/collections/footwear"],
#         "metrics": {"total_clicks": 7, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 65},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 105},
#         "copilot_summary": "Visitor casually scrolled the footwear grid. Applied a price filter (Low to High), examined thumbnail previews, and exited after determining items were outside their interest without clicking into a specific product page."
#     },
#     {
#         "session_id": "ms_clarity_98410612",
#         "start_time": "2026-10-18T03:15:02Z",
#         "end_time": "2026-10-18T03:19:40Z",
#         "duration_seconds": 278,
#         "device": "Desktop (Windows 10 / Firefox)",
#         "geo_location": "Austin, United States",
#         "pages_visited": ["/", "/search?q=mechanical+keyboard", "/products/rgb-mechanical-keyboard"],
#         "metrics": {"total_clicks": 16, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 95},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 90},
#         "copilot_summary": "User performed an on-site search for 'mechanical keyboard', selected the primary featured result, toggled through three colorway options via variant swatches, and clicked the 'Save to Wishlist' button before leaving."
#     },
#     {
#         "session_id": "ms_clarity_98410667",
#         "start_time": "2026-10-18T03:38:11Z",
#         "end_time": "2026-10-18T03:40:02Z",
#         "duration_seconds": 111,
#         "device": "Mobile (Android / Samsung Internet)",
#         "geo_location": "Singapore",
#         "pages_visited": ["/blogs/news/top-10-winter-essentials"],
#         "metrics": {"total_clicks": 3, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 100},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 115},
#         "copilot_summary": "Visitor arrived directly via an Instagram swipe-up link to a seasonal blog post. Read through the full editorial guide, clicked one outbound affiliate link, and did not navigate toward the shopping storefront."
#     },
#     {
#         "session_id": "ms_clarity_98410705",
#         "start_time": "2026-10-18T03:59:30Z",
#         "end_time": "2026-10-18T04:02:12Z",
#         "duration_seconds": 162,
#         "device": "Desktop (macOS / Chrome)",
#         "geo_location": "Dublin, Ireland",
#         "pages_visited": ["/", "/collections/all"],
#         "metrics": {"total_clicks": 11, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 50},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 70},
#         "copilot_summary": "User browsed the sitewide catalog using rapid horizontal pagination across two pages. Verified product availability tags without triggering any API errors or interface pauses."
#     },
#     {
#         "session_id": "ms_clarity_98410754",
#         "start_time": "2026-10-18T04:18:20Z",
#         "end_time": "2026-10-18T04:22:45Z",
#         "duration_seconds": 265,
#         "device": "Mobile (iOS / Safari)",
#         "geo_location": "Delhi, India",
#         "pages_visited": ["/", "/products/leather-messenger-bag", "/pages/shipping-policy"],
#         "metrics": {"total_clicks": 12, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 88},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 102},
#         "copilot_summary": "User inspected high-resolution product images for the leather messenger bag using image zoom. Consulted the return and shipping policy page to assess delivery timelines, then left the site."
#     },
#     {
#         "session_id": "ms_clarity_98410811",
#         "start_time": "2026-10-18T04:41:09Z",
#         "end_time": "2026-10-18T04:43:00Z",
#         "duration_seconds": 111,
#         "device": "Desktop (Windows 11 / Edge)",
#         "geo_location": "Paris, France",
#         "pages_visited": ["/pages/faq"],
#         "metrics": {"total_clicks": 8, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 75},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 82},
#         "copilot_summary": "Visitor searched the FAQ knowledge base regarding international warranty terms. Interacted with multiple collapsible FAQ accordions, all of which rendered promptly without script failures."
#     },
#     {
#         "session_id": "ms_clarity_98410860",
#         "start_time": "2026-10-18T05:02:50Z",
#         "end_time": "2026-10-18T05:08:15Z",
#         "duration_seconds": 325,
#         "device": "Mobile (Android / Chrome)",
#         "geo_location": "Bengaluru, India",
#         "pages_visited": ["/", "/collections/kitchenware", "/products/cast-iron-skillet", "/cart"],
#         "metrics": {"total_clicks": 21, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 92},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 120},
#         "copilot_summary": "User added a cast-iron skillet to their cart and attempted to apply a coupon code ('SAVE20'). The cart displayed a valid promo-code rejection toast ('Coupon expired'), after which the user emptied their cart and terminated the session."
#     },
#     {
#         "session_id": "ms_clarity_98410903",
#         "start_time": "2026-10-18T05:19:33Z",
#         "end_time": "2026-10-18T05:21:40Z",
#         "duration_seconds": 127,
#         "device": "Tablet (Android / Chrome)",
#         "geo_location": "Dubai, United Arab Emirates",
#         "pages_visited": ["/", "/collections/new-arrivals"],
#         "metrics": {"total_clicks": 6, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 55},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 95},
#         "copilot_summary": "Visitor viewed the newly launched catalog items, swiped through the primary carousel banner without issue, and left the page after skimming the top row of items."
#     },
#     {
#         "session_id": "ms_clarity_98410948",
#         "start_time": "2026-10-18T05:37:12Z",
#         "end_time": "2026-10-18T05:42:01Z",
#         "duration_seconds": 289,
#         "device": "Desktop (macOS / Chrome)",
#         "geo_location": "Amsterdam, Netherlands",
#         "pages_visited": ["/collections/office-furniture", "/products/ergonomic-desk-chair"],
#         "metrics": {"total_clicks": 15, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 80},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 88},
#         "copilot_summary": "User spent extensive time comparing dimensions and tilt tension specifications for an ergonomic office chair. They copied the product SKU to their clipboard and left the page."
#     },
#     {
#         "session_id": "ms_clarity_98411001",
#         "start_time": "2026-10-18T05:54:27Z",
#         "end_time": "2026-10-18T05:56:10Z",
#         "duration_seconds": 103,
#         "device": "Mobile (iOS / Safari)",
#         "geo_location": "Hyderabad, India",
#         "pages_visited": ["/", "/pages/store-locator"],
#         "metrics": {"total_clicks": 5, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 60},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 110},
#         "copilot_summary": "User opened the physical retail store locator, allowed geolocation permission, and viewed nearby offline retail partners before exiting."
#     },
#     {
#         "session_id": "ms_clarity_98411045",
#         "start_time": "2026-10-18T06:12:08Z",
#         "end_time": "2026-10-18T06:19:50Z",
#         "duration_seconds": 462,
#         "device": "Desktop (Windows 11 / Chrome)",
#         "geo_location": "Tokyo, Japan",
#         "pages_visited": ["/", "/products/ceramic-pour-over-set", "/cart", "/checkout"],
#         "metrics": {"total_clicks": 28, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 100},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 92},
#         "copilot_summary": "Visitor added a coffee maker set to their cart and proceeded to step 1 of Checkout (Customer Information). They filled in their name and shipping destination, reviewed tax calculations, but closed the tab when reaching the credit card entry step."
#     },
#     {
#         "session_id": "ms_clarity_98411090",
#         "start_time": "2026-10-18T06:28:44Z",
#         "end_time": "2026-10-18T06:31:05Z",
#         "duration_seconds": 141,
#         "device": "Mobile (Android / Chrome)",
#         "geo_location": "Chennai, India",
#         "pages_visited": ["/collections/footwear/sneakers", "/products/retro-runner-white"],
#         "metrics": {"total_clicks": 10, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 78},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 104},
#         "copilot_summary": "User selected a specific shoe model and toggled between sizes UK 8, UK 9, and UK 10. The UI rendered 'Out of Stock' for the desired size (UK 9), prompting the user to submit an email for restock notification."
#     },
#     {
#         "session_id": "ms_clarity_98411132",
#         "start_time": "2026-10-18T06:40:15Z",
#         "end_time": "2026-10-18T06:43:20Z",
#         "duration_seconds": 185,
#         "device": "Desktop (macOS / Safari)",
#         "geo_location": "San Francisco, United States",
#         "pages_visited": ["/policies/privacy-policy", "/policies/terms-of-service"],
#         "metrics": {"total_clicks": 4, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 82},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 76},
#         "copilot_summary": "User landed directly on policy documents via an external audit query. Read through sections concerning data retention and payment processing partners without visiting the storefront."
#     },
#     {
#         "session_id": "ms_clarity_98411178",
#         "start_time": "2026-10-18T06:49:50Z",
#         "end_time": "2026-10-18T06:52:10Z",
#         "duration_seconds": 140,
#         "device": "Mobile (iOS / Safari)",
#         "geo_location": "Chicago, United States",
#         "pages_visited": ["/", "/collections/clearance"],
#         "metrics": {"total_clicks": 8, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 70},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 99},
#         "copilot_summary": "User tapped a promotional push notification, navigated through the clearance catalog, sorted by newest additions, and scrolled through 24 items before exiting without clicking into any item."
#     },
#     {
#         "session_id": "ms_clarity_98411215",
#         "start_time": "2026-10-18T06:57:04Z",
#         "end_time": "2026-10-18T06:59:48Z",
#         "duration_seconds": 164,
#         "device": "Desktop (Windows 11 / Chrome)",
#         "geo_location": "Pune, India",
#         "pages_visited": ["/", "/pages/newsletter-signup", "/collections/all"],
#         "metrics": {"total_clicks": 13, "rage_clicks": 0, "dead_clicks": 0, "scroll_depth_pct": 65},
#         "technical_health": {"js_errors": 0, "http_status_exceptions": 0, "render_blocking_delay_ms": 86},
#         "copilot_summary": "Early morning visitor engaged with the footer newsletter form, completed the email submission successfully, received the confirmation modal, and briefly browsed the product catalog before leaving."
#     }
# ])

if __name__ == "__main__":
    mcp.run(transport = "stdio")