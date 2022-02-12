"This module write respective functions that generates the visual charts" 
"""# **VISUALIZATIONS**"""

def plot_charts(df):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    """Bar graph showing the number of stop and search by force for each force"""
    df['force_ids'].value_counts().to_frame().sample(frac=1).plot(kind='bar', figsize=(15,8))
    plt.xlabel('Force')
    plt.ylabel('Count')
    plt.title('Bar graph showing the number of stop and search by force for each force')
    plt.tight_layout()
    plt.show()
    
    """Gender distribution visualization using countplot"""

    fig, ax = plt.subplots(figsize=(15,8))
    sns.countplot(x=df['gender'])
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.title('Gender distribution visualization using countplot')
    plt.tight_layout()
    plt.show()
    
    """Age range distribution visualization using Countplot"""
    fig, ax = plt.subplots(figsize=(15,8))
    sns.countplot(x=df['age_range'])
    plt.xlabel('Age-range')
    plt.ylabel('Count')
    plt.title('Age range distribution visualization using Countplot')
    plt.tight_layout()
    plt.show()
  
    """Pie chart showing comparison of outcome_linked_to_object_of_search"""
    df['outcome_linked_to_object_of_search'].value_counts().to_frame().plot(kind='pie',autopct='%1.1f%%', y='outcome_linked_to_object_of_search', figsize=(15,8))
    plt.title('Pie chart showing comparison of outcome_linked_to_object_of_search')
    plt.tight_layout()
    plt.show()

    """Stacked bar chart showing trend for the "removal_of_more_than_outer_clothing" and 'outcome'"""
    df.groupby('removal_of_more_than_outer_clothing')['outcome'].value_counts().to_frame().rename(columns={'outcome':'count'}).\
    reset_index().pivot("removal_of_more_than_outer_clothing", 'outcome',	'count').plot(kind='barh',stacked=True, width=0.5,figsize=(15,8))
    plt.xlabel('Count')
    plt.title('Stacked bar chart showing trend for the "removal_of_more_than_outer_clothing" and "outcome" ')
    plt.tight_layout()
    plt.show()
  
      
    """Grouped bar chart showing trend of distribution for officer_defined_ethnicity and self_defined_ethnicity"""
    self_defined_ethnicity_extract=list()
    for i in df['self_defined_ethnicity'].values:
      self_defined_ethnicity_extract.append(i[:5])
    df['self_defined_ethnicity_extract']=self_defined_ethnicity_extract
    df['self_defined_ethnicity_extract'].replace('Unkno', 'Unknown', inplace=True)
    df1=df['officer_defined_ethnicity'].value_counts().to_frame()
    df2=df['self_defined_ethnicity_extract'].value_counts().to_frame()
    df3=pd.concat([df1,df2], axis=1)
    df3.plot(kind='bar', figsize=(15,8))
    plt.ylabel('Count')
    plt.xlabel('Ethnicity')
    plt.title('Grouped bar chart showing trend of distribution for officer_defined_ethnicity and self_defined_ethnicity')
    plt.tight_layout()
    plt.show()
  
    """Donut chart showing proportion of search types"""
    df_t=df['type_'].value_counts().to_frame().reset_index()
    colors= ['#FF0000', '#0000FF', '#FFFF00']
    labels=['Person search','Person and Vehicle search','Vehicle search']
    # Pie Chart
    df_t['type_'].plot(kind='pie', colors=colors,labels=labels, autopct='%1.1f%%', pctdistance=0.85,figsize=(15,8))
      
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
      
    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)
    plt.title('Donut chart showing proportion of search types')
    plt.tight_layout()
    plt.show()


    """Propotion of legislation power used for search"""
    df_waffle=df['legislation'].value_counts().to_frame()
    df_waffle['perc']=(df_waffle['legislation']/df_waffle['legislation'].sum()) * 100
    df_waffle.reset_index(inplace=True)
    df_waffle.rename(columns={'index': 'legislation_act'}, inplace=True)
    df_waffle.drop([4,5,6,7,8,9,10], inplace=True)
    from pywaffle import Waffle
    

    # To plot the waffle Chart
    fig = plt.figure(
        FigureClass = Waffle,
        rows = 5,
        title={'label': 'Propotion of legislation power used for search', 'loc': 'left'},
        values = df_waffle.perc,
        labels = ['{} {:.1f}%'.format(k, v) for k, v in zip(df_waffle.legislation_act,df_waffle.perc)], 
        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(df_waffle.perc),'fontsize': 12, 'framealpha': 0},
        figsize=(20,12)
    )
    plt.tight_layout()
    plt.show()
    
    "Number of search by the hour"
    df['Hour'].value_counts().plot(kind='bar')
    plt.ylabel('Count')
    plt.xlabel('Hours')
    plt.title('Number of search by the hour')
    plt.show()

