from books.models import Book
from io import BytesIO
import base64
import matplotlib.pyplot as plt


# function that takes ID


def get_bookname_from_id(val):
    # used to retrieve name from record
    bookname = Book.objects.get(id=val)
    # return name
    return bookname


def get_graph():
    # create BytesIO buffer for image
    buffer = BytesIO()

    # create plot wit bytesIO object as file like object
    plt.savefig(buffer, format='png')

    # set cursor to beginning of stream
    buffer.seek(0)

    # retrieve content of file
    image_png = buffer.getvalue()

    # encode bytes-like object
    graph = base64.b64encode(image_png)

    # decode to get string as output
    graph = graph.decode('utf-8')

    # free up memory of buffer
    buffer.close()

    # return image/graph
    return graph


def get_chart(chart_type, data, **kwargs):
    # switch plot backend to AAG to write to file
    plt.switch_backend('AGG')

    # specify figure size
    fig = plt.figure(figsize=(6, 3))

    # select chart_type based on user input
    if chart_type == '#1':
        # plot bar chart between date on x-axis and qty on y-axis
        plt.bar(data['date_created'], data['quantity'])

    elif chart_type == '#2':
        # generate pie chart based on price
        # book titles as labels
        labels = kwargs.get('labels')
        plt.pie(data['price'], labels=labels)

    elif chart_type == '#3':
        # plot line chart based on date on x-axis and price on y-axis
        plt.plot(data['date_created'], data['price'])

    else:
        print('unknown chart type')

    # specify layout details
    plt.tight_layout()

    # render graph to file
    chart = get_graph()
    return chart
