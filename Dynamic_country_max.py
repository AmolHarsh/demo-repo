import pandas as pd
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
DF = pd.read_csv(url)
DF = DF[['continent', 'location', 'date', 'new_cases']]
DF = DF[DF['continent'] == "Europe"]
DF = DF.fillna(value=0)
DF = DF.reset_index()
DF = DF.filter(items=['location', 'date', 'new_cases'])
group = DF.groupby('location')
DF['date'] = pd.to_datetime(DF['date'])
time_start = DF['date'].min()
time_frame = '120 days'
time_frame_addition = "1 days"
time_end = time_start + pd.Timedelta('120 days')
Cumulative_country = {}
first = 1
frames = []
Dict = {}
while time_start < DF['date'].max():
    if time_end > DF['date'].max():
        time_end = DF['date'].max()
    time_frame_data = DF[DF['date'].between(time_start, time_end)]
    group = time_frame_data.groupby('location')
    temp = None
    Final = None
    count = 1
    print(DF)

    for country, data_frame in group:
        if count == 1:
            Final = data_frame[['date', 'new_cases']]
            Final.reset_index()
            max_new_cases = Final['new_cases'].max(axis=0)
            DFtemp = (Final['new_cases'].values)/max_new_cases
            Final = Final.rename(columns={'new_cases': country})
            Final[country] = DFtemp
            count += 1
            continue
        curr_db = data_frame[['date', 'new_cases']]
        max_new_cases = curr_db['new_cases'].max(axis=0)
        print(max_new_cases)
        DFtemp = (curr_db['new_cases'].values)/max_new_cases
        curr_db = data_frame.rename(columns={'new_cases': country})
        curr_db[country] = DFtemp
        Final = pd.merge(curr_db, Final, on='date')
        Final.set_index('date')
    time_start = time_start + pd.Timedelta('1 days')
    time_end = time_end + pd.Timedelta('1 days')
    Final.drop(['location_x', 'location_y'], axis=1, inplace=True)
    frames.append(Final)
Concatenated = pd.concat(frames)
group_date = Concatenated.groupby('date')
print(group_date.head(1))
List_Means = []
count = 1
for date, data_frame in group_date:
    data_frame.set_index('date')
    if count == 1:
        Means = data_frame.mean(axis=0)
        Miu = Means.to_frame()
        Miu.reset_index(inplace=True)
        print(Miu)
        print((Miu.shape)[1])
        Miu.columns = ['Country', 'cases']
        Miu['cases'].fillna(0, inplace=True)
        print(type(Means))
        count += 1
        continue
    Means = data_frame.mean(axis=0)
    Temp = Means.to_frame()
    Temp.reset_index(inplace=True)
    Temp.columns = ['Country', 'cases']
    Temp['cases'].fillna(0, inplace=True)
    Miu = pd.merge(Temp, Miu, on='Country')
Miu = Miu.transpose()
Miu.reset_index(inplace=True)
Miu.drop(['index'], inplace=True, axis=1)
headers = Miu.iloc[0]
Miu_correct_head = pd.DataFrame(Miu.values[1:], columns=headers)
# headers = df.iloc[0]
# new_df  = pd.DataFrame(df.values[1:], columns=headers)
print(Miu_correct_head)
Miu_correct_head.plot(kind="line", y=[
                      "Hungary", "Germany"], color=["blue", "red"])
plt.show()
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))
#     for coloumn in data_frame:
#         if country == 'date':
#             continue
#         Dict[coloumn].append(coloumn.mean(axis=1))
# print(Dict)
# if first == 1:
#     Superfinal = Final.copy(deep=True)
#     first += 1
#     continue
# Superfinal = Superfinal.copy(deep=True) + Final.copy(deep=True)
# print(Superfinal)
# Superfinal.plot(x="date")
# plt.show()
# print(Final)
# Final['date'] = pd.to_datetime(Final['date'])
# # Final.plot()
# # plt.title('new_cases')
# # plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2))
# # plt.show()
# # Final["Ukraine"] = Final["Ukraine"]/100
# # print(Final["Ukraine"])
# # print(Final.loc[:, "Vatican"])
