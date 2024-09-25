# SE4AI_group_6

\
**Analysis:**

-   The *ranks()* function calculates the percentage distribution of ranks (0, 1, 2, etc.) for different strategies. The purpose is to count how often each strategy received a certain rank and represent it as a percentage over the total number of records.
-   The *evaluations()* function calculates the mean (mu) and standard deviation (sd) of the evaluation scores (Chebyshev distances) for each strategy at each rank (EVALS).
-   The *improvement()* function calculates the Delta for each strategy by comparing how much better or worse a strategy performs compared to the baseline (mentioned as 'asIs').

-   To sum up, **RANKS** show the percentage distribution of rank assignment for each strategy, **EVALS** show the average and standard deviation of performance for each strategy at different ranks and **DELTA** show how much each strategy improves compared to the baseline performance 'asIs'.

< br / >   
![image](https://github.com/user-attachments/assets/0fb966a3-e553-41f8-aed7-dedc94d8b1bb)

-   Here, RANKS shows that the **smart strategy** in high dimensions performed significantly **better** than the dumb strategy or the asIs baseline, with a majority of its results at rank 0. The ***dumb strategy*** in both low and high dimensions performed ***worse*** overall, receiving higher ranks more frequently.

![image](https://github.com/user-attachments/assets/8b0e6264-c1b9-48a3-9f05-27f47e676e93)

-   The smart strategy generally has lower evaluation scores (which is better since Chebyshev distances measure dissimilarity) than the dumb strategy, especially in high dimensions.
For Rank 0 in high dimensions, the dumb strategy actually performs slightly better than the smart strategy, because a lower EVAL value (28) represents better performance than a higher value (32). Even though dumb strategy performed better than smart strategy at Rank 0 in terms of raw EVAL scores, smart strategy shows a higher improvement over the baseline. This means the **smart strategy shows better relative improvement**, but in absolute terms for Rank 0, ***dumb strategy*** still has the edge based on EVAL scores.

![image](https://github.com/user-attachments/assets/ddab795b-b649-40ca-9513-a4c6cae2e177)

-   Both smart and dumb strategies improve over the baseline, but the smart strategy tends to perform more consistently in high-dimensional data.
smart/dim=high_dim for Rank 0 has a 71% improvement, while dumb/dim=high_dim has 65%. For other ranks and dimensions, **smart strategy** seems to perform **more consistently** in providing improvements over the baseline.

**Summary of Analysis(Smart vs Dumb):**
-   Both strategies improve over the baseline (asIs), but the smart strategy tends to show more significant improvement in high-dimensional data, with a delta of 71%.
The dumb strategy also shows improvement but is less consistent, especially in low-dimensional data.<br />
-   Statistically, the smart strategy consistently (evident due to lower standard deviation) outperforms the dumb strategy (shows more variability in results) in both high and low-dimensional data, receiving lower ranks and better evaluation scores, indicating that it's more reliable particularly in high-dimensional scenarios.

 
**Final conclusion:**
-   Since we observed that the dumb strategy (random guessing) performed comparably to the smart strategy in low-dimensional data (with similar or even slightly better EVAL scores in some cases), we confirm the JJR1 hypothesis that nothing works better than 50 random guesses for low-dimensional problems.<br />
However, for high-dimensional data, we observed that while the dumb strategy performed well in absolute terms at Rank 0, the smart strategy showed significantly greater improvement over the baseline (as indicated by higher DELTA values). This suggests that random guessing is less effective in higher dimensions, and we confirm the JJR2 hypothesis that random guessing is indeed suboptimal for high-dimensional problems.


Test cases 
![image](https://github.com/user-attachments/assets/4e51f72e-3c92-4caf-949e-6457dd691bb7)

- Test Case #1 - Test if the dumb list is the right length (i.e. N). They should be 20. 

- Test Case #2 - Test if the smart list is the right length (i.e. N). They should be 20. 

- Test Case #3 - Checks if the first value given by Chebyshev is really the best. Did this for a small .csv file given in data/test_data/test_extend_file.csv.

- Test Case #4 - Test if we run the experimental treatment 20 times which is the length of the dumb and smart strategy.
  
- Test Case #5 - Test if the shuffle() method is really changin the order the data. Needed to use .copy() otherwise both DATAs would change. 
