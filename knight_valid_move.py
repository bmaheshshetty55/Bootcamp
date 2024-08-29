def valid_knight_move(start,end):
    x=abs(start[0]-end[0])
    y=abs(start[1]-end[1])

    if (x==2 and y==1) or (x==1 and y==2):
        return True
    else:
        return False
    
start_x=int(input("Enter the value for x coordinate of start:"))
start_y=int(input("Enter the value for y coordinate of start:"))
start=(start_x, start_y)

end_x=int(input("Enter the value for x coordinate of end:"))
end_y=int(input("Enter the value for y coordinate of end:"))
end=(end_x, end_y)

if valid_knight_move(start,end):
    print("Move is valid")
else:
    print("Move is invalid")
