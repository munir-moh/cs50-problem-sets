from um import count

def test_basic():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_sentence():
    assert count("Hello, um, world") == 1
    assert count("Um, um... UM!") == 3

def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0

def test_spacing():
    assert count("um um um") == 3
    assert count(" um  um ") == 2
    assert count("um?") == 1
