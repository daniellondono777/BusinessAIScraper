import re


arr = ['Dec-31-22 07:00AM', '06:45AM', '06:00AM', '05:10AM', 'Dec-30-22 05:45PM', '03:41PM', '01:30PM', '09:45AM', '06:45AM', 'Dec-29-22 07:56PM', '08:00AM', 'Dec-28-22 04:36PM', '02:10PM', '09:00AM', '08:19AM', '07:47AM', '07:15AM', '06:47AM', '06:45AM', '05:52AM', 'Dec-27-22 10:44PM', '10:08PM', '05:01PM', '09:26AM', '08:20AM', '07:01AM', '06:00AM', '05:36AM', '05:35AM', '05:06AM', 'Dec-26-22 07:26PM', '02:42PM', '12:48PM', '08:23AM', '06:00AM', '05:31AM', 'Dec-25-22 11:17AM', '08:10AM', 'Dec-24-22 12:28PM', '10:10AM', '08:15AM', 'Dec-23-22 05:45PM', '04:07PM', '03:56PM', '02:46PM', '09:53AM', '08:23AM', '07:20AM', '06:30AM', '06:00AM', '05:59AM', '05:21AM', 'Dec-22-22 04:00PM', '02:01PM', '12:45PM', '11:33AM', '09:42AM', '08:10AM', '07:07AM', '06:02AM', '05:56AM', 'Dec-21-22 09:46PM', '09:24PM', '03:02PM', '02:51PM', '01:15PM', '10:40AM', '10:29AM', 'Dec-20-22 08:20AM', '07:30AM', '07:20AM', '07:00AM', 'Dec-19-22 07:21PM', '01:32PM', '10:19AM', '10:13AM', '10:06AM', '09:01AM', '08:22AM', '08:17AM', '06:19AM', '06:00AM', 'Dec-18-22 11:03PM', '02:09PM', '09:21AM', '09:13AM', '08:11AM', '07:00AM', '06:10AM', 'Dec-17-22 06:40AM', '05:09AM', 'Dec-16-22 04:37PM', '04:27PM', '01:16PM', '11:30AM', '10:49AM', '09:00AM', '08:21AM', '06:30AM', '05:51AM']
pattern_news_content = '\d\d:\d\d(AM|PM)\s.*'
pattern_date = '(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d\d-\d\d\s\d\d:\d\d(AM|PM)'
    

def easy_format(x):
    ret = []
    actual_date = x[0].split(' ')[0]
    for i in range(0, len(x)):
        actual = x[i].split(' ')
        if len(actual) == 2:
            if actual[0] != actual_date:
                actual_date = actual[0]
                ret.append(actual_date + ' ' + actual[1])
            else:
                ret.append(actual_date + ' ' + actual[1])
        if len(actual) == 1:
            ret.append(actual_date + ' ' +actual[0])
    return ret




print(len(easy_format(arr)) == len(arr))