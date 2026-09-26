def test_backend_app_import():
    import backend.app

    assert backend.app is not None


def test_backend_app_module():
    import backend.app

    assert hasattr(backend.app, "__file__")