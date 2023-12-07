import pandas

balance_df = pandas.read_csv('./data/SaldoITEM.csv')
movement_df = pandas.read_csv('./data/MovtoITEM.csv')
item_df_list: list[pandas.DataFrame] = []
movement_df.groupby('item').apply(lambda df: item_df_list.append(df))

result_df = pandas.DataFrame(
    columns=[
        'item', 
        'data_lancamento', 
        'qtd_entrada', 
        'valor_entrada', 
        'qtd_saida', 
        'valor_saida', 
        'qtd_inicio', 
        'valor_inicio', 
        'qtd_final', 
        'valor_final'
    ]
)

for item_df in item_df_list:
    code = item_df.iloc[0]['item']
    balance_line = balance_df.loc[balance_df['item'] == code]

    init_quantity = balance_line.iloc[0]['qtd_inicio']
    init_value = balance_line.iloc[0]['valor_inicio']


    date_df_list: list[pandas.DataFrame] = []
    item_df.sort_values('data_lancamento').groupby('data_lancamento').apply(lambda df: date_df_list.append(df))
    
    for date_df in date_df_list:
        timestamp = date_df.iloc[0]['data_lancamento']
        entry_quantity = 0
        leave_quantity = 0

        entry_value = 0
        leave_value = 0
        for movement in date_df.values.tolist():
            if movement[1] == 'Ent':
                entry_quantity += movement[3]
                entry_value += movement[4]
            else:
                leave_quantity += movement[3]
                leave_value += movement[4]
          
          
        end_quantity = init_quantity + entry_quantity - leave_quantity
        end_value = init_value + entry_value - leave_value
        
        result = [code, timestamp, entry_quantity, entry_value, leave_quantity, leave_value, init_quantity, init_value, end_quantity, end_value]

        result_df.loc[len(result_df)] = result

        init_quantity = end_quantity
        init_value = end_value

result_df.to_csv('./data/result.csv')