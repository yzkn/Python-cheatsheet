import pytest
import warnings


def api_v1():
    warnings.warn(UserWarning("deprecated: This API will be deprecated."))
    return 1


@pytest.mark.filterwarnings("ignore:deprecated")
def test_one():
    assert api_v1() == 1
