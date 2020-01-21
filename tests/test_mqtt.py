import pytest
from joyit.mqtt import join_topics


def test_join_topics():
    with pytest.raises(ValueError):
        join_topics()
    assert join_topics("parent") == "parent"
    assert join_topics("parent", "child") == "parent/child"
    assert join_topics("parent", "child1", "child2") == "parent/child1/child2"

