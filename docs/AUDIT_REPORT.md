# ShopSense AI — independent repository audit (2026-10-14)

## Scope and evidence
Reviewed the public GitHub repository, its executed notebook, data file, published output tables, documentation, and charts. Independently re-executed the downloaded **user-executed Colab notebook** in a clean working folder containing only the repository dataset and provenance file, with Python 3.13.5, scikit-learn 1.8.0, pandas 2.2.3 and numpy 2.3.5. All **39 code cells executed successfully in 27.5 seconds** on the audit runtime. No cell error outputs.

## Results confirmed
- Source dataset: **12,330 sessions**, **18 columns**, **1,908 purchases**; packaged SHA-256 `a7e2714f884a221e95822830fe8e4400e9365d5e5af7c619f3fc6c9343254ad6`.
- Split: train **8,807**, validation **1,762**, test **1,761**.
- Main model: **RF_leaf5**, threshold **0.25**, `PageValues` excluded.
- Test AP **0.39125534377307064**; precision **0.35405405405405405**, recall **0.48161764705882354**, F1 **0.40809968847352024**.
- Audit rerun matched **all six** saved validation and test metrics exactly (AP, ROC-AUC, precision, recall, F1, accuracy). All candidate validation AP values also matched. One training CV value varied by less than 0.00000021; that small difference does not change candidate ranking.
- The saved-model `joblib` round-trip assertion passed as part of the notebook rerun.

## Methodology
- **Pass:** Target is correctly described as binary purchase outcome, not revenue amount.
- **Pass:** `PageValues` is excluded from the primary model and evaluated only as a sensitivity analysis.
- **Pass:** Identical primary predictor vectors are grouped before splitting, reducing exact-duplicate leakage risk.
- **Pass:** Preprocessing is fitted within pipelines; CV is confined to training data; model and threshold selection use validation data; final test evaluation is downstream.
- **Caution:** The dataset is historical and lacks a real deployment-time feature contract; this is not validated for early-session predictions.
- **Caution:** Reproducibility depends on scikit-learn 1.8.0; a different release changed the group split in an observed Colab run. Future work could save immutable split row IDs.
- **Caution:** The six model candidates and threshold grid are deliberately small; there is no production-grade hyperparameter search or uncertainty interval. These are limitations, not hidden failures.
- **Caution:** The example prediction uses a held-out historical session, not a live customer input.

## Publication findings and fixes
1. **Restored** the original left-to-right Mermaid workflow diagram at the user's request.
2. **Clarified** that the four GitHub SVG figures were redrawn from verified run metrics; the notebook itself holds the original generated plots.
3. **Fixed** the GitHub `outputs/summary.json` to match the complete Colab summary schema, rather than a manually shortened version.
4. **Added** the complete real threshold sweep and a lightweight standard-library integrity test.
5. **Corrected** the last CV numbers in published experiment tables to match the actual executed notebook.

## Remaining publication gaps
- The repository does not commit the generated `models/shopsense_pipeline.joblib` binary or original PNG chart exports. The notebook regenerates both; the user's downloadable complete archive includes them.
- The GitHub **About / Topics / Pin** metadata was empty in the observed screenshots. The connected repository file API can write repository files but does not expose a repository-metadata update operation, so those account-level settings are not changed here.
- The fast integrity tests check published files; they **do not** independently retrain the ML model. The full notebook rerun was separately completed during this audit.

## How to check quickly
Run `python -m unittest discover -s tests -v` from the repository root. To fully reproduce the model, run the notebook with the pinned scikit-learn version.

**Verdict:** Suitable as an honest first professional learning portfolio project. The published model is **not** validated as a production purchase prediction service.
