def pytest_configure(config):
    markers_list = ["search", "login"]
    for markers in markers_list:
        config.addinivalue_line(
            "markers", markers
        )
