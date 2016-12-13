from tornado.httpclient import AsyncHTTPClient
try:
  import pycurl
  AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
except ImportError:
  pycurl = None

from .zhihu import ZhihuZhuanlanHandler
from .zhihu_stream import ZhihuStream
