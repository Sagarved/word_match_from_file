import scan_content

path_0 = r'C:\Users\MJK\Documents\Sagar.Panchal\Panic Button\Testing bugs artifacts\V15\putty-Dev-6-10_14AM'
path_1 = r'C:\Users\MJK\Documents\Sagar.Panchal\Panic Button\Testing bugs artifacts\V15\putty-dev13-channel-8to15'

if __name__=="__main__":
    scan_content.scan_keywords('backtrace',path_1, 'panic')
    scan_content.scan_keywords('00 00 00 00',path_1, 'panic')
    scan_content.scan_keywords('mask', path_1, 'panic')