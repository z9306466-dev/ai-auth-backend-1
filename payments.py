PACKAGES = {
    "50": {"coins": 50, "price": 1},
    "100": {"coins": 100, "price": 2},
    "1000": {"coins": 1000, "price": 20},
    "50000": {"coins": 50000, "price": 1000, "discount": 30},
}

def get_package(name):
    return PACKAGES.get(name)