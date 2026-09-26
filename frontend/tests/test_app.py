def test_frontend_app_import():
    import frontend.app

    assert frontend.app is not None


def test_frontend_app_module():
    import frontend.app

    assert hasattr(frontend.app, "__file__")