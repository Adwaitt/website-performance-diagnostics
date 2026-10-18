import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fetch_summaries")

@mcp.tool()
async def fetch_logs()->str:
    return json.dumps([
    {
        "stream": {
            "app": "ecommerce-ingress",
            "environment": "production",
            "namespace": "storefront",
            "service": "nginx-ingress"
        },
        "values": [
            "1729213694000000000",
            '{"timestamp":"2026-10-18T01:08:14.102Z","trace_id":"trace_8410291_01","client_ip":"82.165.197.1","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.038,"upstream_response_time":"0.036","upstream_status":"200","http_referrer":"https://www.google.com/","http_user_agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1","country":"GB","clarity_session_id":"ms_clarity_98410291","ga_session_id":"1729213694"}'
        ]
    },
    {
        "stream": {
            "app": "ecommerce-ingress",
            "environment": "production",
            "namespace": "storefront",
            "service": "nginx-ingress"
        },
        "values": [
            "1729214585000000000",
            '{"timestamp":"2026-10-18T01:23:05.412Z","trace_id":"trace_8410344_02","client_ip":"103.21.124.55","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.032,"upstream_response_time":"0.030","upstream_status":"200","http_referrer":"-","http_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36","country":"IN","clarity_session_id":"ms_clarity_98410344","ga_session_id":"1729214585"}'
        ]
    }])#,
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729215922000000000",
#             '{"timestamp":"2026-10-18T01:45:22.018Z","trace_id":"trace_8410419_03","client_ip":"185.220.101.5","remote_user":"-","request_method":"GET","request_uri":"/account/login","status":200,"body_bytes_sent":18420,"request_time":0.028,"upstream_response_time":"0.026","upstream_status":"200","http_referrer":"https://mail.google.com/","http_user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15","country":"DE","clarity_session_id":"ms_clarity_98410419","ga_session_id":"1729215922"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729217499000000000",
#             '{"timestamp":"2026-10-18T02:11:39.894Z","trace_id":"trace_8410492_04","client_ip":"142.214.22.80","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.041,"upstream_response_time":"0.039","upstream_status":"200","http_referrer":"https://www.googleadservices.com/","http_user_agent":"Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.58 Mobile Safari/537.36","country":"CA","clarity_session_id":"ms_clarity_98410492","ga_session_id":"1729217499"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729218858000000000",
#             '{"timestamp":"2026-10-18T02:34:18.150Z","trace_id":"trace_8410531_05","client_ip":"139.130.4.5","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.035,"upstream_response_time":"0.033","upstream_status":"200","http_referrer":"https://partner-portal.com/","http_user_agent":"Mozilla/5.0 (iPad; CPU OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1","country":"AU","clarity_session_id":"ms_clarity_98410531","ga_session_id":"1729218858"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729219965000000000",
#             '{"timestamp":"2026-10-18T02:52:45.331Z","trace_id":"trace_8410588_06","client_ip":"69.162.124.226","remote_user":"-","request_method":"GET","request_uri":"/collections/footwear","status":200,"body_bytes_sent":32100,"request_time":0.045,"upstream_response_time":"0.043","upstream_status":"200","http_referrer":"https://www.pinterest.com/","http_user_agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1","country":"US","clarity_session_id":"ms_clarity_98410588","ga_session_id":"1729219965"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729221302000000000",
#             '{"timestamp":"2026-10-18T03:15:02.503Z","trace_id":"trace_8410612_07","client_ip":"23.111.154.12","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.031,"upstream_response_time":"0.029","upstream_status":"200","http_referrer":"-","http_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0","country":"US","clarity_session_id":"ms_clarity_98410612","ga_session_id":"1729221302"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729222691000000000",
#             '{"timestamp":"2026-10-18T03:38:11.782Z","trace_id":"trace_8410667_08","client_ip":"118.200.24.110","remote_user":"-","request_method":"GET","request_uri":"/blogs/news/top-10-winter-essentials","status":200,"body_bytes_sent":41200,"request_time":0.040,"upstream_response_time":"0.038","upstream_status":"200","http_referrer":"https://l.instagram.com/","http_user_agent":"Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0.6167.101 Mobile Safari/537.36","country":"SG","clarity_session_id":"ms_clarity_98410667","ga_session_id":"1729222691"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729223970000000000",
#             '{"timestamp":"2026-10-18T03:59:30.220Z","trace_id":"trace_8410705_09","client_ip":"185.89.219.1","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.029,"upstream_response_time":"0.027","upstream_status":"200","http_referrer":"https://www.google.ie/","http_user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36","country":"IE","clarity_session_id":"ms_clarity_98410705","ga_session_id":"1729223970"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729225100000000000",
#             '{"timestamp":"2026-10-18T04:18:20.941Z","trace_id":"trace_8410754_10","client_ip":"122.161.49.20","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.034,"upstream_response_time":"0.032","upstream_status":"200","http_referrer":"-","http_user_agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1","country":"IN","clarity_session_id":"ms_clarity_98410754","ga_session_id":"1729225100"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729226469000000000",
#             '{"timestamp":"2026-10-18T04:41:09.610Z","trace_id":"trace_8410811_11","client_ip":"51.159.21.3","remote_user":"-","request_method":"GET","request_uri":"/pages/faq","status":200,"body_bytes_sent":19800,"request_time":0.026,"upstream_response_time":"0.024","upstream_status":"200","http_referrer":"https://www.google.fr/","http_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","country":"FR","clarity_session_id":"ms_clarity_98410811","ga_session_id":"1729226469"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729227770000000000",
#             '{"timestamp":"2026-10-18T05:02:50.051Z","trace_id":"trace_8410860_12","client_ip":"106.51.78.140","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.037,"upstream_response_time":"0.035","upstream_status":"200","http_referrer":"https://l.facebook.com/","http_user_agent":"Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.58 Mobile Safari/537.36","country":"IN","clarity_session_id":"ms_clarity_98410860","ga_session_id":"1729227770"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729228773000000000",
#             '{"timestamp":"2026-10-18T05:19:33.472Z","trace_id":"trace_8410903_13","client_ip":"94.200.41.9","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.033,"upstream_response_time":"0.031","upstream_status":"200","http_referrer":"https://www.google.ae/","http_user_agent":"Mozilla/5.0 (Linux; Android 14; SM-X910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.58 Safari/537.36","country":"AE","clarity_session_id":"ms_clarity_98410903","ga_session_id":"1729228773"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729229832000000000",
#             '{"timestamp":"2026-10-18T05:37:12.880Z","trace_id":"trace_8410948_14","client_ip":"145.131.7.90","remote_user":"-","request_method":"GET","request_uri":"/collections/office-furniture","status":200,"body_bytes_sent":34900,"request_time":0.042,"upstream_response_time":"0.040","upstream_status":"200","http_referrer":"-","http_user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36","country":"NL","clarity_session_id":"ms_clarity_98410948","ga_session_id":"1729229832"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729230867000000000",
#             '{"timestamp":"2026-10-18T05:54:27.112Z","trace_id":"trace_8411001_15","client_ip":"117.216.32.18","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.036,"upstream_response_time":"0.034","upstream_status":"200","http_referrer":"https://www.google.co.in/","http_user_agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1","country":"IN","clarity_session_id":"ms_clarity_98411001","ga_session_id":"1729230867"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729231928000000000",
#             '{"timestamp":"2026-10-18T06:12:08.390Z","trace_id":"trace_8411045_16","client_ip":"133.242.18.77","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.039,"upstream_response_time":"0.037","upstream_status":"200","http_referrer":"https://newsletter.organization.com/","http_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36","country":"JP","clarity_session_id":"ms_clarity_98411045","ga_session_id":"1729231928"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729232924000000000",
#             '{"timestamp":"2026-10-18T06:28:44.755Z","trace_id":"trace_8411090_17","client_ip":"49.207.200.12","remote_user":"-","request_method":"GET","request_uri":"/collections/footwear/sneakers","status":200,"body_bytes_sent":29800,"request_time":0.038,"upstream_response_time":"0.035","upstream_status":"200","http_referrer":"https://www.google.co.in/","http_user_agent":"Mozilla/5.0 (Linux; Android 14; SM-M346B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.58 Mobile Safari/537.36","country":"IN","clarity_session_id":"ms_clarity_98411090","ga_session_id":"1729232924"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729233615000000000",
#             '{"timestamp":"2026-10-18T06:40:15.620Z","trace_id":"trace_8411132_18","client_ip":"198.51.100.84","remote_user":"-","request_method":"GET","request_uri":"/policies/privacy-policy","status":200,"body_bytes_sent":16250,"request_time":0.024,"upstream_response_time":"0.022","upstream_status":"200","http_referrer":"https://audit.compliance.org/","http_user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15","country":"US","clarity_session_id":"ms_clarity_98411132","ga_session_id":"1729233615"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729234190000000000",
#             '{"timestamp":"2026-10-18T06:49:50.198Z","trace_id":"trace_8411178_19","client_ip":"67.180.12.9","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.033,"upstream_response_time":"0.031","upstream_status":"200","http_referrer":"android-app://com.storefront.app/","http_user_agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1","country":"US","clarity_session_id":"ms_clarity_98411178","ga_session_id":"1729234190"}'
#         ]
#     },
#     {
#         "stream": {
#             "app": "ecommerce-ingress",
#             "environment": "production",
#             "namespace": "storefront",
#             "service": "nginx-ingress"
#         },
#         "values": [
#             "1729234624000000000",
#             '{"timestamp":"2026-10-18T06:57:04.430Z","trace_id":"trace_8411215_20","client_ip":"115.112.88.5","remote_user":"-","request_method":"GET","request_uri":"/","status":200,"body_bytes_sent":24580,"request_time":0.030,"upstream_response_time":"0.028","upstream_status":"200","http_referrer":"-","http_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36","country":"IN","clarity_session_id":"ms_clarity_98411215","ga_session_id":"1729234624"}'
#         ]
#     }
# ])

if __name__ == "__main__":
    mcp.run(transport = "stdio")