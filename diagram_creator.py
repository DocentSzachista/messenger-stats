from matplotlib import pyplot as plot
import matplotlib
def generate_a_bar_diagram(x_axis=[1, 2, 3], y_axis=[1, 2, 3], title="", description="", xlabel="", ylabel="")->matplotlib:
    """Draw a bar chart diagram"""
    fix, ax = plot.subplots()
    ax.barh(x_axis, y_axis, align='center')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plot.show()
    
    
def generate_a_pie_diagram(actual_data, titles, title="", description="", xlabel="", ylabel=""):
    """Draw a pie diagram"""
    fix, ax = plot.subplots()
    ax.pie(actual_data, labels=titles,  autopct='%1.1f%%' )
    ax.set_title(title)
    plot.show()

# for the further development
# def generate_fig(n, m ):
#     fig, axis= plot.subplots(n, m)
#     axis[0][0] = generate_diagram()
#     plot.show()

# generate_fig(2, 2)