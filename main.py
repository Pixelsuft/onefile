core_files='''
const.js config.js log.js lib.js cpu.js debug.js io.js main.js ide.js
pci.js floppy.js memory.js dma.js pit.js vga.js ps2.js pic.js rtc.js uart.js acpi.js apic.js
ioapic.js hpet.js ne2k.js state.js virtio.js bus.js elf.js kernel.js'''

browser_files='''
main.js screen.js keyboard.js mouse.js serial.js lib.js network.js
 starter.js worker_bus.js print_stats.js filestorage.js'''

lib_files="jor1k.js 9p.js filesystem.js marshall.js utf8.js"

build_files="capstone-x86.min.js libwabt.js"


output_file='build.js'


result=''
file_list=[]

def contact_text(filename):
    global result
    temp_f_r=open(str(filename), 'r')
    if not result=='':
        result+='\n'
    result+=temp_f_r.read()
    temp_f_r.close()


def contact_files(vars, folder):
    vars=str(vars).replace('\n', ' ')
    folder=str(folder).replace('/', '\\')
    if not folder[-1]=='\\':
        folder+='\\'
    for i in vars.split(' '):
        if not i=='':
            file_list.append(folder+i)

contact_files(core_files, "src")
contact_files(build_files, "build")
contact_files(browser_files, "src/browser")
contact_files(lib_files, "lib")
for i in file_list:
    contact_text(i)
temp_f_w=open(str(output_file), 'w')
temp_f_w.write(result)
temp_f_w.close()