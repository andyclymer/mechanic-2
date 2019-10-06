from urlreader import URLReader


# default shared URLReader, uses standard HTTP caching, quotes the 
# URL path component by default and forces connections over HTTPS 
# to comply with App Transport Security policy requirements
DefaultURLReader = URLReader(force_https=True)

# URLReader with an on-disk, persistent cache
CachingURLReader = URLReader(force_https=True, use_cache=True)
