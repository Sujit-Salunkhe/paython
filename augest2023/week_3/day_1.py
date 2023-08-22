catA=1
catB=3
mouse=2
if (abs((catA-mouse)) > (abs(catB-mouse))):
    print("catB")
elif (abs((catA-mouse)) < abs((catB-mouse))):
    print("catA")
else:
    print("mouseC")

