import tempfile
import unittest
from pathlib import Path

import cividoc


class NavigationTests(unittest.TestCase):
    def test_split_replaces_base_and_preserves_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            (docs / "survey").mkdir()
            (docs / "survey/everyday-tasks-part1.md").write_text("# First\n", encoding="utf-8")
            (docs / "survey/everyday-tasks-part2.md").write_text("# Second\n", encoding="utf-8")
            nav = [{"Survey": [{"Everyday tasks": "survey/everyday-tasks.md"}]}]
            result = cividoc.transform_nav(nav, docs)
            self.assertEqual(result, [{"Survey": [
                {"Everyday tasks": "survey/everyday-tasks-part1.md"},
                {"Second": "survey/everyday-tasks-part2.md"},
            ]}])

    def test_missing_titled_page_is_removed(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = cividoc.transform_nav([{"Missing": "missing.md"}], Path(tmp))
            self.assertEqual(result, [])

    def test_multi_key_items_are_split(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            (docs / "a.md").write_text("# A\n", encoding="utf-8")
            (docs / "b.md").write_text("# B\n", encoding="utf-8")
            result = cividoc.transform_nav([{"A": "a.md", "B": "b.md"}], docs)
            self.assertEqual(result, [{"A": "a.md"}, {"B": "b.md"}])


if __name__ == "__main__":
    unittest.main()
