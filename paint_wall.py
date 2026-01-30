def paint_required(lenght,breadth,cover):
    area_wall=lenght*breadth
    canes=float(area_wall/cover)
    print(f" {round(canes,1)} canes required for painting the wall.")

a=float(input("Enter the height of wall(in meter): "))
b=float(input(f"Enter the breadth of the wall(in meter): "))
coverage=7
paint_required(a,b,cover=coverage)