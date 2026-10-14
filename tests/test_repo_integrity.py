"""Fast checks of published artifacts; this does NOT retrain the model."""
import csv
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SHA = "a7e2714f884a221e95822830fe8e4400e9365d5e5af7c619f3fc6c9343254ad6"

class RepositoryIntegrityTests(unittest.TestCase):
    def test_dataset_rows_and_checksum(self):
        data = ROOT / "data" / "online_shoppers_intention.csv"
        self.assertEqual(hashlib.sha256(data.read_bytes()).hexdigest(), EXPECTED_SHA)
        with data.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            self.assertEqual(len(reader.fieldnames), 18)
            rows = list(reader)
        self.assertEqual(len(rows), 12330)
        self.assertEqual(sum(row["Revenue"].lower() == "true" for row in rows), 1908)

    def test_notebook_is_executed_without_recorded_errors(self):
        notebook = json.loads((ROOT / "notebooks" / "shopsense_ai.ipynb").read_text())
        code = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
        self.assertEqual(len(code), 39)
        self.assertTrue(all(cell.get("execution_count") is not None for cell in code))
        self.assertFalse(any(out.get("output_type") == "error"
                             for cell in code for out in cell.get("outputs", [])))

    def test_saved_metrics_are_consistent(self):
        result = json.loads((ROOT / "outputs" / "summary.json").read_text())
        self.assertEqual(result["selected_model"], "RF_leaf5")
        self.assertEqual(result["threshold"], 0.25)
        self.assertFalse(result["page_values_in_headline_model"])
        self.assertEqual([s["sessions"] for s in result["split"]], [8807, 1762, 1761])
        tp, fp, fn, tn = 131, 239, 141, 1250
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * precision * recall / (precision + recall)
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        for key, value in [("precision", precision), ("recall", recall),
                           ("F1", f1), ("accuracy", accuracy)]:
            self.assertAlmostEqual(result["test"][key], value, places=12)
        self.assertAlmostEqual(result["test"]["AP"], 0.39125534377307064, places=12)

    def test_chart_files_exist(self):
        for filename in ["test_confusion_matrix.svg", "permutation_importance.svg",
                         "purchase_rate_by_split.svg", "test_metrics.svg"]:
            self.assertTrue((ROOT / "outputs" / filename).is_file())

if __name__ == "__main__":
    unittest.main()
