# My results — simple English

The final model is a Random Forest. I chose a threshold of **0.25** using validation data.

| Metric | Test result | What it means |
|---|---:|---|
| Average Precision | 0.3913 | How well I rank sessions that end in a purchase |
| Precision | 0.3541 | About 35 out of 100 predicted purchases were real purchases |
| Recall | 0.4816 | I found about 48 out of 100 real purchases |
| F1 | 0.4081 | A balance of precision and recall |
| ROC-AUC | 0.7834 | Ranking quality across different thresholds |
| Accuracy | 0.7842 | Share of correct predictions overall |

## The confusion matrix
On the 1,761-session test set:
- **131** sessions: predicted purchase, and a purchase happened.
- **239** sessions: predicted purchase, but no purchase happened.
- **141** sessions: predicted no purchase, but a purchase happened.
- **1,250** sessions: predicted no purchase, and no purchase happened.

![Test confusion matrix](../outputs/test_confusion_matrix.svg)

## What the numbers do NOT say
The model is not guaranteed to work in a real shop. It does not predict spending amount. Its score is not guaranteed to be a calibrated probability. The test is on historical session data, not a live experiment.
