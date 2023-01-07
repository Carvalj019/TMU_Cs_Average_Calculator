import plotly.express as px
months = ['88', '96', '95', '94.75', '94', '92.3', '94', '94', '94', '98.17', '96', '96', '94.50', '94.5', '94', '94', '92', '98.66', '94', '94.5', '95.33', '91', '94.83', '92']
averages = ['DEC', 'FEB', 'APR', 'FEB', 'MAY', 'MAY', 'APR', 'FEB', 'JAN', 'DEC', 'DEC', 'DEC', 'JAN', 'APR', 'MAY', 'MAY', 'MAY', 'DEC', 'FEB', 'MAY', 'MAY', 'MAY', 'MAY', 'MAY']

plot = px.scatter(x = averages, y = months, title='TMU CS Entrance Averages',
                  labels = dict(x="MONTHS", y="AVERAGES"))
plot.show()
