from matplotlib import pyplot as plot
import matplotlib
from numpy import ceil
# Kroki do rysowania wykresow
# tworz subplota
# wrzuc dane ile chcesz
# wydrukuj subplota

# source https://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct 
def custom_apct (values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct 

def generate_a_bar_diagram(x_axis, y_axis,  subplot=None, title="", description="", xlabel="", ylabel="")->matplotlib:
    
    """Draw a bar chart diagram
    
    Parameters
    ----------
    x_axis : list
        list holding names of conversation participants
    y_axis : list
        list holding statistics of meassured data
    description : str
        describes diagram (default is "" )
    xlabel : str
        name for x_axis label (default is "" )
    ylabel : str
        name for x_axis label (default is "" )
    
    """
    """
    if subplot is None:
        fix, ax = plot.subplots()
        ax.barh(x_axis, y_axis, align='center')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        plot.show()
    else:
    """
    subplot.bar(x_axis, y_axis)
    subplot.set_xlabel(xlabel)
    subplot.set_ylabel(ylabel)
    subplot.set_title(title)
   
    
def generate_a_pie_diagram(actual_data, titles, subplot, title="")->matplotlib:
    """Draw a pie diagram
    
    Parameters
    ----------
    actual_data : list
        list of values to be included in diagram
    titles : list
        list of strings that corresponds authors to values
    title : str
        name of diagram (default is "")
    
    """
    subplot.pie(actual_data, labels=titles, autopct=custom_apct(actual_data))
    subplot.set_title(title)

def generate_figures( data, conversation_name = "blank", option="bar", to_save=True ) -> None:
    """ generate figure holding charts dependent on the needs

        Parameters
        ----------
        data : dict
            dictionary holding type of statistics as a key and dictionaries of data as a value

        conversation_name : str, optional
            its a title of whole figure (default is blank)
        
        option: str, optional
            helper parameter to decide which option should be used 
            atm only supported options are "bar" and "pie" (default "bar")
        to_save : bool, optional
            a boolean parameter when it has assigned true, then it saves charts to an png file in img directory, 
            otherwise it displays the figures  (default is set to be True)
    """
    ammount_of_diagrams = len(data)
    col = 1
    plot.figure(figsize=(ammount_of_diagrams*3, ammount_of_diagrams*3))
    plot.tight_layout()
    ite=1
    for  data_name, data_values in data.items():  
        subplot = plot.subplot(ammount_of_diagrams, 1, col )
        col +=1
        if option in "bar":
            generate_a_bar_diagram( list(data_values.keys()), list(data_values.values()),  subplot, data_name)
        if option in "pie":
            generate_a_pie_diagram(list(data_values.values()), list(data_values.keys()),  subplot, data_name)
    if to_save is True:
        plot.savefig("messenger-statistics/img/"+conversation_name+".png")
    else:
        plot.show()
        
