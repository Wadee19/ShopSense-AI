# My learning journey — real try and error

This is my first complete machine learning portfolio project. I wanted to learn by doing, not by copying a perfect example.

## Try 1 — understand the question
I started with the UCI Online Shoppers Purchasing Intention dataset. The target is `Revenue`: a purchase happened or did not happen. It is **not** a money amount.

## Try 2 — look at the data
I checked the 12,330 sessions and the purchase share (15.47%). I learned that accuracy alone can be misleading when most sessions do not end in a purchase.

## Try 3 — avoid an easy but risky shortcut
I tested `PageValues` separately. It gave a much stronger result, but its timing and meaning may reveal information related to the purchase. I kept it out of my main model.

## Try 4 — compare models
I tried Logistic Regression and Random Forest settings. I used training data for grouped cross-validation and validation data to choose. Random Forest with 160 trees and minimum leaf size 5 won.

## Try 5 — a new feature did not help
I tried `AvgProductSeconds`. Validation Average Precision went from about **0.3801** to **0.3778**. I did not keep the feature. A new feature is not always a better feature.

## Try 6 — choose the threshold
I compared thresholds using validation F1 and chose **0.25**. Then I froze the model and threshold before testing.

## Try 7 — the final test
My test Average Precision was **0.3913**. Precision was **0.3541**, recall **0.4816**, and F1 **0.4081**.

## Try 8 — Colab did not match
The first Google Colab run worked but gave a different test AP: **0.3407**. We checked the data file, then the scikit-learn versions. Colab was on **1.6.1** while the original run used **1.8.0**. After installing **1.8.0**, restarting and rerunning, the split, threshold and metrics matched. The Colab run was executed by me, and its artifacts were checked separately.

## My lesson
I must check **data, versions, split, threshold and results**. I can learn from a failed experiment. I should say what really happened, not pretend that everything worked on the first try.

*The code and recorded outputs are in the notebook. AI helped with implementation and review.*
