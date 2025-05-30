import pandas as pd

a = [{'asd': 'a'}]
df = pd.DataFrame(a)
df.to_csv('D:/Subject/Year 3/Do_an_2/jobs_data.csv', index=False, encoding='utf-8-sig')