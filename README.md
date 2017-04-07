# Best answer prediction for Yahoo! answers

* **main.py**: The program to preprocess the data and segregate the categories of questions used in analysis. **Dataset** - *Webscope_L4.tgz*
* **longest.py**: A Python program to fetch the longest answer resulting in the longest answer as the best answer.
* **cosine.py**: A Python program to find the cosine similarity between the (question & the best answer) and (question & all answers). The answer with the highest cosine distance is considered as the best answer.
* **jaccard.py**: A Python program to find the Jaccard similarity between the (question & the best answer) and (question & all answers). The answer with the highest Jaccard Index is considered as the best answer.(Jaccard index is the intersection of the two sets/ Union of the two sets)
