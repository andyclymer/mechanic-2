from urlreader import URLReader, USER_CACHE_PATH


PERSISTENT_CACHE_PATH = USER_CACHE_PATH.\
    URLByAppendingPathComponent_isDirectory_(
        'com.robofontmechanic.PersistentCache', True).relativePath()


# Two singletons for URLReaders with slightly different behavior.
# Both quote the URL path component by default and force connections 
# over HTTPS to comply with App Transport Security policy requirements.

# The default URLReader, uses standard HTTP caching policies.
DefaultURLReader = URLReader(force_https=True)

# An URLReader that caches more aggressively and tries to serve 
# responses from its own cache first before hitting the remote source.
CachingURLReader = URLReader(force_https=True, 
    use_cache=True, cache_location=PERSISTENT_CACHE_PATH)
