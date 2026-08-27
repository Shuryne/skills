import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "shuryne-skills"


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text())


class PluginVersionTest(unittest.TestCase):
    def test_plugin_versions_match(self) -> None:
        marketplace = load_json(".claude-plugin/marketplace.json")
        marketplace_plugin = next(
            plugin for plugin in marketplace["plugins"] if plugin["name"] == PLUGIN_NAME
        )
        versions = {
            "Codex manifest": load_json(".codex-plugin/plugin.json")["version"],
            "Claude manifest": load_json(".claude-plugin/plugin.json")["version"],
            "Claude marketplace": marketplace_plugin["version"],
        }

        self.assertEqual(
            len(set(versions.values())),
            1,
            f"Plugin versions must match: {versions}",
        )


if __name__ == "__main__":
    unittest.main()
