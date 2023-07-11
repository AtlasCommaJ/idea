import csv

print('''

<table id="myTable">
''')

def boolify(val):
    if val == "Yes":
        return '&#9989;'
    else: return '&#10060;'

with open('data.csv', newline='') as inFile:
    data = csv.reader(inFile, delimiter=',')

    for row in data:
        print('''

 <tr>
  <td class="title" style="width:50%;"><a href="{source}" target="_blank">{title} <i class="fa fa-external-link"></i></a></td>
  <td class="author">{author}</td>
  <td class="challenge">{challenge}</td>
  <td class="type">{type}</td>
  <td class="prevention">{prevention}</td>
  <td class="resilience">{resilience}</td>
  <td class="recovery">{recovery}</td>
  <td class="gender">{gender}</td>
  <td class="legal">{legal}</td>
  <td class="institutional">{institutional}</td>
  <td class="management">{management}</td>
 </tr>
        '''.format(
            title=row[0],
            source=row[1],
            challenge=row[2],
            author=row[3],
            type=row[4],
            prevention=boolify(row[5]),
            resilience=boolify(row[6]), 
            recovery=boolify(row[7]),
            gender=boolify(row[8]),
            legal=boolify(row[9]), 
            institutional=boolify(row[10]),
            management=boolify(row[11])
            ))

print('''
</table>

''')
    

