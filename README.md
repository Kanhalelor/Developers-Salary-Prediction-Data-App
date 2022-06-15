# Stackoverflow Developer's Salary Prediction ML Data App

![Credit: flex jobs](https://fjwp.s3.amazonaws.com/blog/wp-content/uploads/2021/02/18095635/Salary-Range.png)
---

Using Stackoverflow's anual developer survey data, we'll build a machine learning model to predict employeee salaries based on certain features in the dataset.


**Note**
The `csv file` cannot be uploaded to github because it is > the required 25MB.

Download it from stackflow:

```python
import requests, zipfile, io, os

url = "https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip"

file = requests.get(url)
zipf = zipfile.ZipFile(io.BytesIO(file.content))
expracted_data = zipf.extractall(os.mkdir('./survey-data'))
```

**Follow the steps in the `ipynb` for further reference.**
