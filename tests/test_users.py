# -*- coding:utf-8 -*-

"""Users representation tests."""

from fcc_scp.user import User


def test_instantiation():
    """Check that User instance has the particular properties."""
    bob = User('Bob', 42)
    assert bob.name == 'Bob'
    assert bob.age == 42


def test_introduction():
    """Check that user introduses herself properly."""
    alice = User('Alice', 21)
    intro = alice.get_introduction()
    assert alice.name in intro
    assert str(alice.age) in intro
