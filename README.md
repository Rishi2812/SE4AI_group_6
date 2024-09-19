# SE4AI_group_6
To run the extension of comparing smart vs dumb strategy put all files under ezr directory and Run \
```python extend_smartVSdumb.py low|high``` \
\
**Conclusion:**

-   The **smart strategy performs better than dumb strategy** in most datasets. It outperforms the dumb strategy in 9 out of 15  low dimension (xcols<=6) datasets.

1.  For sorted Chebyshev distances, a lower median indicates better algorithm performance, as it means the algorithm is producing  more shorter distances between the rows and goals.

2.  For e.g ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeyPSiBuhy_32ObKnrw05-ZZDw8dTAc6Bc3-P0TRhn965P2UbjMeVjV-HESkVeNqLzz5Fd6sOWEQH2QOqfiQpg4R8on2Diwn4HQyWnoDDdKSl1dQw_ATEPnLvUt5_3quwqyouqI3e42hx6u1Tb3ftl4SLpY?key=NrRNAj4z1NT8uDWfF8crnQ)

        Smart medians : 0.32,0.25,0.25,0.25

        Dumb medians : 0.41,0.37,0.37,0.39

Here, smart medians are consistently lower than dumb medians .Hence showing smart   strategy produces more shorter chebyshev distances.

-   **Smart Strategy also outperforms dumb strategy in high** dimensionality datasets

-   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd-2z7bx5xLN3Vqy6Ek9djot3VsI2hRfxO5mxehnckrUxHI3sQB2Tya91TSbFXHWT-hNducZsZs6UbxIMfwZ__fhXLgBL4dB-N3abaD-7lf2jjHoc9HK5Eu5tP3Rl7-onVT4vqY4mDc0mS0Ui62wHScEEzn?key=NrRNAj4z1NT8uDWfF8crnQ)

-   The Smart Strategy medians are lower than dumb strategy ones in most of the datasets, as the chebyshev distances are sorted of these strategies . The lower median would indicate more number of shorter distances .
