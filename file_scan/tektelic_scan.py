import scan_content

path_0 = r'C:\Users\MJK\Downloads\log\syslog'
path_1 = r'C:\Users\MJK\Downloads\log\debug'


if __name__=="__main__":
    scan_content.scan_keywords('ip_check_alarm-Checking',path_1, 'tektelic')
    #scan_content.scan_keywords('eth0', path_0, 'tektelic')
    # scan_content.scan_keywords('00 00 00 00',path_2, 'panic')
    # scan_content.scan_keywords('mask', path_2, 'panic')