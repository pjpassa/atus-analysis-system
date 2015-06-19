def average_minutes(data, activity_name):
    # print(data)
    activity_col = activity_name
    data = data[["weight", activity_col]]
    print(data)
    data = data.rename(columns={activity_col: "minutes"})
    data['weighted_minutes'] = data.weight * data.minutes
    return data.weighted_minutes.sum() / data.weight.sum()


def get_input(dataset):
    done = False
    avg = input("want the average? y/n")
    clean = input("Want your data cleaned?  We drop zeros and nan. y/n")
    columns = []
    if avg == "y":
        print("Automatically including weight and household because you want the average")
        columns.append('weight')
    for item in dataset.columns.tolist():
        print(item)
    while not done:
        print("Enter you column as appears above, type DONE when done, or CLEAR if you messup")
        column = input("What columns do you want?")
        if column == 'DONE':
            done = True
            break
        if column == 'CLEAR':
            columns = []
        columns.append(column)
        print(columns)
    return(avg, clean, columns)


def querys(datawork, query):
    return datawork[query]


def datasets(dataset, query=None):
    avg, clean, columns = get_input(dataset)
    # print(avg, clean, columns)
    data = dataset[columns]
    if query is not None:
        data = querys(data, query)
    data.describe()
    if avg == 'y':
        newdataframe = {}
        for item in data.columns.tolist():
            if item == "weight":
                pass
            else:
                # print(data.columns.tolist())
                newdataframe[item] = [average_minutes(data, item)]
        data = pd.DataFrame.from_dict(newdataframe, orient='columns', dtype=None)
    if clean == 'y':
        for item in data.columns.tolist():
            if item == "weight":
                pass
            else:
                data = data[data[item] > 0]
                # print(data)
        return data
    return data
