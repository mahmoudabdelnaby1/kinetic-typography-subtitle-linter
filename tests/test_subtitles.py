import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from subtitle_linter import lint_srt

class TestSub(unittest.TestCase):
    def test_lint(self):
        bad = Path(__file__).resolve().parent.parent / "examples" / "bad_subtitles.srt"
        res = lint_srt(str(bad))
        self.assertEqual(res["status"], "FAIL")

if __name__ == "__main__":
    unittest.main()
