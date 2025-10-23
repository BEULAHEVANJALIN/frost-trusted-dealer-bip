import json
from pathlib import Path

def test_vectors_json_loadable():
    p = Path(__file__).parent / "vectors" / "v1" / "frost_td_vectors.json"
    j = json.loads(p.read_text())
    assert j.get("name") == "frost-td-vectors"
    assert j.get("version") in ("1", 1)
    assert isinstance(j.get("cases"), list)
