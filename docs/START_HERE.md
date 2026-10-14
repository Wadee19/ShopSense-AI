# Start here — my simple ShopSense AI guide

I built a small AI project to answer one question: **Will an online shopping session end with a purchase?**

## What is inside?
- **Data:** a table with 12,330 shopping sessions.
- **Notebook:** the code and my explanations in one file.
- **Model:** a program that learns patterns from old sessions.
- **Charts:** pictures that help me understand the data and the result.

## Run it in Google Colab
1. Open [Google Colab](https://colab.research.google.com/).
2. Upload `notebooks/shopsense_ai.ipynb` from this repository.
3. Run the first setup cell. It installs the correct scikit-learn version.
4. If Colab asks for a restart, restart the session and run from the top.
5. Run the notebook cells in order. The notebook can download the public UCI data.
6. Look at the tables and charts. Do not skip the final test.

## Easy words
- **Feature:** one input, like the number of product pages viewed.
- **Label:** the answer I want to predict, called `Revenue`.
- **Train:** let the model learn.
- **Validation:** choose between models without touching the final test.
- **Test:** check my final choice on unseen sessions.
- **Threshold:** the score where I say "purchase".

## What should I change first?
Change one model setting and rerun. Write down the new validation result. Do **not** keep choosing changes based on the final test.

Read [my learning journey](LEARNING_JOURNEY.md) next.
