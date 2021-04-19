import os.path

path_home0 = r'C:\Users\MJK\Downloads\647fdafffe00b50f_Logs_2021-04-08T231743.tar\all_logs\orbiwise'
path_home1 = r'C:\Users\MJK\Downloads\647fdafffe00b50f_Logs_2021-04-13T231453.tar\all_logs\orbiwise'
def scan_keywords(word, file, name):
    """
    :param word: word string to match
    :param file: file path (absolute)
    :param name: file name, this file name is not linked with file path
    :return:
    """
    #with open(path_home1 + file) as fp:
    with open(file) as fp:
        counter = 1
        for line in fp:
            #line = fp.readline()
            #print(line)
            counter +=1
            if word in line:
                print("{} {} {}".format(counter,name, line))
            # if word and 'status=ok' and 'rt=19' in line:
            #     print("{} {} {}".format(counter, name, line))

def scan_file_for_word(word, path_home):

        #print("inside scan file")
        file_pre = "\\gwdaemon.log"
        for i in range(50,0,-1):
            file_fullname = file_pre + '.' + str(i)
            full_path = path_home + file_fullname
            #print(full_path)
            if os.path.exists(full_path):
                scan_keywords(word, full_path, file_fullname)
                #print("inside file")

        scan_keywords(word, path_home + file_pre, 'log')

if __name__=="__main__":
    #scan_keywords('[BH]', "\\gwdaemon.log.0")
    #scan_keywords('[BH]', "\\gwdaemon.log")
    #scan_file_for_word('[BH]', path_home0)
    scan_file_for_word('-> status=', path_home0)


