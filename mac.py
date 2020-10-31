import subprocess    #harici komutlari kullanabilmek icin olan kutuphane
import optparse      #farkli opsiyonlar eklemek icin kullanilan kutuphane
import re            #Regex: Degisiklikleri anlamamiz icin kullanacagimiz kutuphane

def get_user_input():

    parse_object = optparse.OptionParser()   #kullanacagimiz opsiyonlar
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")


    return parse_object.parse_args()



def change_mac_address(user_interface,user_mac_address):        #sectigimiz interfaceye gore mac adresi degistirme kodlari
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):                                 #Mac adresinde bir degisiklik var mi diye kontrol regex ile
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))  #str ile string moda cevirme

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac degistiriliyor...!")

(user_input,arguments)= get_user_input()                        #Girilen input degeri ile sonunun basarali olup olmadiginin kontrolu
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac =control_new_mac(str(user_input.interface))
if finalized_mac ==user_input.mac_address:
    print("Basarili...!")
else:
    print("Hata...!")




