import classprog as cp
from bidang1dan2 import skem


while True:
    choice = int(input("1. Bidang 1 & 2\n2. Bidang\n3. Bidang 4\n"))
    if choice == 1:
        skem12_calc = skem()
        skem12_calc.main()
    elif choice == 2:
        skem_calc = cp.skem()
        skem_calc.nilai_skem(cp.peng_mas)
        print(skem_calc.final)
    elif choice == 3:
        skem_calc = cp.skem()
        skem_calc.nilai_skem(cp.isr)
        print(skem_calc.final)
    else:
        pass
