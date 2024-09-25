# SE4AI_group_6

\
**Conclusion:**

-   The **smart strategy performs better than dumb strategy** in most datasets. 


-   **Smart Strategy also outperforms dumb strategy in high** dimensionality datasets

-  
-   The Smart Strategy medians are lower than dumb strategy ones in most of the datasets, as the chebyshev distances are sorted of these strategies . The lower median would indicate more number of shorter distances .
-   Therefore, based on the above observation as evidences, we confirm that the hypothesis JJR1 doesn't hold true. JJR2, on the other hand, is valid and contradicts JJR1 by providing results showing that the smart strategy works well for both higher and lower dimensionality datasets.


Test cases 
![image](https://github.com/user-attachments/assets/4e51f72e-3c92-4caf-949e-6457dd691bb7)

- Test Case #1 - Test if the dumb list is the right length (i.e. N). They should be 20. 

- Test Case #2 - Test if the smart list is the right length (i.e. N). They should be 20. 

- Test Case #3 - Checks if the first value given by Chebyshev is really the best. Did this for a small .csv file given in data/test_data/test_extend_file.csv.

- Test Case #4 - Test if we run the experimental treatment 20 times which is the length of the dumb and smart strategy.
  
- Test Case #5 - Test if the shuffle() method is really changin the order the data. Needed to use .copy() otherwise both DATAs would change. 
