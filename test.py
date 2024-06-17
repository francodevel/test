import csv

workers = [{"nombre": "Franco", "apellido": "Vasquez", "telefono": "645238"}, {"nombre": "Clark", "apellido": "Kent", "telefono": "6466680"}]
# def csv_writer():
#     with open("file.cvs", "w") as archivo:
#         for index in range(len(workers)):
#             keys = workers[index].keys()
#             csv_writer = csv.DictWriter(archivo, keys)
#             if index == 0:
#                 csv_writer.writeheader()
#             csv_writer.writerow(workers[index])

def csv_writer_with_fieldnames():
    workers = [{"nombre": "Franco", "apellido": "Vasquez", "telefono": "645238"}, {"nombre": "Clark", "apellido": "Kent", "telefono": "6466680"}]
    fieldnames = ['nombre', 'apellido', 'telefono']

    with open("file.csv", "w") as archivo:
        csv_writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        csv_writer.writeheader()
        for worker in workers:
            csv_writer.writerow(worker)

def csv_reader():
    dicts = []
    with open("file.csv", "r") as resource:
        reader = csv.DictReader(resource)
        for row in reader:
            print(row)
            # dicts.append(row)
    
    # print(dicts)
        # print(list_read)

if __name__ == "__main__":
    csv_writer_with_fieldnames()