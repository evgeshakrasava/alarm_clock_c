import re
import os
import datetime



def get_path_from_name(name):
    path = os.path.abspath(name)
    return path
def return_name(path):
    filename = os.path.splitext(path)[0]
    name = filename.split('/')[-1]
    return name




def create_name_path(name,path):
    #name-key is time of creation
    name_path ={}
    name_path[name] = path
    return name_path




def convert_name_to_datetime(name):
    #delete mp4 extens
    file = re.findall(r"[\w']+", name)
    #broke by digit
    w_ext = file[0].split('_')
    #CONVERT!!!!
    #time_creation = datetime.time(year =int(w_ext[3]),month=int(w_ext[2]),day =int(w_ext[1]),
    #                              hour = int(w_ext[6]),min = int(w_ext[7]),sec = int(month[8])
    #fix datetime
    dt = datetime.datetime(int(w_ext[3]),int(w_ext[2]),int(w_ext[1]))
    tm = datetime.time(int(w_ext[6]),int(w_ext[7]),int(w_ext[8]))
    time_creation = dt.combine(dt, tm)
    #datetime_object = datetime.strptime('{}/{}/{} {}:{}:{}'.format(int(w_ext[1]),int(w_ext[2]),int(w_ext[3]), int(w_ext[6]), int(w_ext[7]), int(w_ext[8])), '%m/%d/%Y %I:%M%p')
    return time_creation

def create_limit():
    today = datetime.datetime.now()
    hour = datetime.timedelta(hours =1)
    limit = today - hour
    return limit


def find_older_one_hour_files(name_path):
    #fix compare staff
    limit = create_limit()
    older_one_hour = ""
    for name,path in name_path.items():
        time_creation = convert_name_to_datetime(name)
        if time_creation <= limit:
            older_one_hour = name
    return older_one_hour

def find_weight(path_to_file):
    statinfo = os.stat(get_path_from_name(path_to_file))
    size = statinfo.st_size
    return size


def main():
    #1
    path = get_path_from_name('cam29_25_06_2019___19_40_01.mp4')
    #2
    name = return_name(path)
    name_path = create_name_path(name,path)
    #operation compare and return path

    file_older_one_hour =find_older_one_hour_files(name_path)
    weight = find_weight(file_older_one_hour+'.mp4')
    print(weight)
    return weight


if __name__ == "__main__":
    main()