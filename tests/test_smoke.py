from frost_td import hash_tag

def test_hash_tag_length():
    assert len(hash_tag("FROST/aux", b"")) == 32
