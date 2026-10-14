# Model card — ShopSense AI

**Purpose:** Predict the binary outcome `Revenue` for a historical online shopping session.

**Data:** UCI Online Shoppers Purchasing Intention Dataset, 12,330 rows, 18 original columns, 1,908 purchases.

**Main model:** Random Forest, 160 trees, minimum leaf size 5. Decision threshold 0.25.

**Inputs:** Session browsing summary fields available in the source data, excluding `PageValues`. Categorical fields are one-hot encoded in the fitted preprocessing pipeline.

**Evaluation:** Duplicate-aware, group-safe stratified split: train 8,807, validation 1,762, test 1,761. Training-only grouped cross-validation and validation model selection. Test Average Precision 0.3913, F1 0.4081.

**Important limitations:** The data is historical. Some session features may only be known after enough browsing has happened. This is not validated as an early-session or real-time predictor. Scores are not calibrated purchase probabilities. No causal or commercial uplift claim is made. There is no production monitoring, drift testing or temporal holdout.

**Reproducibility:** Use scikit-learn 1.8.0; other versions changed the grouped split in observed Colab testing. Run the notebook to regenerate the trained pipeline.

**Responsible use:** Learning and demonstration only. Do not use this model to make consequential decisions about people.
