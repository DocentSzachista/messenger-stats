from matplotlib import pyplot as plot
import matplotlib
from numpy import ceil
# Kroki do rysowania wykresow
# tworz subplota
# wrzuc dane ile chcesz
# wydrukuj subplota


def generate_a_bar_diagram(x_axis, y_axis, title="", ax=None, description="", xlabel="", ylabel="")->matplotlib:
    
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
    if ax is None:
        fix, ax = plot.subplots()
        ax.barh(x_axis, y_axis, align='center')
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        plot.show()
    else:
        ax.barh(x_axis, y_axis)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
   
    #return plot.barh(x_axis, y_axis, align='center')
    
def generate_a_pie_diagram(actual_data, titles, title=""):
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
    #fix, ax = plot.subplots()
    #ax.pie(actual_data, labels=titles,  autopct='%1.1f%%' )
    #ax.set_title(title)
    #plot.show()

def generate_figures( data, conversation_name = "blank", option="bar" ):
    """ generate figures dependent on the needs

        Parameters
        ----------
        data : dict
            dictionary holding type of statistics as a key and dictionaries of data as a value
        
        conversation_name : str, optional
            its a title of whole figure (default is blank)
        option: str, optional
            helper parameter to decide which option should be used 
            atm only supported options are "bar" and "pie" (default "bar")
    """
    fig, axis = plot.subplots()
    for  data_name, data_values in zip( data, data.values() ):
        #print(ax, data_name, data_values)
        print(list(data_values.keys()), list(data_values.values()), data_name, axis)
        generate_a_bar_diagram(list(data_values.keys()), list(data_values.values()), data_name, axis)
    plot.show()
        


# for the further development
# def generate_fig(n, m ):
#     fig, axis= plot.subplots(n, m)
#     axis[0][0] = generate_diagram()
#     plot.show()

# generate_fig(2, 2)