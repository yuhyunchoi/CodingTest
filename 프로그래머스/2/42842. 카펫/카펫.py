def solution(brown, yellow):
    carpet = brown + yellow
    
    for height in range(3, int(carpet**0.5)+1):
        if carpet % height == 0:
            width = carpet // height
            print("carpet:", carpet, "width:", width, "height:", height)
            
            if (width - 2)*(height - 2) == yellow:
                return [width, height]
    
    

