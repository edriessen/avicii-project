import pandas as pd

def find_next_row(df, current_row, n_iter, active_titles):
    current_score = current_row['score']
    current_magnitude = current_row['magnitude']
    if n_iter == 0:
        df_filtered = df[
          (df['score'] >= current_score) &
          (df['magnitude'] >= current_magnitude) &
          (~df['title'].isin(active_titles))
        ].sort_values(['score']).reset_index(drop=True)
        if len(df_filtered) == 0:
            df_filtered = df[
              (df['score'] >= current_score) &
              (~df['title'].isin(active_titles))
            ].sort_values(['score']).reset_index(drop=True)
    else:
        df_filtered = df[
          (df['score'] >= current_score) &
          (
            (df['magnitude'].abs() >= current_magnitude) |
            ((df['magnitude'] - current_magnitude).abs() <= 1.1)
          ) &
          (~df['title'].isin(active_titles))
        ].sort_values(['score']).reset_index(drop=True)
        if len(df_filtered) == 0:
          df_filtered = df[
            (df['score'] >= current_score) &
            (~df['title'].isin(active_titles))
          ].sort_values(['score']).reset_index(drop=True)

    if len(df_filtered) == 0:
        df_filtered = df[
          (df['score'] <= current_score) &
          (~df['title'].isin(active_titles))
        ].sort_values(['score', 'magnitude'], ascending=False).reset_index(drop=True)

    next_row = df_filtered.loc[0]
    return next_row


def sort_df_by_starting_point(df, start_at=''):
    min_score = df['score'].min()
    first_row = {}

    for index, row in df.iterrows():
      if row['score'] == min_score:
        if len(first_row) != 0:
          if row['magnitude'] > first_row['magnitude']:
            first_row = row
        else:
          first_row = row

    current_row = first_row

    for index in range(len(df)-1):
      if index == 0:
        active_rows = [
          first_row
        ]
        active_songs = [
          first_row['title']
        ]

      next_row = find_next_row(df, current_row, index, active_songs)
      active_songs.append(next_row['title'])
      active_rows.append(next_row)
      current_row = next_row

    df_edge = pd.DataFrame(active_rows)[['title', 'score', 'magnitude']].reset_index(drop=True)
    df_edge.reset_index()

    if start_at != '':
        collect = False
        data_custom_sort = []
        for index, row in df_edge.iterrows():
            if row['title'] == start_at:
                collect = True
            if collect:
                data_custom_sort.append(row)
                df_edge = df_edge.drop(index)
        for index, row in df_edge.iterrows():
            data_custom_sort.append(row)
        df_edge = pd.DataFrame(data_custom_sort).reset_index()

    df_edge = df_edge.append(df_edge.loc[0]).reset_index(drop=True)

    return(df_edge)