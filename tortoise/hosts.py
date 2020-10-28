from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'www', 'websitedata.urls', name='www'),
    host(r'api', 'tortoise_api.urls', name='api'),
    host(r'staff', 'tortoise.urls', name='staff'),
    host(r'dashboard', 'admin_dashboard.urls', name='dashboard'),
)
